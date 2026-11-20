import platform

from thorlabs_xa.products.kdc101 import Kdc101
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.enums import TLMC_DigitalOutput, TLMC_EnableState, TLMC_HardLimitOperatingMode, TLMC_HomeDirection, TLMC_HomeLimitSwitch, TLMC_JogMode, TLMC_JogStopMode, TLMC_MoveMode, TLMC_OperatingMode, TLMC_SoftLimitOperatingMode, TLMC_Wait
from thorlabs_xa.shared.params import TLMC_DcPidParams, TLMC_DeviceInfo, TLMC_GeneralMoveParams, TLMC_HomeParams, TLMC_JogParams, TLMC_LimitSwitchParams, TLMC_MoveAbsoluteParams, TLMC_MoveRelativeParams
from thorlabs_xa.shared.xa_error_factory import XADeviceException

KDC101_PART_NUMBER = "KDC101"

SIMULATION_CONFIG_STRING = { "PartNumber" : KDC101_PART_NUMBER, "SerialNumber" : "27001234", "ActuatorType" : "MTS25-Z8" }
DEFAULT_TIMEOUT = 5000

def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:

    system_manager.create_simulation(SIMULATION_CONFIG_STRING)

    device_info = TLMC_DeviceInfo()

    device_info.device_type_description = SIMULATION_CONFIG_STRING["PartNumber"]
    device_info.device = SIMULATION_CONFIG_STRING["SerialNumber"]
    device_info.transport = ""

    return device_info

