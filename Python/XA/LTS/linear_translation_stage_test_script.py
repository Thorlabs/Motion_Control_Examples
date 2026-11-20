import platform

from thorlabs_xa.products.linear_translation_stage import LinearTranslationStage
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_OperatingMode, TLMC_MoveMode, TLMC_ScaleType, TLMC_Wait
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_GeneralMoveParams, TLMC_MoveAbsoluteParams, TLMC_VelocityParams
from thorlabs_xa.shared.system_manager import SystemManager

from thorlabs_xa.shared.xa_error_factory import XADeviceException

LTS300C_PART_NUMBER = "LTS300C"

SIMULATION_CONFIG_STRING = { "PartNumber" : LTS300C_PART_NUMBER, "SerialNumber" : "45000001" }
# TLMC_InfiniteWait
DEFAULT_TIMEOUT = -1

def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:
    system_manager.create_simulation(SIMULATION_CONFIG_STRING)

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = SIMULATION_CONFIG_STRING["PartNumber"]
    device_info.device = SIMULATION_CONFIG_STRING["SerialNumber"]
    device_info.transport = ""

    return device_info

def main() -> None:

    device: LinearTranslationStage | None = None

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
            print (f"{listed_device_info.device_type_description}:{listed_device_info.device} found at {listed_device_info.transport} ({listed_device_info.part_number})")

            if listed_device_info.part_number == LTS300C_PART_NUMBER:
                device_info = listed_device_info

        if not device_info:
            print("No LTS devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
            device_info = create_simulation(system_manager)

    try:
        # Create device object and enable device.
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, LinearTranslationStage)

        DiagnosticsHelper.console(f"Enabling {device_info.device_type_description}...")
        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        enable_state = device.get_enable_state(DEFAULT_TIMEOUT)

        if enable_state == TLMC_EnableState.TLMC_Enabled:
            DiagnosticsHelper.console_green(f"{device_info.device_type_description} enabled.")
        else:
            DiagnosticsHelper.console_error(f"{device_info.device_type_description} not enabled as expected.")
            
        # Get Connected controller part number and available methods.
        DiagnosticsHelper.console(f"Device part number is {device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait).part_number}")

        # Home the stage
        DiagnosticsHelper.console(f"Homing {device_info.device_type_description}")
        device.home(DEFAULT_TIMEOUT)

        # Convert unit methods used to work in real world units.
        physical_position, position_unit = device.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Distance, 1000)
        DiagnosticsHelper.console(f"Physical position: {physical_position}, device unit position: {position_unit}")

        # Test setting parameters. 
        DiagnosticsHelper.console("Testing velocity params...")
        velocity_params = TLMC_VelocityParams()
        velocity_params.acceleration = 1000
        velocity_params.max_velocity = 2000
        velocity_params.min_velocity = 1000

        device.set_velocity_params(velocity_params)

        velocity_params_returned = device.get_velocity_params(DEFAULT_TIMEOUT)

        settings_params_string = DiagnosticsHelper.object_as_string(velocity_params)
        settings_params_returned_string = DiagnosticsHelper.object_as_string(velocity_params_returned)

        DiagnosticsHelper.console(f"Sent: {settings_params_string}")
        DiagnosticsHelper.console(f"Received: {settings_params_returned_string}")

        # Testing move param structures and moves 
        DiagnosticsHelper.console("Testing general move params...")
        move_params = TLMC_GeneralMoveParams()
        move_params.backlash_distance = 200

        device.set_general_move_params(move_params)

        DiagnosticsHelper.console("Testing absolute move params...")
        absolute_move_params = TLMC_MoveAbsoluteParams()
        absolute_move_params.absolute_position = 1000

        device.set_move_absolute_params(absolute_move_params)

        absolute_move_settings_returned = device.get_move_absolute_params(DEFAULT_TIMEOUT)

        move_absolute_params_string = DiagnosticsHelper.object_as_string(absolute_move_params)
        move_absolute_params_returned_string = DiagnosticsHelper.object_as_string(absolute_move_settings_returned)

        DiagnosticsHelper.console(f"Sent: {move_absolute_params_string}")
        DiagnosticsHelper.console(f"Received: {move_absolute_params_returned_string}")

        device.move(TLMC_MoveMode.TLMC_MoveMode_AbsoluteToProgrammedPosition, 0 , DEFAULT_TIMEOUT)

        
    except XADeviceException as e:
        print("Encountered error, code: ", e.error_code)
    
    finally:
        if device is not None:
            DiagnosticsHelper.console("Shutting down LTS...")
            device.disconnect()
            device.close()

        DiagnosticsHelper.console("Shutting down system...")
        system_manager.shutdown()

    DiagnosticsHelper.console("Completed.")

main()