import platform

from thorlabs_xa.products.lnnx_logical_channel import LnnxLogicalChannel
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_OperatingMode, TLMC_PZ_PositionControlMode, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_DeviceInfo
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException

LNNX_PART_NUMBER = "LNN001"
LNNX_PARENT_SERIAL = "15000001"
LNNX_CHANNEL_SERIAL = "15000002"
DEFAULT_TIMEOUT = 5000

SIMULATION_CONFIG_STRING = {
    "PartNumber": LNNX_PART_NUMBER,
    "SerialNumber": LNNX_PARENT_SERIAL,
    "Channels": [{"BayNumber": 1, "SerialNumber": LNNX_CHANNEL_SERIAL}],
}


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo | None:
    try:
        system_manager.create_simulation(SIMULATION_CONFIG_STRING)
    except XADeviceException as e:
        print(f"Unable to create simulation for LNNX logical channel: {e.error_code}")
        return None

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = "LNNX Logical Channel"
    device_info.device = LNNX_CHANNEL_SERIAL
    device_info.transport = LNNX_PARENT_SERIAL
    return device_info


def main() -> None:
    device: LnnxLogicalChannel | None = None
    system_manager = SystemManager.instance()

    if platform.system() == "Linux":
        system_manager.startup("deviceDiscovery.connections=/dev/ttyUSB0")
    else:
        system_manager.startup()

    device_info: TLMC_DeviceInfo | None = None
    for listed_device_info in system_manager.get_device_list():
        if listed_device_info.device == LNNX_CHANNEL_SERIAL:
            device_info = listed_device_info

    if not device_info:
        device_info = create_simulation(system_manager)

    if not device_info:
        print("No compatible LNNX logical channel available.")
        system_manager.shutdown()
        return

    try:
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, LnnxLogicalChannel)

        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)
        DiagnosticsHelper.console(f"Enable state: {device.get_enable_state(DEFAULT_TIMEOUT)}")
        DiagnosticsHelper.console_object(device.get_hardware_info(DEFAULT_TIMEOUT))

        device.set_position_control_mode(TLMC_PZ_PositionControlMode.TLMC_PZ_PositionControlMode_OpenLoop, DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Position control mode: {device.get_position_control_mode(DEFAULT_TIMEOUT)}")

        device.set_position(600)
        DiagnosticsHelper.console(f"Piezo position: {device.get_position(DEFAULT_TIMEOUT)}")

        DiagnosticsHelper.console_object(device.get_piezo_status(DEFAULT_TIMEOUT))
        DiagnosticsHelper.console_object(device.get_piezo_status_bits(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console(device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True))

    except XADeviceException as e:
        print("Encountered error, code:", e.error_code)
    finally:
        if device:
            device.close()
        system_manager.shutdown()


if __name__ == "__main__":
    main()
