import time
import platform

from thorlabs_xa.products.kpc101 import Kpc101
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import TLMC_EnableState, TLMC_KcubeIoTriggerPolarity, TLMC_KcubeMmi_JoystickGear, TLMC_KcubeMmiLockState, TLMC_OperatingMode, TLMC_PZ_KpcAnalogInputSource, TLMC_PZ_KpcIoTriggerMode, TLMC_PZ_KpcMmi_JoystickDirectionSense, TLMC_PZ_KpcMmi_JoystickMode, TLMC_PZ_KpcMonitorOutputMode, TLMC_PZ_KpcStrainGaugeOption, TLMC_PZ_KpcVoltageRange, TLMC_PZ_OutputVoltageControlSource, TLMC_PZ_OutputWaveformOperatingMode, TLMC_PZ_PositionControlMode, TLMC_ScaleType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_Wait
from thorlabs_xa.shared.params import TLMC_DeviceInfo, TLMC_PZ_KpcIoSettingsParams, TLMC_PZ_KpcIoTriggerParams, TLMC_PZ_KpcMmiParams, TLMC_PZ_OutputVoltageControlSourceParams, TLMC_PZ_OutputWaveformParams
from thorlabs_xa.shared.system_manager import SystemManager

from thorlabs_xa.shared.xa_error_factory import XADeviceException

KPC101_PART_NUMBER = "KPC101"

SIMULATION_CONFIG_STRING = { "PartNumber" : KPC101_PART_NUMBER, "SerialNumber" : "113000001" }
DEFAULT_TIMEOUT = 5000

def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:

    system_manager.create_simulation(SIMULATION_CONFIG_STRING)

    device_info = TLMC_DeviceInfo()

    device_info.device_type_description = SIMULATION_CONFIG_STRING["PartNumber"]
    device_info.device = SIMULATION_CONFIG_STRING["SerialNumber"]
    device_info.transport = ""

    return device_info

