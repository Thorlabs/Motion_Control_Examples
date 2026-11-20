import platform

from thorlabs_xa.products.udxc import Udxc
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_JogMode, TLMC_OperatingMode, TLMC_PZ_PositionControlMode, TLMC_ScaleType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_Wait, TLMC_PZIM_AbnormalMoveDetectionState, TLMC_PZIM_ExternalTriggerMode, TLMC_PZIM_IpAddressAssignmentMode
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_PZIM_AbnormalMoveDetectionParams, TLMC_PZIM_ClosedLoopMoveParams, TLMC_PZIM_ClosedLoopParams, TLMC_PZIM_EthernetParams, TLMC_PZIM_ExternalTriggerConfig, TLMC_PZIM_ExternalTriggerParams, TLMC_PZIM_JogParams, TLMC_PZIM_OpenLoopMoveParams
from thorlabs_xa.shared.xa_error_factory import XADeviceException

UDXC_PART_NUMBER = "UDXC"

SIMULATION_CONFIG_STRING = { "PartNumber" : UDXC_PART_NUMBER, "SerialNumber" : "12200001", "ActuatorType" : "PDX1" }
DEFAULT_TIMEOUT = 5000

def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:

    system_manager.create_simulation(SIMULATION_CONFIG_STRING)

    device_info = TLMC_DeviceInfo()

    device_info.device_type_description = SIMULATION_CONFIG_STRING["PartNumber"]
    device_info.device = SIMULATION_CONFIG_STRING["SerialNumber"]
    device_info.transport = ""

    return device_info

