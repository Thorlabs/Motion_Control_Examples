import platform

from thorlabs_xa.products.kst101 import Kst101
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_MoveMode, TLMC_OperatingMode, TLMC_SettingStringFormat, TLMC_StopMode
from thorlabs_xa.shared.params import TLMC_DeviceInfo
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException

KST101_PART_NUMBER = "KST101"
DEFAULT_TIMEOUT = 5000

SIMULATION_CONFIG_STRING = {
    "PartNumber": KST101_PART_NUMBER,
    "SerialNumber": "26100001",
    "ActuatorType": "FW103",
}


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo | None:
    try:
        system_manager.create_simulation(SIMULATION_CONFIG_STRING)
    except XADeviceException as e:
        print(f"Unable to create simulation for {KST101_PART_NUMBER}: {e.error_code}")
        return None

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = KST101_PART_NUMBER
    device_info.device = SIMULATION_CONFIG_STRING["SerialNumber"]
    device_info.transport = ""
    return device_info


def main() -> None:
    device: Kst101 | None = None
    system_manager = SystemManager.instance()

    if platform.system() == "Linux":
        system_manager.startup("deviceDiscovery.connections=/dev/ttyUSB0")
    else:
        system_manager.startup()

    device_info: TLMC_DeviceInfo | None = None
    for listed_device_info in system_manager.get_device_list():
        if listed_device_info.part_number == KST101_PART_NUMBER:
            device_info = listed_device_info

    if not device_info:
        device_info = create_simulation(system_manager)

    if not device_info:
        print("No compatible KST101 device available.")
        system_manager.shutdown()
        return

    try:
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Kst101)

        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)
        DiagnosticsHelper.console(f"Enable state: {device.get_enable_state(DEFAULT_TIMEOUT)}")
        DiagnosticsHelper.console_object(device.get_hardware_info(DEFAULT_TIMEOUT))

        device.move(TLMC_MoveMode.TLMC_MoveMode_ContinuousForward, 300, DEFAULT_TIMEOUT)
        device.stop(TLMC_StopMode.TLMC_StopMode_Immediate, DEFAULT_TIMEOUT)

        device.request_status(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console_object(device.get_stepper_status(DEFAULT_TIMEOUT))
        DiagnosticsHelper.console_object(device.get_universal_status_bits(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console(device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True))

    except XADeviceException as e:
        print("Encountered error, code:", e.error_code)
    finally:
        if device:
            device.disconnect()
            device.close()
        system_manager.shutdown()


if __name__ == "__main__":
    main()