def main() -> None:

    device: Kpc101 | None = None

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

            if listed_device_info.part_number == KPC101_PART_NUMBER:
                device_info = listed_device_info

        if not device_info:
            print("No KPC101 devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
            device_info = create_simulation(system_manager)

    try:
        
        # Create device object and enable device.
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Kpc101)

        DiagnosticsHelper.console("Enabling KPC101...")
        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        enable_state = device.get_enable_state(DEFAULT_TIMEOUT)

        if enable_state == TLMC_EnableState.TLMC_Enabled:
            DiagnosticsHelper.console_green("KPC101 enabled.")
        else:
            DiagnosticsHelper.console_error("KPC101 not enabled as expected.")

        # Get Connected controller part number and available methods.
        DiagnosticsHelper.console(f"Device part number is {device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait).part_number}")

        # Convert unit methods used to work in real world units.
        physical_voltage, voltage_unit = device.convert_from_device_units_to_physical(TLMC_ScaleType.TLMC_ScaleType_Voltage, 1000)
        DiagnosticsHelper.console(f"New converted value is: {physical_voltage} Unit: {voltage_unit}.")

        # Test round trip of IO settings params
        DiagnosticsHelper.console("Testing round trip of KPC IO Settings Params...")

        settings_params = TLMC_PZ_KpcIoSettingsParams()
        settings_params.analog_input_source = TLMC_PZ_KpcAnalogInputSource.TLMC_PZ_KpcAnalogInputSource_HubInputA
        settings_params.voltage_limit = 75
        settings_params.voltage_range = TLMC_PZ_KpcVoltageRange.TLMC_PZ_KpcVoltageRange_75Volts
        settings_params.strain_gauge_option = TLMC_PZ_KpcStrainGaugeOption.TLMC_PZ_KpcStrainGaugeOption_Position
        settings_params.filter_cut_off_frequency = 40
        settings_params.force_sense = 50

        device.set_io_settings_params(settings_params)

        settings_params_returned = device.get_io_settings_params(DEFAULT_TIMEOUT)
        
        settings_params_string = DiagnosticsHelper.object_as_string(settings_params)
        settings_params_returned_string = DiagnosticsHelper.object_as_string(settings_params_returned)

        DiagnosticsHelper.console(f"Sent: {settings_params_string}")
        DiagnosticsHelper.console(f"Received: {settings_params_returned_string}")

        if settings_params_string == settings_params_returned_string:

            DiagnosticsHelper.console_green("KPC IO Settings Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("KPC IO Settings Params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of KPC IO Trigger Params...")

        trigger_params = TLMC_PZ_KpcIoTriggerParams()
        trigger_params.trigger_1_mode = TLMC_PZ_KpcIoTriggerMode.TLMC_PZ_KpcIoTriggerMode_InputTriggersVoltagePositionStepDown
        trigger_params.trigger_1_polarity = TLMC_KcubeIoTriggerPolarity.TLMC_KcubeIoTriggerPolarity_ActiveIsLogicHigh
        trigger_params.trigger_2_mode = TLMC_PZ_KpcIoTriggerMode.TLMC_PZ_KpcIoTriggerMode_OutputActiveStrainGaugeLessThanUpperLimit
        trigger_params.trigger_2_polarity = TLMC_KcubeIoTriggerPolarity.TLMC_KcubeIoTriggerPolarity_ActiveIsLogicLow
        trigger_params.monitor_output_mode = TLMC_PZ_KpcMonitorOutputMode.TLMC_PZ_KpcMonitorOutputMode_Software
        trigger_params.monitor_output_software_value = 50
        trigger_params.monitor_filter_cut_off_frequency = 250
        trigger_params.smoothing_samples = 300
        trigger_params.strain_gauge_lower_limit = 20
        trigger_params.strain_gauge_upper_limit = 40

        device.set_io_trigger_params(trigger_params)

        trigger_params_returned = device.get_io_trigger_params(DEFAULT_TIMEOUT)

        trigger_params_string = DiagnosticsHelper.object_as_string(trigger_params)
        trigger_params_returned_string = DiagnosticsHelper.object_as_string(trigger_params_returned)

        DiagnosticsHelper.console(f"Sent: {trigger_params_string}")
        DiagnosticsHelper.console(f"Received: {trigger_params_returned_string}")

        if trigger_params_string == trigger_params_returned_string:

            DiagnosticsHelper.console_green("KPC IO Trigger Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("KPC IO Trigger Params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of KPC MMI Params...")

        mmi_params = TLMC_PZ_KpcMmiParams()
        mmi_params.display_brightness = 20
        mmi_params.display_dim_level = 10
        mmi_params.display_timeout = 5
        mmi_params.joystick_direction_sense = TLMC_PZ_KpcMmi_JoystickDirectionSense.TLMC_PZ_KpcMmiJoystickDirectionSense_Normal
        mmi_params.joystick_gear = TLMC_KcubeMmi_JoystickGear.TLMC_KcubeMmiJoystickGear_High
        mmi_params.joystick_mode = TLMC_PZ_KpcMmi_JoystickMode.TLMC_PZ_KpcMmiJoystickMode_GoesToVoltagePosition
        mmi_params.joystick_position_step_size = 33
        mmi_params.joystick_voltage_step_size = 30
        mmi_params.preset_position_1 = 0
        mmi_params.preset_position_2 = 33
        mmi_params.preset_voltage_1 = 5
        mmi_params.preset_voltage_2 = 40

        device.set_kpc_mmi_params(mmi_params)

        mmi_params_returned = device.get_kpc_mmi_params(DEFAULT_TIMEOUT)

        mmi_params_string = DiagnosticsHelper.object_as_string(mmi_params)
        mmi_params_returned_string = DiagnosticsHelper.object_as_string(mmi_params_returned)

        DiagnosticsHelper.console(f"Sent: {mmi_params_string}")
        DiagnosticsHelper.console(f"Received: {mmi_params_returned_string}")

        if mmi_params_string == mmi_params_returned_string:
 
            DiagnosticsHelper.console_green("KPC MMI Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("KPC MMI Params round trip test failed.")

        DiagnosticsHelper.console("Getting settings...")

        json_settings = device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True)
        DiagnosticsHelper.console(json_settings)

        settings_params = TLMC_PZ_KpcIoSettingsParams()
        settings_params.analog_input_source = TLMC_PZ_KpcAnalogInputSource.TLMC_PZ_KpcAnalogInputSource_HubInputA
        settings_params.voltage_limit = 75
        settings_params.voltage_range = TLMC_PZ_KpcVoltageRange.TLMC_PZ_KpcVoltageRange_75Volts
        settings_params.strain_gauge_option = TLMC_PZ_KpcStrainGaugeOption.TLMC_PZ_KpcStrainGaugeOption_Position
        settings_params.filter_cut_off_frequency = 40
        settings_params.force_sense = 50

        device.set_io_settings_params(settings_params)

        settings_params_returned = device.get_io_settings_params(DEFAULT_TIMEOUT)
        
        settings_params_string = DiagnosticsHelper.object_as_string(settings_params)
        settings_params_returned_string = DiagnosticsHelper.object_as_string(settings_params_returned)

        DiagnosticsHelper.console(f"Sent: {settings_params_string}")
        DiagnosticsHelper.console(f"Received: {settings_params_returned_string}")

        if settings_params_string == settings_params_returned_string:

            DiagnosticsHelper.console_green("KPC IO Settings Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("KPC IO Settings Params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of KPC IO Trigger Params...")

        trigger_params = TLMC_PZ_KpcIoTriggerParams()
        trigger_params.trigger_1_mode = TLMC_PZ_KpcIoTriggerMode.TLMC_PZ_KpcIoTriggerMode_InputTriggersVoltagePositionStepDown
        trigger_params.trigger_1_polarity = TLMC_KcubeIoTriggerPolarity.TLMC_KcubeIoTriggerPolarity_ActiveIsLogicHigh
        trigger_params.trigger_2_mode = TLMC_PZ_KpcIoTriggerMode.TLMC_PZ_KpcIoTriggerMode_OutputActiveStrainGaugeLessThanUpperLimit
        trigger_params.trigger_2_polarity = TLMC_KcubeIoTriggerPolarity.TLMC_KcubeIoTriggerPolarity_ActiveIsLogicLow
        trigger_params.monitor_output_mode = TLMC_PZ_KpcMonitorOutputMode.TLMC_PZ_KpcMonitorOutputMode_Software
        trigger_params.monitor_output_software_value = 50
        trigger_params.monitor_filter_cut_off_frequency = 250
        trigger_params.smoothing_samples = 300
        trigger_params.strain_gauge_lower_limit = 20
        trigger_params.strain_gauge_upper_limit = 40

        device.set_io_trigger_params(trigger_params)

        trigger_params_returned = device.get_io_trigger_params(DEFAULT_TIMEOUT)

        trigger_params_string = DiagnosticsHelper.object_as_string(trigger_params)
        trigger_params_returned_string = DiagnosticsHelper.object_as_string(trigger_params_returned)

        DiagnosticsHelper.console(f"Sent: {trigger_params_string}")
        DiagnosticsHelper.console(f"Received: {trigger_params_returned_string}")

        if trigger_params_string == trigger_params_returned_string:

            DiagnosticsHelper.console_green("KPC IO Trigger Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("KPC IO Trigger Params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of KPC MMI Params...")

        mmi_params = TLMC_PZ_KpcMmiParams()
        mmi_params.display_brightness = 20
        mmi_params.display_dim_level = 10
        mmi_params.display_timeout = 5
        mmi_params.joystick_direction_sense = TLMC_PZ_KpcMmi_JoystickDirectionSense.TLMC_PZ_KpcMmiJoystickDirectionSense_Normal
        mmi_params.joystick_gear = TLMC_KcubeMmi_JoystickGear.TLMC_KcubeMmiJoystickGear_High
        mmi_params.joystick_mode = TLMC_PZ_KpcMmi_JoystickMode.TLMC_PZ_KpcMmiJoystickMode_GoesToVoltagePosition
        mmi_params.joystick_position_step_size = 30
        mmi_params.joystick_voltage_step_size = 30
        mmi_params.preset_position_1 = 0
        mmi_params.preset_position_2 = 30
        mmi_params.preset_voltage_1 = 5
        mmi_params.preset_voltage_2 = 40

        device.set_kpc_mmi_params(mmi_params)

        mmi_params_returned = device.get_kpc_mmi_params(DEFAULT_TIMEOUT)

        mmi_params_string = DiagnosticsHelper.object_as_string(mmi_params)
        mmi_params_returned_string = DiagnosticsHelper.object_as_string(mmi_params_returned)

        DiagnosticsHelper.console(f"Sent: {mmi_params_string}")
        DiagnosticsHelper.console(f"Received: {mmi_params_returned_string}")

        if mmi_params_string == mmi_params_returned_string:
 
            DiagnosticsHelper.console_green("KPC MMI Params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("KPC MMI Params round trip test failed.")

        DiagnosticsHelper.console("Getting settings...")

        json_settings = device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True)
        DiagnosticsHelper.console(json_settings)

        # Set to open loop position control mode
        DiagnosticsHelper.console("Setting to open loop control mode...")
        device.set_position_control_mode(TLMC_PZ_PositionControlMode.TLMC_PZ_PositionControlMode_OpenLoop)

        position_control_mode_returned = device.get_position_control_mode(DEFAULT_TIMEOUT)
        
        if position_control_mode_returned == TLMC_PZ_PositionControlMode.TLMC_PZ_PositionControlMode_OpenLoop:

            DiagnosticsHelper.console_green("KPC set to open loop.")

        else:

            DiagnosticsHelper.console_error(f"KPC not set to open loop (set to {position_control_mode_returned}).")

        # Set a new target output voltage and wait
        DiagnosticsHelper.console("Setting output voltage and waiting...")
        device.set_output_voltage(25)

        time.sleep(3)

        print("New output voltage is:", device.get_output_voltage(DEFAULT_TIMEOUT))

        io_settings_params = device.get_io_settings_params(DEFAULT_TIMEOUT)        
        print("Output voltage limit is:", io_settings_params.voltage_limit)

        status_items_count = device.get_status_item_count()
        status_items = device.get_status_items(0, status_items_count)

        for status_item in status_items:
            DiagnosticsHelper.console_object(status_item)

        error_status_item = device.get_status_item(TLMC_StatusItemId.TLMC_StatusItemId_Error)
        print (f"Error status item: ID {error_status_item.id.name}, Value: {error_status_item.value}, Value type: {error_status_item.value_type.name}")

        connected_product = device.get_connected_product_info()
        print(f"Product name: {connected_product.product_name}")

        device_firmware_version, required_firmware_version = device.get_firmware_version_info(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console_object(device_firmware_version)
        DiagnosticsHelper.console_object(required_firmware_version)

        hardware_info = device.get_hardware_info(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console_object(hardware_info)

        DiagnosticsHelper.console("Testing round trip of Kcube MMI lock state...")
        lock_state = TLMC_KcubeMmiLockState.TLMC_KcubeMmiLockState_Locked
        device.set_kcube_mmi_lock_state(lock_state)

        lock_state_returned = device.get_kcube_mmi_lock_state(DEFAULT_TIMEOUT)

        DiagnosticsHelper.console(f"Sent: {lock_state.name}")
        DiagnosticsHelper.console(f"Received: {lock_state_returned.name}")

        if (lock_state == lock_state_returned):

            DiagnosticsHelper.console_green(f"MMI lock state set to set to {lock_state.name} as expected.")

        else:

            DiagnosticsHelper.console_error(f"MMI lock state not set to {lock_state.name} as expected (set to {lock_state_returned.name}.")

        DiagnosticsHelper.console("Testing round trip of max travel...")

        max_travel = 50
        device.set_max_travel(max_travel)

        max_travel_returned = device.get_max_travel(DEFAULT_TIMEOUT)
        
        if max_travel == max_travel_returned:

            DiagnosticsHelper.console_green(f"Max travel set to {max_travel} as expected.")

        else:

            DiagnosticsHelper.console_error(f"Max travel not set to {max_travel_returned} as expected.")

        DiagnosticsHelper.console("Testing round trip of output voltage control source params...")

        source_params = TLMC_PZ_OutputVoltageControlSourceParams()
        source_params.source = TLMC_PZ_OutputVoltageControlSource.TLMC_PZ_OutputVoltageControlSource_Knob

        device.set_output_voltage_control_source_params(source_params)

        source_params_returned = device.get_output_voltage_control_source_params(DEFAULT_TIMEOUT)

        source_params_string = DiagnosticsHelper.object_as_string(source_params)
        source_params_returned_string = DiagnosticsHelper.object_as_string(source_params_returned)

        DiagnosticsHelper.console(f"Sent: {source_params_string}")
        DiagnosticsHelper.console(f"Received: {source_params_returned_string}")

        if source_params_string == source_params_returned_string:

            DiagnosticsHelper.console_green("Output voltage control source params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Output voltage control source params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of output waveform params...")

        waveform_params = TLMC_PZ_OutputWaveformParams()
        waveform_params.mode = TLMC_PZ_OutputWaveformOperatingMode.TLMC_PZ_OutputWaveformOperatingMode_OutputGated
        waveform_params.inter_sample_delay = 500
        waveform_params.number_of_cycles = 30
        waveform_params.number_of_samples_between_trigger_repetition = 30
        waveform_params.number_of_samples_per_cycle = 30
        waveform_params.output_trigger_start_index = 3
        waveform_params.output_trigger_width = 20
        waveform_params.post_cycle_delay = 20
        waveform_params.pre_cycle_delay = 10

        device.set_output_waveform_params(waveform_params)

        waveform_params_returned = device.get_output_waveform_params(DEFAULT_TIMEOUT)

        waveform_params_string = DiagnosticsHelper.object_as_string(waveform_params)
        waveform_params_returned_string = DiagnosticsHelper.object_as_string(waveform_params_returned)

        DiagnosticsHelper.console(f"Sent: {waveform_params_string}")
        DiagnosticsHelper.console(f"Received: {waveform_params_returned_string}")

        if waveform_params_string == waveform_params_returned_string:

             DiagnosticsHelper.console_green("Output waveform params round trip test passed.")

        else:

            DiagnosticsHelper.console_error("Output waveform params round trip test failed.")

        DiagnosticsHelper.console_object(device.get_piezo_status(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console_object(device.get_piezo_status_bits(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console_object(device.get_preferred_physical_unit(TLMC_ScaleType.TLMC_ScaleType_Voltage))

        settings_items = device.get_settings_items()

        for settings_item in settings_items:
            DiagnosticsHelper.console_object(settings_item)

    except XADeviceException as e:

        print("Encountered error, code: ", e.error_code)

    finally:

        if device is not None:
            DiagnosticsHelper.console("Shutting down KPC101...")
            device.disconnect()
            device.close()

        DiagnosticsHelper.console("Shutting down system...")
        system_manager.shutdown()

    DiagnosticsHelper.console("Completed.")

main()