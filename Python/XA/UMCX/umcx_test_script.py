import platform

from thorlabs_xa.products.umcx import Umcx
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import (
    TLMC_AuxIoPortMode,
    TLMC_AuxIoPortNumber,
    TLMC_MoveSyncStartTrigger,
    TLMC_OperatingMode,
    TLMC_RackBayNumber,
    TLMC_SettingStringFormat,
)
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_MoveSyncArray, TLMC_MoveSyncParams, TLMC_MoveSyncStartParams
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException

UMCX_PART_NUMBER = "UMC1"
DEFAULT_TIMEOUT = 5000

SIMULATION_CONFIG_STRING = {
    "PartNumber": UMCX_PART_NUMBER,
    "SerialNumber": "121000002",
    "Channels": [
        {
            "BayNumber": 1,
            "SerialNumber": "126000003",
            "ActuatorType": "DDS220",
        }
    ],
}


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:
    system_manager.create_simulation(SIMULATION_CONFIG_STRING)

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = str(SIMULATION_CONFIG_STRING["PartNumber"])
    device_info.device = str(SIMULATION_CONFIG_STRING["SerialNumber"])
    device_info.transport = ""

    return device_info


def main() -> None:
    device: Umcx | None = None

    system_manager = SystemManager.instance()

    if platform.system() == "Linux":
        # If using Linux, we are required to state the port explicitly. Replace if you require an alternative port.
        system_manager.startup("deviceDiscovery.connections=/dev/ttyUSB0")
    else:
        system_manager.startup()

    devices = system_manager.get_device_list()
    device_info: TLMC_DeviceInfo | None = None

    if not devices:
        print("No devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
        device_info = create_simulation(system_manager)
    else:
        print("Devices found:")
        for listed_device_info in devices:
            print(f"{listed_device_info.device_type_description}:{listed_device_info.device} found at {listed_device_info.transport} ({listed_device_info.part_number})")

            if listed_device_info.part_number == UMCX_PART_NUMBER:
                device_info = listed_device_info

        if not device_info:
            print("No UMCX devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
            device_info = create_simulation(system_manager)

    try:
        device = system_manager.open_device_as(
            device_info.device,
            device_info.transport,
            TLMC_OperatingMode.TLMC_OperatingMode_Default,
            Umcx,
        )

        DiagnosticsHelper.console("Getting hardware info...")
        DiagnosticsHelper.console_object(device.get_hardware_info(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console("Getting firmware version info...")
        application_firmware, device_firmware = device.get_firmware_version_info(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Application firmware: {application_firmware}")
        DiagnosticsHelper.console(f"Device firmware: {device_firmware}")

        DiagnosticsHelper.console("Testing AUX IO port mode round trip...")
        test_port = TLMC_AuxIoPortNumber.TLMC_AuxIoPortNumber_Port1
        device.set_aux_io_port_mode(
            test_port,
            TLMC_AuxIoPortMode.TLMC_AuxIoPortMode_SoftwareControlled,
        )

        aux_mode_returned = device.get_aux_io_port_mode(test_port, DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(f"Received AUX IO mode: {aux_mode_returned}")

        if aux_mode_returned == TLMC_AuxIoPortMode.TLMC_AuxIoPortMode_SoftwareControlled:
            DiagnosticsHelper.console_green("AUX IO port mode round trip test passed.")
        else:
            DiagnosticsHelper.console_error("AUX IO port mode round trip test failed.")

        DiagnosticsHelper.console("Testing AUX IO software states round trip...")
        software_states = 0x01
        device.set_aux_io_software_states(software_states)

        software_states_returned = device.get_aux_io_software_states(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(f"Sent: {software_states}")
        DiagnosticsHelper.console(f"Received: {software_states_returned}")

        if software_states == software_states_returned:
            DiagnosticsHelper.console_green("AUX IO software states round trip test passed.")
        else:
            DiagnosticsHelper.console_error("AUX IO software states round trip test failed.")

        DiagnosticsHelper.console("Reading rack bay 1 occupied state...")
        bay_1_state = device.get_rack_bay_occupied_state(TLMC_RackBayNumber.TLMC_RackBayNumber_1, DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Rack bay 1 state: {bay_1_state}")

        # Send new move sync array to the controller
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
        move_sync_params = TLMC_MoveSyncParams()
        move_sync_params.array_id = 1
        move_sync_params.cycle_start_index = 127
        move_sync_params.cycle_end_index = 254
        move_sync_params.number_of_cycles = 1
        move_sync_params.end_index = 255
        move_sync_params.deceleration = 10000
        device.set_move_sync_params(move_sync_params)

        # Send new move sync start params to the controller
        move_sync_start_params = TLMC_MoveSyncStartParams()
        move_sync_start_params.array_id = 1
        move_sync_start_params.channels = 3
        move_sync_start_params.trigger = TLMC_MoveSyncStartTrigger.TLMC_MoveSyncStartTrigger_Software
        device.move_sync_start(move_sync_start_params)

        DiagnosticsHelper.console("Getting settings JSON...")
        json_settings = device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True)
        DiagnosticsHelper.console(json_settings)

    except XADeviceException as e:
        print("Encountered error, code:", e.error_code)

    finally:
        if device:
            DiagnosticsHelper.console("Shutting down UMCX...")
            device.disconnect()
            device.close()

        DiagnosticsHelper.console("Shutting down system...")
        system_manager.shutdown()

    DiagnosticsHelper.console("Completed.")


if __name__ == "__main__":
    main()
