import platform

from thorlabs_xa.products.bpc30x_logical_channel import Bpc30xLogicalChannel
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_OperatingMode, TLMC_PZ_PositionControlMode, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_DeviceInfo
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException

BPC30X_PART_NUMBER = "BPC303"
BPC30X_PARENT_SERIAL = "71003334"
BPC30X_CHANNEL_SERIAL = "91003335"
DEFAULT_TIMEOUT = 5000

SIMULATION_CONFIG_STRING = {
    "PartNumber": BPC30X_PART_NUMBER,
    "SerialNumber": BPC30X_PARENT_SERIAL,
    "Channels": [
        {"BayNumber": 1, "SerialNumber": BPC30X_CHANNEL_SERIAL, "ActuatorType": "DDS220"},
        {"BayNumber": 2, "SerialNumber": "91003336", "ActuatorType": "DDS300"},
        {"BayNumber": 3, "SerialNumber": "91003337", "ActuatorType": "DDS600"},
    ],
}


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo | None:
    try:
        system_manager.create_simulation(SIMULATION_CONFIG_STRING)
    except XADeviceException as e:
        print(f"Unable to create simulation for {BPC30X_PART_NUMBER}: {e.error_code}")
        return None

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = "BPC30X Logical Channel"
    device_info.device = BPC30X_CHANNEL_SERIAL
    device_info.transport = BPC30X_PARENT_SERIAL
    return device_info


def main() -> None:
    device: Bpc30xLogicalChannel | None = None
    system_manager = SystemManager.instance()

    if platform.system() == "Linux":
        system_manager.startup("deviceDiscovery.connections=/dev/ttyUSB0")
    else:
        system_manager.startup()

    device_info: TLMC_DeviceInfo | None = None
    for listed_device_info in system_manager.get_device_list():
        if listed_device_info.device == BPC30X_CHANNEL_SERIAL:
            device_info = listed_device_info

    if not device_info:
        device_info = create_simulation(system_manager)

    if not device_info:
        print("No compatible BPC30X logical channel available.")
        system_manager.shutdown()
        return

    try:
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Bpc30xLogicalChannel)

        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)
        DiagnosticsHelper.console(f"Enable state: {device.get_enable_state(DEFAULT_TIMEOUT).name}")
        DiagnosticsHelper.console(device.get_hardware_info(DEFAULT_TIMEOUT))

        device.set_position_control_mode(TLMC_PZ_PositionControlMode.TLMC_PZ_PositionControlMode_OpenLoop, DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Position control mode: {device.get_position_control_mode(DEFAULT_TIMEOUT).name}")

        device.set_output_voltage(900)
        DiagnosticsHelper.console(f"Piezo position: {device.get_output_voltage(DEFAULT_TIMEOUT)}")

        DiagnosticsHelper.console(device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True))

    except XADeviceException as e:
        print("Encountered error, code:", e.error_code)
    finally:
        if device:
            device.close()
        system_manager.shutdown()


if __name__ == "__main__":
    main()