def main() -> None:

    device: Udxc | None = None

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

            if listed_device_info.part_number == UDXC_PART_NUMBER:
                device_info = listed_device_info

        if not device_info:
            print("No UDXC devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
            device_info = create_simulation(system_manager)

    try:

        # Create device object and enable device.
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Udxc)

        DiagnosticsHelper.console("Enabling UDXC...")
        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        enable_state = device.get_enable_state(DEFAULT_TIMEOUT)

        if enable_state == TLMC_EnableState.TLMC_Enabled:
            DiagnosticsHelper.console_green("UDXC enabled.")
        else:
            DiagnosticsHelper.console_error("UDXC not enabled as expected.")
            return

        DiagnosticsHelper.console(f"Device part number is {device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait).part_number}")

        # Test round trip of position control mode.
        DiagnosticsHelper.console("Testing round trip of position control mode...")

        device.set_position_control_mode(TLMC_PZ_PositionControlMode.TLMC_PZ_PositionControlMode_OpenLoop, DEFAULT_TIMEOUT)

        position_control_mode_returned = device.get_position_control_mode(DEFAULT_TIMEOUT)

        if position_control_mode_returned == TLMC_PZ_PositionControlMode.TLMC_PZ_PositionControlMode_OpenLoop:

            DiagnosticsHelper.console_green("UDXC set to open loop.")

        else:

            DiagnosticsHelper.console_error(f"UDXC not set to open loop (set to {position_control_mode_returned}).")

        DiagnosticsHelper.console("Testing round trip of abnormal move detection params...")

        abnormal_move_detection_params = TLMC_PZIM_AbnormalMoveDetectionParams()
        abnormal_move_detection_params.state = TLMC_PZIM_AbnormalMoveDetectionState.TLMC_PZIM_AbnormalMoveDetectionState_Enabled

        device.set_abnormal_move_detection_params(abnormal_move_detection_params)

        abnormal_move_detection_params_returned = device.get_abnormal_move_detection_params(DEFAULT_TIMEOUT)

        abnormal_move_detection_params_string = DiagnosticsHelper.object_as_string(abnormal_move_detection_params)
        abnormal_move_detection_params_returned_string = DiagnosticsHelper.object_as_string(abnormal_move_detection_params_returned)

        DiagnosticsHelper.console(f"Sent: {abnormal_move_detection_params_string}")
        DiagnosticsHelper.console(f"Received: {abnormal_move_detection_params_returned_string}")

        if abnormal_move_detection_params_string == abnormal_move_detection_params_returned_string:

            DiagnosticsHelper.console_green("Abnormal move detection params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Abnormal move detection params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of closed loop move params...")

        closed_loop_move_params = TLMC_PZIM_ClosedLoopMoveParams()
        closed_loop_move_params.desired_position = 500

        device.set_closed_loop_move_params(closed_loop_move_params)

        closed_loop_move_params_returned = device.get_closed_loop_move_params(DEFAULT_TIMEOUT)

        closed_loop_move_params_string = DiagnosticsHelper.object_as_string(closed_loop_move_params)
        closed_loop_move_params_returned_string = DiagnosticsHelper.object_as_string(closed_loop_move_params_returned)

        DiagnosticsHelper.console(f"Sent: {closed_loop_move_params_string}")
        DiagnosticsHelper.console(f"Received: {closed_loop_move_params_returned_string}")

        if closed_loop_move_params_string == closed_loop_move_params_returned_string:

            DiagnosticsHelper.console_green("Closed loop move params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Closed loop move params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of closed loop params...")

        closed_loop_params = TLMC_PZIM_ClosedLoopParams()
        closed_loop_params.reference_speed = 40
        closed_loop_params.proportional = 150
        closed_loop_params.integral = 90
        closed_loop_params.derivative = 40
        closed_loop_params.acceleration = 20

        device.set_closed_loop_params(closed_loop_params)

        closed_loop_params_returned = device.get_closed_loop_params(DEFAULT_TIMEOUT)

        closed_loop_params_string = DiagnosticsHelper.object_as_string(closed_loop_params)
        closed_loop_params_returned_string = DiagnosticsHelper.object_as_string(closed_loop_params_returned)

        DiagnosticsHelper.console(f"Sent: {closed_loop_params_string}")
        DiagnosticsHelper.console(f"Received: {closed_loop_params_returned_string}")

        if closed_loop_params_string == closed_loop_params_returned_string:

            DiagnosticsHelper.console_green("Closed loop params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Closed loop params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of ethernet params...")

        ethernet_params = TLMC_PZIM_EthernetParams()
        ethernet_params.ip_address_assignment_mode = TLMC_PZIM_IpAddressAssignmentMode.TLMC_PZIM_IpAddressAssignmentMode_FromParameters
        ethernet_params.ip_address = [192, 168, 1, 100]
        ethernet_params.subnet_mask = [255, 255, 255, 0]
        ethernet_params.gateway_address = [192, 168, 1, 1]

        device.set_ethernet_params(ethernet_params)

        ethernet_params_returned = device.get_ethernet_params(DEFAULT_TIMEOUT)

        ethernet_params_string = DiagnosticsHelper.object_as_string(ethernet_params)
        ethernet_params_returned_string = DiagnosticsHelper.object_as_string(ethernet_params_returned)

        DiagnosticsHelper.console(f"Sent: {ethernet_params_string}")
        DiagnosticsHelper.console(f"Received: {ethernet_params_returned_string}")

        if ethernet_params_string == ethernet_params_returned_string:

            DiagnosticsHelper.console_green("Ethernet params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Ethernet params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of external trigger config...")

        external_trigger_config = TLMC_PZIM_ExternalTriggerConfig()
        external_trigger_config.mode = TLMC_PZIM_ExternalTriggerMode.TLMC_PZIM_ExternalTriggerMode_RelativeMoveWithRisingTriggerEdge

        device.set_external_trigger_config(external_trigger_config)

        external_trigger_config_returned = device.get_external_trigger_config(DEFAULT_TIMEOUT)

        external_trigger_config_string = DiagnosticsHelper.object_as_string(external_trigger_config)
        external_trigger_config_returned_string = DiagnosticsHelper.object_as_string(external_trigger_config_returned)

        DiagnosticsHelper.console(f"Sent: {external_trigger_config_string}")
        DiagnosticsHelper.console(f"Received: {external_trigger_config_returned_string}")

        if external_trigger_config_string == external_trigger_config_returned_string:

            DiagnosticsHelper.console_green("External trigger config round trip test passed.")

        else:

            DiagnosticsHelper.console_error("External trigger config round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of external trigger params...")

        external_trigger_params = TLMC_PZIM_ExternalTriggerParams()
        external_trigger_params.rising_edge_relative_distance = 100
        external_trigger_params.falling_edge_relative_distance = -100
        external_trigger_params.rising_edge_absolute_position_1 = 200
        external_trigger_params.falling_edge_absolute_position_1 = -200
        external_trigger_params.rising_edge_absolute_position_2 = 300
        external_trigger_params.falling_edge_absolute_position_2 = -300
        external_trigger_params.analog_in_gain = 1.0
        external_trigger_params.analog_in_offset = 0
        external_trigger_params.analog_out_gain = 2.0
        external_trigger_params.analog_out_offset = 10

        device.set_external_trigger_params(external_trigger_params)

        external_trigger_params_returned = device.get_external_trigger_params(DEFAULT_TIMEOUT)

        external_trigger_params_string = DiagnosticsHelper.object_as_string(external_trigger_params)
        external_trigger_params_returned_string = DiagnosticsHelper.object_as_string(external_trigger_params_returned)

        DiagnosticsHelper.console(f"Sent: {external_trigger_params_string}")
        DiagnosticsHelper.console(f"Received: {external_trigger_params_returned_string}")

        if external_trigger_params_string == external_trigger_params_returned_string:

            DiagnosticsHelper.console_green("External trigger params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("External trigger params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of jog params...")

        jog_params = TLMC_PZIM_JogParams()
        jog_params.jog_mode = TLMC_JogMode.TLMC_JogMode_SingleStep
        jog_params.open_loop_step_size = 36
        jog_params.open_loop_step_rate = 40
        jog_params.open_loop_acceleration = 20
        jog_params.closed_loop_step_size = 30
        jog_params.closed_loop_speed = 25
        jog_params.closed_loop_acceleration = 20

        device.set_pzim_jog_params(jog_params)

        jog_params_returned = device.get_pzim_jog_params(DEFAULT_TIMEOUT)

        jog_params_string = DiagnosticsHelper.object_as_string(jog_params)
        jog_params_returned_string = DiagnosticsHelper.object_as_string(jog_params_returned)

        DiagnosticsHelper.console(f"Sent: {jog_params_string}")
        DiagnosticsHelper.console(f"Received: {jog_params_returned_string}")

        if jog_params_string == jog_params_returned_string:

            DiagnosticsHelper.console_green("Jog params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Jog params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of open loop move params...")

        open_loop_move_params = TLMC_PZIM_OpenLoopMoveParams()
        open_loop_move_params.target_step_size = 400

        device.set_open_loop_move_params(open_loop_move_params)

        open_loop_move_params_returned = device.get_open_loop_move_params(DEFAULT_TIMEOUT)

        open_loop_move_params_string = DiagnosticsHelper.object_as_string(open_loop_move_params)
        open_loop_move_params_returned_string = DiagnosticsHelper.object_as_string(open_loop_move_params_returned)

        DiagnosticsHelper.console(f"Sent: {open_loop_move_params_string}")
        DiagnosticsHelper.console(f"Received: {open_loop_move_params_returned_string}")

        if open_loop_move_params_string == open_loop_move_params_returned_string:

            DiagnosticsHelper.console_green("Open loop move params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Open loop move params round trip test failed.")

        DiagnosticsHelper.console("Getting current position...")

        current_position = device.get_current_position(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(f"Current position is {current_position}.")

        DiagnosticsHelper.console("Getting piezo inertial motor status...")

        piezo_inertial_motor_status = device.get_piezo_inertial_motor_status(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(DiagnosticsHelper.object_as_string(piezo_inertial_motor_status))

        DiagnosticsHelper.console("Getting trigger target position...")

        trigger_target_position = device.get_trigger_target_position(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(f"Trigger target position is {trigger_target_position}.")

        DiagnosticsHelper.console("Pulse parameter acquisition...")

        device.pulse_para_acquire(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console_green("Pulse parameter acquisition completed.")

        DiagnosticsHelper.console("Getting settings...")

        json_settings = device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True)
        DiagnosticsHelper.console(json_settings)

        status_items_count = device.get_status_item_count()
        status_items = device.get_status_items(0, status_items_count)

        for status_item in status_items:
            DiagnosticsHelper.console_object(status_item)

        error_status_item = device.get_status_item(TLMC_StatusItemId.TLMC_StatusItemId_Error)
        print (f"Error status item: ID {error_status_item.id.name}, Value: {error_status_item.value}, Value type: {error_status_item.value_type.name}")

        connected_product = device.get_connected_product_info()
        print(f"Product name: {connected_product.product_name}")

        DiagnosticsHelper.console("Getting preferred physical unit...")
        DiagnosticsHelper.console_object(device.get_preferred_physical_unit(TLMC_ScaleType.TLMC_ScaleType_Distance))

        physical_position, position_unit = device.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Distance, 1000)
        DiagnosticsHelper.console(f"New converted value is: {physical_position} Unit: {position_unit}.")

    except XADeviceException as e:

        print("Encountered error, code: ", e.error_code)

    finally:

        if device is not None:
            DiagnosticsHelper.console("Shutting down UDXC...")
            device.disconnect()
            device.close()

        DiagnosticsHelper.console("Shutting down system...")
        system_manager.shutdown()

    DiagnosticsHelper.console("Completed.")

main()
