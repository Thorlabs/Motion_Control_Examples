import platform
from typing import cast

from thorlabs_xa.products.pdxc3 import Pdxc3
from thorlabs_xa.products.pdxc3_subchannel import Pdxc3Subchannel
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_MoveMode, TLMC_OperatingMode, TLMC_PZ_PositionControlMode, TLMC_SettingStringFormat, TLMC_StopMode
from thorlabs_xa.shared.params import TLMC_DeviceInfo
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException

PDXC3_PART_NUMBER = "PDXC3"
DEFAULT_TIMEOUT = 5000

SIMULATION_CONFIG_STRING = {
    "PartNumber": PDXC3_PART_NUMBER,
    "SerialNumber": "129000002",
    "Channels": [
        {"BayNumber": 1, "ActuatorType": "PDX1"},
        {"BayNumber": 2, "ActuatorType": "PDX1"},
        {"BayNumber": 3, "ActuatorType": "PDX1"},
    ],
}


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo | None:
    try:
        system_manager.create_simulation(SIMULATION_CONFIG_STRING)
    except XADeviceException as e:
        print(f"Unable to create simulation for {PDXC3_PART_NUMBER}: {e.error_code}")
        return None

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = PDXC3_PART_NUMBER
    device_info.device = str(SIMULATION_CONFIG_STRING["SerialNumber"])
    device_info.transport = ""
    return device_info


def main() -> None:
    parent_device: Pdxc3 | None = None
    device: Pdxc3Subchannel | None = None
    system_manager = SystemManager.instance()

    if platform.system() == "Linux":
        system_manager.startup("deviceDiscovery.connections=/dev/ttyUSB0")
    else:
        system_manager.startup()

    device_info: TLMC_DeviceInfo | None = None
    for listed_device_info in system_manager.get_device_list():
        if listed_device_info.part_number == PDXC3_PART_NUMBER:
            device_info = listed_device_info

    if not device_info:
        device_info = create_simulation(system_manager)

    if not device_info:
        print("No compatible PDXC3 device available.")
        system_manager.shutdown()
        return

    try:
        parent_device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Pdxc3)
        device = cast(Pdxc3Subchannel, parent_device.get_subchannel(1))

        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)
        DiagnosticsHelper.console(f"Enable state: {device.get_enable_state(DEFAULT_TIMEOUT).name}")

        device.set_position_control_mode(TLMC_PZ_PositionControlMode.TLMC_PZ_PositionControlMode_OpenLoop, DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Position control mode: {device.get_position_control_mode(DEFAULT_TIMEOUT).name}")

        device.move(TLMC_MoveMode.TLMC_MoveMode_JogForward, 200, DEFAULT_TIMEOUT)
        device.stop(TLMC_StopMode.TLMC_StopMode_Immediate, DEFAULT_TIMEOUT)

        device.request_status(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console_object(device.get_stage_axis_params(DEFAULT_TIMEOUT))
        DiagnosticsHelper.console(device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True))

    except XADeviceException as e:
        print("Encountered error, code:", e.error_code)
    finally:
        if parent_device:
            parent_device.disconnect()
            parent_device.close()
        system_manager.shutdown()


if __name__ == "__main__":
    main()