def main() -> None:

    device: Kdc101 | None = None

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

            if listed_device_info.part_number == KDC101_PART_NUMBER:
                device_info = listed_device_info

        if not device_info:
            print("No KDC101 devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
            device_info = create_simulation(system_manager)

    try:

        # Create device object and enable device.
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Kdc101)

        DiagnosticsHelper.console("Enabling KDC101...")
        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        enable_state = device.get_enable_state(DEFAULT_TIMEOUT)

        if enable_state == TLMC_EnableState.TLMC_Enabled:
            DiagnosticsHelper.console_green("KDC101 enabled.")
        else:
            DiagnosticsHelper.console_error("KDC101 not enabled as expected.")
            return

        DiagnosticsHelper.console(f"Device part number is {device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait).part_number}")

        DiagnosticsHelper.console("Testing round trip of DC PID Params...")

        dc_pid_params = TLMC_DcPidParams()
        dc_pid_params.integral = 90
        dc_pid_params.filter_control = 0b00001111
        dc_pid_params.derivative = 40
        dc_pid_params.integral_limit = 45
        dc_pid_params.proportional = 150

        device.set_dc_pid_params(dc_pid_params)

        dc_pid_params_returned = device.get_dc_pid_params(DEFAULT_TIMEOUT)

        dc_pid_params_string = DiagnosticsHelper.object_as_string(dc_pid_params)
        dc_pid_params_returned_string = DiagnosticsHelper.object_as_string(dc_pid_params_returned)

        DiagnosticsHelper.console(f"Sent: {dc_pid_params_string}")
        DiagnosticsHelper.console(f"Received: {dc_pid_params_returned_string}")

        if dc_pid_params_string == dc_pid_params_returned_string:

            DiagnosticsHelper.console_green("DC PID Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("DC PID Params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of digital output states...")

        digital_output = TLMC_DigitalOutput.TLMC_DigitalOutput_1
        device.set_digital_output_states(digital_output)

        digital_output_returned = device.get_digital_output_states(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(f"Sent: {digital_output}")
        DiagnosticsHelper.console(f"Received: {digital_output_returned}")

        if digital_output == digital_output_returned:

            DiagnosticsHelper.console_green("Digital Output States round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Digital Output States round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of general move params...")

        general_move_params = TLMC_GeneralMoveParams()
        general_move_params.backlash_distance = 50

        device.set_general_move_params(general_move_params)

        general_move_params_returned = device.get_general_move_params(DEFAULT_TIMEOUT)

        general_move_params_string = DiagnosticsHelper.object_as_string(general_move_params)
        general_move_params_returned_string = DiagnosticsHelper.object_as_string(general_move_params_returned)

        DiagnosticsHelper.console(f"Sent: {general_move_params_string}")
        DiagnosticsHelper.console(f"Received: {general_move_params_returned_string}")

        if general_move_params_string == general_move_params_returned_string:

            DiagnosticsHelper.console_green("General move params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("General move params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of home params...")

        home_params = TLMC_HomeParams()

        home_params.direction = TLMC_HomeDirection.TLMC_HomeDirection_Forward
        home_params.limit_switch = TLMC_HomeLimitSwitch.TLMC_HomeLimitSwitch_Reverse
        home_params.offset_distance = 40
        home_params.velocity = 50

        device.set_home_params(home_params)

        home_params_returned = device.get_home_params(DEFAULT_TIMEOUT)

        home_params_string = DiagnosticsHelper.object_as_string(home_params)
        home_params_returned_string = DiagnosticsHelper.object_as_string(home_params_returned)

        DiagnosticsHelper.console(f"Sent: {home_params_string}")
        DiagnosticsHelper.console(f"Received: {home_params_returned_string}")

        if home_params_string == home_params_returned_string:

            DiagnosticsHelper.console_green("Home Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Home Params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of jog params...")

        jog_params = TLMC_JogParams()
        jog_params.acceleration = 20
        jog_params.max_velocity = 25
        jog_params.min_velocity = 0
        jog_params.mode = TLMC_JogMode.TLMC_JogMode_SingleStep
        jog_params.step_size = 36
        jog_params.stop_mode = TLMC_JogStopMode.TLMC_JogStopMode_Profiled

        device.set_jog_params(jog_params)

        jog_params_returned = device.get_jog_params(DEFAULT_TIMEOUT)

        jog_params_string = DiagnosticsHelper.object_as_string(jog_params)
        jog_params_returned_string = DiagnosticsHelper.object_as_string(jog_params_returned)

        DiagnosticsHelper.console(f"Sent: {jog_params_string}")
        DiagnosticsHelper.console(f"Received: {jog_params_returned_string}")

        if jog_params_string == jog_params_returned_string:

            DiagnosticsHelper.console_green("Jog Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Jog Params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of limit switch params...")

        limit_switch_params = TLMC_LimitSwitchParams()
        limit_switch_params.clockwise_limit_mode = TLMC_HardLimitOperatingMode.TLMC_HardLimitOperatingMode_SwitchContactMakes
        limit_switch_params.clockwise_soft_limit = 20
        limit_switch_params.counterclockwise_limit_mode = TLMC_HardLimitOperatingMode.TLMC_HardLimitOperatingMode_SwitchContactMakes
        limit_switch_params.counterclockwise_soft_limit = 30
        limit_switch_params.soft_limit_operating_mode = TLMC_SoftLimitOperatingMode.TLMC_SoftLimitOperatingMode_Ignored

        device.set_limit_switch_params(limit_switch_params)

        limit_switch_params_returned = device.get_limit_switch_params(DEFAULT_TIMEOUT)

        limit_switch_params_string = DiagnosticsHelper.object_as_string(limit_switch_params)
        limit_switch_params_returned_string = DiagnosticsHelper.object_as_string(limit_switch_params_returned)

        DiagnosticsHelper.console(f"Sent: {limit_switch_params_string}")
        DiagnosticsHelper.console(f"Received: {limit_switch_params_returned_string}")

        if limit_switch_params_string == limit_switch_params_returned_string:

            DiagnosticsHelper.console_green("Limit Switch Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Limit Switch Params round trip test failed.")

        DiagnosticsHelper.console("Running test move command...")
        device.move(TLMC_MoveMode.TLMC_MoveMode_ContinuousForward, 500, DEFAULT_TIMEOUT)

        DiagnosticsHelper.console("Testing round trip of move absolute params...")

        move_absolute_params = TLMC_MoveAbsoluteParams()
        move_absolute_params.absolute_position = 500

        device.set_move_absolute_params(move_absolute_params)

        move_absolute_params_returned = device.get_move_absolute_params(DEFAULT_TIMEOUT)

        move_absolute_params_string = DiagnosticsHelper.object_as_string(move_absolute_params)
        move_absolute_params_returned_string = DiagnosticsHelper.object_as_string(move_absolute_params_returned)

        DiagnosticsHelper.console(f"Sent: {move_absolute_params_string}")
        DiagnosticsHelper.console(f"Received: {move_absolute_params_returned_string}")

        if move_absolute_params_string == move_absolute_params_returned_string:

            DiagnosticsHelper.console_green("Move Absolute Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Move Absolute Params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of move relative params...")

        move_relative_params = TLMC_MoveRelativeParams()
        move_relative_params.relative_distance = 400

        device.set_move_relative_params(move_relative_params)

        move_relative_params_returned = device.get_move_relative_params(DEFAULT_TIMEOUT)

        move_relative_params_string = DiagnosticsHelper.object_as_string(move_relative_params)
        move_relative_params_returned_string = DiagnosticsHelper.object_as_string(move_relative_params_returned)

        DiagnosticsHelper.console(f"Sent: {move_relative_params_string}")
        DiagnosticsHelper.console(f"Received: {move_relative_params_returned_string}")

        if move_relative_params_string == move_relative_params_returned_string:

            DiagnosticsHelper.console_green("Move Relative Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Move Relative Params round trip test failed.")

        position_counter = 50
        device.set_position_counter(position_counter)

        position_counter_returned = device.get_position_counter(DEFAULT_TIMEOUT)

        if position_counter == position_counter_returned:

            DiagnosticsHelper.console_green("Position Counter round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Position Counter round trip test failed.")

        DiagnosticsHelper.console("Getting universal status...")
        universal_status = device.get_universal_status(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(DiagnosticsHelper.object_as_string(universal_status))

        DiagnosticsHelper.console("Getting universal status bits...")
        universal_status_bits = device.get_universal_status_bits(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(DiagnosticsHelper.object_as_string(universal_status_bits))


    except XADeviceException as e:

        print("Encountered error, code: ", e.error_code)

    finally:

        if device is not None:
            DiagnosticsHelper.console("Shutting down KDC101...")
            device.disconnect()
            device.close()

        DiagnosticsHelper.console("Shutting down system...")
        system_manager.shutdown()

    DiagnosticsHelper.console("Completed.")

main()