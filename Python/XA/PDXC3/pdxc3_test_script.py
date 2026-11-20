import platform

from thorlabs_xa.products.pdxc3 import Pdxc3
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import TLMC_MoveSyncStartTrigger, TLMC_OperatingMode, TLMC_SettingStringFormat
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_MoveSyncArray, TLMC_MoveSyncParams, TLMC_MoveSyncStartParams
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
    device: Pdxc3 | None = None
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
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Pdxc3)

        DiagnosticsHelper.console(device.get_hardware_info(DEFAULT_TIMEOUT))
        application_firmware, device_firmware = device.get_firmware_version_info(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Application firmware: {application_firmware}")
        DiagnosticsHelper.console(f"Device firmware: {device_firmware}")

        # Send new move sync array to the controller
        DiagnosticsHelper.console("Setting example move sync array...")
        
        move_sync_array = TLMC_MoveSyncArray()
        move_sync_array.array_id = 1
        move_sync_array.channels = 3
        move_sync_array.num_points = 3
        move_sync_array.start_index = 0
        move_sync_array.time_positions = [
            0,1100000,1150000,
            250,1119781,1149511,
            250,1139515,1148043,
        ]

        device.set_move_sync_array(move_sync_array)

        # Send new move sync params to the controller
        DiagnosticsHelper.console("Setting example move sync params...")
        
        move_sync_params = TLMC_MoveSyncParams()
        move_sync_params.array_id = 1
        move_sync_params.cycle_start_index = 127
        move_sync_params.cycle_end_index = 254
        move_sync_params.number_of_cycles = 1
        move_sync_params.end_index = 255
        move_sync_params.deceleration = 10000
        device.set_move_sync_params(move_sync_params)

        # Send new move sync start params to the controller
        DiagnosticsHelper.console("Setting example move sync start params...")
        
        move_sync_start_params = TLMC_MoveSyncStartParams()
        move_sync_start_params.array_id = 1
        move_sync_start_params.channels = 3
        move_sync_start_params.trigger = TLMC_MoveSyncStartTrigger.TLMC_MoveSyncStartTrigger_Software
        device.move_sync_start(move_sync_start_params)

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
