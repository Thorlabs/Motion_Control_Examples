from ctypes import c_bool, c_char, c_double, c_int16, c_int32, c_longlong, c_uint16, c_uint32, c_uint8

from thorlabs_xa.shared.c_params import C_TLMC_AnalogMonitorConfigurationParams, C_TLMC_ButtonParams, C_TLMC_ConnectedProductInfo, C_TLMC_CurrentLoopParams, C_TLMC_DcPidParams, C_TLMC_GeneralMoveParams, C_TLMC_HomeParams, C_TLMC_IoConfigurationParams, C_TLMC_IoTriggerParams, C_TLMC_JogParams, C_TLMC_JoystickParams, C_TLMC_JoystickSettingsParams, C_TLMC_KcubeIoTriggerParams, C_TLMC_KcubeMmiParams, C_TLMC_KcubePositionTriggerParams, C_TLMC_LcdDisplayParams, C_TLMC_LcdMoveParams, C_TLMC_LimitSwitchParams, C_TLMC_MonitorOutputParams, C_TLMC_MotorOutputParams, C_TLMC_MoveAbsoluteParams, C_TLMC_MoveRelativeParams, C_TLMC_PZ_IoTriggerParams, C_TLMC_PZ_KpcIoSettingsParams, C_TLMC_PZ_KpcIoTriggerParams, C_TLMC_PZ_KpcMmiParams, C_TLMC_PZ_LnnxControlLoopParams, C_TLMC_PZ_LnnxNotchFilterParams, C_TLMC_PZ_NanoTrakCircleDiameterLookupTableData, C_TLMC_PZ_NanoTrakCircleHomePositionParams, C_TLMC_PZ_NanoTrakCircleParams, C_TLMC_PZ_NanoTrakEEPROMParams, C_TLMC_PZ_NanoTrakGainParams, C_TLMC_PZ_NanoTrakMode, C_TLMC_PZ_NanoTrakPhaseCompensationParams, C_TLMC_PZ_NanoTrakRangeParams, C_TLMC_PZ_NanoTrakTnaIoSettings, C_TLMC_PZ_NanoTrakTrackThresholdParams, C_TLMC_PZ_OutputVoltageControlSourceParams, C_TLMC_PZ_OutputWaveformLoopTableSample, C_TLMC_PZ_OutputWaveformParams, C_TLMC_PZ_PositionLoopParams, C_TLMC_PZ_SlewRateParams, C_TLMC_PZ_StageInfoParams, C_TLMC_PositionLoopParams, C_TLMC_PotentiometerParams, C_TLMC_PowerParams, C_TLMC_ProfileModeParams, C_TLMC_StageAxisParams, C_TLMC_StepperLoopParams, C_TLMC_TrackSettleParams, C_TLMC_TriggerParamsForDcBrushless, C_TLMC_TriggerParamsForStepper, C_TLMC_Value, C_TLMC_VelocityParams
from thorlabs_xa.shared.params import TLMC_AnalogMonitorConfigurationParams, TLMC_ButtonParams, TLMC_ConnectedProductInfo, TLMC_CurrentLoopParams, TLMC_DcPidParams, TLMC_GeneralMoveParams, TLMC_HomeParams, TLMC_IoConfigurationParams, TLMC_IoTriggerParams, TLMC_JogParams, TLMC_JoystickParams, TLMC_JoystickSettingsParams, TLMC_KcubeIoTriggerParams, TLMC_KcubeMmiParams, TLMC_KcubePositionTriggerParams, TLMC_LcdDisplayParams, TLMC_LcdMoveParams, TLMC_LimitSwitchParams, TLMC_MonitorOutputParams, TLMC_MotorOutputParams, TLMC_MoveAbsoluteParams, TLMC_MoveRelativeParams, TLMC_PZ_IoTriggerParams, TLMC_PZ_KpcIoSettingsParams, TLMC_PZ_KpcIoTriggerParams, TLMC_PZ_KpcMmiParams, TLMC_PZ_LnnxControlLoopParams, TLMC_PZ_LnnxNotchFilterParams, TLMC_PZ_NanoTrakCircleDiameterLookupTableData, TLMC_PZ_NanoTrakCircleHomePositionParams, TLMC_PZ_NanoTrakCircleParams, TLMC_PZ_NanoTrakEEPROMParams, TLMC_PZ_NanoTrakGainParams, TLMC_PZ_NanoTrakMode, TLMC_PZ_NanoTrakPhaseCompensationParams, TLMC_PZ_NanoTrakRangeParams, TLMC_PZ_NanoTrakTnaIoSettings, TLMC_PZ_NanoTrakTrackThresholdParams, TLMC_PZ_OutputVoltageControlSourceParams, TLMC_PZ_OutputWaveformLoopTableSample, TLMC_PZ_OutputWaveformParams, TLMC_PZ_PositionLoopParams, TLMC_PZ_SlewRateParams, TLMC_PZ_StageInfoParams, TLMC_PositionLoopParams, TLMC_PotentiometerParams, TLMC_PowerParams, TLMC_ProfileModeParams, TLMC_StageAxisParams, TLMC_StepperLoopParams, TLMC_TrackSettleParams, TLMC_TriggerParamsForDcBrushless, TLMC_TriggerParamsForStepper, TLMC_Value, TLMC_VelocityParams

MAPPING_STRING_ENCODING = 'utf-8'

class MapPythonToNative:

    @staticmethod
    def string(string: str | None) -> bytes | None:
        if string is None:
            return None

        return string.encode(MAPPING_STRING_ENCODING)
      
    @staticmethod
    def analog_monitor_configuration_params(params: TLMC_AnalogMonitorConfigurationParams) -> C_TLMC_AnalogMonitorConfigurationParams:

        c_params = C_TLMC_AnalogMonitorConfigurationParams()
        c_params.motorChannel = c_uint16(params.motor_channel)
        c_params.systemVariable = c_uint16(params.system_variable)
        c_params.scale = c_int32(params.scale)
        c_params.offset = c_int32(params.offset)

        return c_params
    
    @staticmethod
    def button_params(params: TLMC_ButtonParams) -> C_TLMC_ButtonParams:

        c_params = C_TLMC_ButtonParams()
        c_params.buttonMode = c_uint16(int(params.button_mode))
        c_params.position1 = c_int32(params.position_1)
        c_params.position2 = c_int32(params.position_2)
        c_params.timeout1Milliseconds = c_uint16(params.timeout_1_milliseconds)
        c_params.timeout2Milliseconds = c_uint16(params.timeout_2_milliseconds)

        return c_params
    
    @staticmethod
    def connected_product_info(params: TLMC_ConnectedProductInfo) -> C_TLMC_ConnectedProductInfo:

        c_params = C_TLMC_ConnectedProductInfo()
        c_params.productName = MapPythonToNative.string(params.product_name)
        c_params.axisType = c_uint16(int(params.axis_type))
        c_params.movementType = c_uint16(int(params.movement_type))
        c_params.unitType = c_uint16(int(params.unit_type))
        c_params.distanceScaleFactor = c_double(params.distance_scale_factor)
        c_params.velocityScaleFactor = c_double(params.velocity_scale_factor)
        c_params.accelerationScaleFactor = c_double(params.acceleration_scale_factor)
        c_params.minPosition = c_double(params.min_position)
        c_params.maxPosition = c_double(params.max_position)
        c_params.maxvelcoity = c_double(params.max_velocity)
        c_params.maxAcceleration = c_double(params.max_acceleration)

        return c_params
    
    @staticmethod
    def current_loop_params(params: TLMC_CurrentLoopParams) -> C_TLMC_CurrentLoopParams:

        c_params = C_TLMC_CurrentLoopParams()
        c_params.phase = c_uint16(int(params.phase))
        c_params.proportional = c_uint16(params.proportional)
        c_params.integral = c_uint16(params.integral)
        c_params.integralLimit = c_uint16(params.integral_limit)
        c_params.integralDeadBand = c_uint16(params.integral_dead_band)
        c_params.feedForward = c_uint16(params.feed_forward)

        return c_params
    
    @staticmethod
    def dc_pid_params(params: TLMC_DcPidParams) -> C_TLMC_DcPidParams:

        c_params = C_TLMC_DcPidParams()
        c_params.proportional = c_uint32(params.proportional)
        c_params.integral = c_uint32(params.integral)
        c_params.derivative = c_uint32(params.derivative)
        c_params.integralLimit = c_uint32(params.integral_limit)
        c_params.filterControl = c_uint16(params.filter_control)

        return c_params
    
    @staticmethod
    def general_move_params(params: TLMC_GeneralMoveParams) -> C_TLMC_GeneralMoveParams:

        c_params = C_TLMC_GeneralMoveParams()
        c_params.backlashDistance = c_int32(params.backlash_distance)

        return c_params
    
    @staticmethod
    def home_params(params: TLMC_HomeParams) -> C_TLMC_HomeParams:

        c_params = C_TLMC_HomeParams()
        c_params.direction = c_uint16(int(params.direction))
        c_params.limitSwitch = c_uint16(int(params.limit_switch))
        c_params.velocity = c_uint32(params.velocity)
        c_params.offsetDistance = c_int32(params.offset_distance)

        return c_params
    
    @staticmethod
    def io_configuration_params(params: TLMC_IoConfigurationParams) -> C_TLMC_IoConfigurationParams:

        c_params = C_TLMC_IoConfigurationParams()
        c_params.mode = c_uint16(int(params.mode))
        c_params.triggerOutSource = c_uint16(int(params.trigger_out_source))

        return c_params
    
    @staticmethod
    def io_trigger_params(params: TLMC_IoTriggerParams) -> C_TLMC_IoTriggerParams:

        c_params = C_TLMC_IoTriggerParams()
        c_params.triggerInMode = c_uint16(int(params.trigger_in_mode))
        c_params.triggerInPolarity = c_uint16(int(params.trigger_in_polarity))
        c_params.triggerInSource = c_uint16(int(params.trigger_in_source))
        c_params.triggerOutMode = c_uint16(int(params.trigger_out_mode))
        c_params.triggerOutPolarity = c_uint16(int(params.trigger_out_polarity))
        c_params.triggerOutForwardStartPosition = c_int32(params.trigger_out_forward_start_position)
        c_params.triggerOutForwardInterval = c_int32(params.trigger_out_forward_interval)
        c_params.triggerOutForwardNumberOfPulses = c_int32(params.trigger_out_forward_number_of_pulses)
        c_params.triggerOutReverseStartPosition = c_int32(params.trigger_out_reverse_start_position)
        c_params.triggerOutReverseInterval = c_int32(params.trigger_out_reverse_interval)
        c_params.triggerOutReverseNumberOPulses = c_int32(params.trigger_out_reverse_number_of_pulses)
        c_params.triggerOutPulseWidth = c_uint32(params.trigger_out_pulse_width)
        c_params.triggerOutNumberOfCycles = c_uint32(params.trigger_out_number_of_cycles)

        return c_params
    
    @staticmethod
    def jog_params(params: TLMC_JogParams) -> C_TLMC_JogParams:

        c_params = C_TLMC_JogParams()
        c_params.mode = c_uint16(int(params.mode))
        c_params.stepSize = c_int32(params.step_size)
        c_params.minVelocity = c_uint32(params.min_velocity)
        c_params.acceleration = c_uint32(params.acceleration)
        c_params.maxVelocity = c_uint32(params.max_velocity)
        c_params.stopMode = c_uint16(int(params.stop_mode))

        return c_params

    @staticmethod
    def joystick_params(params: TLMC_JoystickParams) -> C_TLMC_JoystickParams:

        c_params = C_TLMC_JoystickParams()
        c_params.lowGearMaxVelocity = c_uint32(params.low_gear_max_velocity)
        c_params.highGearMaxVelocity = c_uint32(params.high_gear_max_velocity)
        c_params.lowGearAcceleration = c_uint32(params.low_gear_acceleration)
        c_params.highGearAcceleration = c_uint32(params.high_gear_acceleration)
        c_params.directionSense = c_uint16(params.direction_sense)

        return c_params
    
    @staticmethod
    def joystick_settings_params(params: TLMC_JoystickSettingsParams) -> C_TLMC_JoystickSettingsParams:

        c_params = C_TLMC_JoystickSettingsParams()
        c_params.joystickSerialInterface = c_uint8(int(params.joystick_serial_interface))
        c_params.joystickModel = c_uint8(int(params.joystick_model))
        c_params.directionSense[0] = c_uint16(int(params.direction_sense[0]))
        c_params.directionSense[1] = c_uint16(int(params.direction_sense[1]))
        c_params.directionSense[2] = c_uint16(int(params.direction_sense[2]))
        c_params.axisMapping[0] = c_uint8(int(params.axis_mapping[0]))
        c_params.axisMapping[1] = c_uint8(int(params.axis_mapping[1]))
        c_params.axisMapping[2] = c_uint8(int(params.axis_mapping[2]))

        return c_params

    @staticmethod
    def kcube_io_trigger_params(params: TLMC_KcubeIoTriggerParams) -> C_TLMC_KcubeIoTriggerParams:

        c_params = C_TLMC_KcubeIoTriggerParams()
        c_params.trigger1Mode = c_uint16(int(params.trigger_1_mode))
        c_params.trigger1Polarity = c_uint16(int(params.trigger_1_polarity))
        c_params.trigger2Mode = c_uint16(int(params.trigger_2_mode))
        c_params.trigger2Polarity = c_uint16(int(params.trigger_2_polarity))

        return c_params
    
    @staticmethod
    def kcube_mmi_params(params: TLMC_KcubeMmiParams) -> C_TLMC_KcubeMmiParams:

        c_params = C_TLMC_KcubeMmiParams()
        c_params.joystickMode = c_uint16(int(params.joystick_mode))
        c_params.joystickMaxVelocity = c_uint32(params.joystick_max_velocity)
        c_params.joystickAcceleration = c_uint32(params.joystick_acceleration)
        c_params.joystickDirectionSense = c_uint16(params.joystick_direction_sense)
        c_params.presetPosition1 = c_int32(params.preset_position_1)
        c_params.presetPosition2 = c_int32(params.preset_position_2)
        c_params.displayBrightness = c_uint16(params.display_brightness)
        c_params.displayTimeout = c_uint16(params.display_timeout)
        c_params.displayDimLevel = c_uint16(params.display_dim_level)
        c_params.presetPosition3 = c_int32(params.preset_position_3)
        c_params.joystickSensitivity = c_uint16(params.joystick_sensitivity)

        return c_params
    
    @staticmethod
    def kcube_position_trigger_params(params: TLMC_KcubePositionTriggerParams) -> C_TLMC_KcubePositionTriggerParams:

        c_params = C_TLMC_KcubePositionTriggerParams()
        c_params.forwardStartPosition = c_int32(params.forward_start_position)
        c_params.forwardInterval = c_uint32(params.forward_interval)
        c_params.forwardNumberOfPulses = c_uint32(params.forward_number_of_pulses)
        c_params.reverseStartPosition = c_int32(params.reverse_start_position)
        c_params.reverseInterval = c_uint32(params.reverse_interval)
        c_params.reverseNumberOfPulses = c_uint32(params.reverse_number_of_pulses)
        c_params.pulseWidth = c_uint32(params.pulse_width)
        c_params.numberOfCycles = c_uint32(params.number_of_cycles)

        return c_params
    
    @staticmethod
    def lcd_display_params(params: TLMC_LcdDisplayParams) -> C_TLMC_LcdDisplayParams:

        c_params = C_TLMC_LcdDisplayParams()
        c_params.knobSensitivity = c_int16(params.knob_sensitivity)
        c_params.displayBrightness = c_uint16(params.display_brightness)
        c_params.displayTimeout = c_uint16(params.display_timeout)
        c_params.displayDimLevel = c_uint16(params.display_dim_level)

        return c_params
    
    @staticmethod
    def lcd_move_params(params: TLMC_LcdMoveParams) -> C_TLMC_LcdMoveParams:

        c_params = C_TLMC_LcdMoveParams()
        c_params.knobMode = c_uint16(params.knob_mode)
        c_params.jogStepSize = c_int32(params.jog_step_size)
        c_params.acceleration = c_int32(params.acceleration)
        c_params.maxVelocity = c_int32(params.max_velocity)
        c_params.jogStopMode = c_uint16(params.jog_stop_mode)

        for i, v in enumerate(params.preset_position):
            c_params.presetPosition[i] = c_int32(int(v))

        return c_params
    
    @staticmethod
    def limit_switch_params(params: TLMC_LimitSwitchParams) -> C_TLMC_LimitSwitchParams:

        c_params = C_TLMC_LimitSwitchParams()
        c_params.clockwiseHardLimitOperatingMode = c_uint16(int(params.clockwise_limit_mode))
        c_params.counterclockwiseHardLimitOperatingMode = c_uint16(int(params.counterclockwise_limit_mode))
        c_params.clockwiseSoftLimit = c_int32(params.clockwise_soft_limit)
        c_params.counterclockwiseSoftLimit = c_int32(params.counterclockwise_soft_limit)
        c_params.softLimitOperatingMode = c_uint16(int(params.soft_limit_operating_mode))

        return c_params
    
    @staticmethod
    def monitor_output_params(params: TLMC_MonitorOutputParams) -> C_TLMC_MonitorOutputParams:

        c_params = C_TLMC_MonitorOutputParams()
        c_params.monitorOutput = int(params.monitor_output)
        c_params.dac = params.dac

        return c_params

    @staticmethod
    def motor_output_params(params: TLMC_MotorOutputParams) -> C_TLMC_MotorOutputParams:

        c_params = C_TLMC_MotorOutputParams()
        c_params.continuousCurrentLimit = c_uint16(params.continuous_current_limit)
        c_params.energyLimit = c_uint16(params.energy_limit)
        c_params.motorLimit = c_uint16(params.motor_limit)
        c_params.motorBias = c_uint16(params.motor_bias)

        return c_params

    @staticmethod
    def move_absolute_params(params: TLMC_MoveAbsoluteParams) -> C_TLMC_MoveAbsoluteParams:

        c_params = C_TLMC_MoveAbsoluteParams()
        c_params.absolutePosition = c_int32(params.absolute_position)

        return c_params

    @staticmethod
    def move_relative_params(params: TLMC_MoveRelativeParams) -> C_TLMC_MoveRelativeParams:

        c_params = C_TLMC_MoveRelativeParams()
        c_params.relativeDistance = c_int32(params.relative_distance)

        return c_params
    
    @staticmethod
    def position_loop_params(params: TLMC_PositionLoopParams) -> C_TLMC_PositionLoopParams:

        c_params = C_TLMC_PositionLoopParams()
        c_params.proportional = c_uint16(params.proportional)
        c_params.integral = c_uint16(params.integral)
        c_params.integralLimit = c_uint32(params.integral_limit)
        c_params.derivative = c_uint16(params.derivative)
        c_params.servoCycles = c_uint16(params.servo_cycles)
        c_params.scale = c_uint16(params.scale)
        c_params.velocityFeedForward = c_uint16(params.velocity_feed_forward)
        c_params.accelerationFeedForward = c_uint16(params.acceleration_feed_forward)
        c_params.errorLimit = c_uint32(params.error_limit)

        return c_params
    
    @staticmethod
    def power_params(params: TLMC_PowerParams) -> C_TLMC_PowerParams:
        
        c_params = C_TLMC_PowerParams()
        c_params.restFactor = c_uint16(params.rest_factor)
        c_params.moveFactor = c_uint16(params.move_factor)

        return c_params
    
    @staticmethod
    def potentiometer_params(params: TLMC_PotentiometerParams) -> C_TLMC_PotentiometerParams:

        c_params = C_TLMC_PotentiometerParams()
        c_params.deflection0 = c_uint16(params.deflection_0)
        c_params.velocity1 = c_int32(params.velocity_1)
        c_params.deflection1 = c_uint16(params.deflection_1)
        c_params.velocity2 = c_int32(params.velocity_2)
        c_params.deflection2 = c_uint16(params.deflection_2)
        c_params.velocity3 = c_int32(params.velocity_3)
        c_params.deflection3 = c_uint16(params.deflection_3)
        c_params.velocity4 = c_int32(params.velocity_4)

        return c_params
    
    @staticmethod
    def profile_mode_params(params: TLMC_ProfileModeParams) -> C_TLMC_ProfileModeParams:

        c_params = C_TLMC_ProfileModeParams()
        c_params.mode = c_uint16(int(params.mode))
        c_params.jerk = c_uint32(params.jerk)

        return c_params

    @staticmethod
    def pz_kpc_io_settings_params(params: TLMC_PZ_KpcIoSettingsParams) -> C_TLMC_PZ_KpcIoSettingsParams:

        c_params = C_TLMC_PZ_KpcIoSettingsParams()
        c_params.voltageLimit = c_uint16(params.voltage_limit)
        c_params.analogInputSource = c_uint16(int(params.analog_input_source))
        c_params.filterCutOffFrequency = c_uint16(params.filter_cut_off_frequency)
        c_params.voltageRange = c_uint16(int(params.voltage_range))
        c_params.forceSense = c_uint16(params.force_sense)
        c_params.strainGaugeOption = c_uint16(int(params.strain_gauge_option))

        return c_params
    
    @staticmethod
    def pz_kpc_io_trigger_params(params: TLMC_PZ_KpcIoTriggerParams) -> C_TLMC_PZ_KpcIoTriggerParams:

        c_params = C_TLMC_PZ_KpcIoTriggerParams()
        c_params.trigger1Mode = c_uint16(int(params.trigger_1_mode))
        c_params.trigger1Polarity = c_uint16(int(params.trigger_1_polarity))
        c_params.trigger2Mode = c_uint16(int(params.trigger_2_mode))
        c_params.trigger2Polarity = c_uint16(int(params.trigger_2_polarity))
        c_params.strainGaugeLowerLimit = c_int32(params.strain_gauge_lower_limit)
        c_params.strainGaugeUpperLimit = c_int32(params.strain_gauge_upper_limit)
        c_params.smoothingSamples = c_uint16(params.smoothing_samples)
        c_params.monitorFilterCutOffFrequency = c_uint16(params.monitor_filter_cut_off_frequency)
        c_params.monitorOutputSoftwareValue = c_int16(params.monitor_output_software_value)

        return c_params

    @staticmethod
    def pz_io_trigger_params(params: TLMC_PZ_IoTriggerParams) -> C_TLMC_PZ_IoTriggerParams:

        c_params = C_TLMC_PZ_IoTriggerParams()
        c_params.numberOfPortsPerChannel = params.number_of_ports_per_channel
        c_params.portNumber = c_uint16(int(params.port_number))
        c_params.portType = c_uint16(int(params.port_type))
        c_params.mode = c_uint16(int(params.mode))
        c_params.polarity = c_uint16(int(params.polarity))
        c_params.triggerParameter1 = params.trigger_parameter1
        c_params.triggerParameter2 = params.trigger_parameter2

        return c_params

    @staticmethod
    def pz_kpc_mmi_params(params: TLMC_PZ_KpcMmiParams) -> C_TLMC_PZ_KpcMmiParams:

        c_params = C_TLMC_PZ_KpcMmiParams()
        c_params.joystickMode = c_uint16(int(params.joystick_mode))
        c_params.joystickGear = c_uint16(int(params.joystick_gear))
        c_params.joystickVoltageStepSize = c_uint16(params.joystick_voltage_step_size)
        c_params.joystickPositionStepSize = c_uint16(params.joystick_voltage_step_size)
        c_params.joystickDirectionSense = c_uint16(int(params.joystick_direction_sense))
        c_params.presetVoltage1 = c_uint16(params.preset_voltage_1)
        c_params.presetVoltage2 = c_uint16(params.preset_voltage_2)
        c_params.presetPosition1 = c_uint16(params.preset_position_1)
        c_params.presetPosition2 = c_uint16(params.preset_position_2)
        c_params.displayBrightness = c_uint16(params.display_brightness)
        c_params.displayTimeout = c_uint16(params.display_timeout)
        c_params.displayDimLevel = c_uint16(params.display_dim_level)

        return c_params

    @staticmethod
    def pz_lnnx_control_loop_params(params: TLMC_PZ_LnnxControlLoopParams) -> C_TLMC_PZ_LnnxControlLoopParams:

        c_params = C_TLMC_PZ_LnnxControlLoopParams()
        c_params.overrideMode = c_uint8(int(params.override_mode))
        c_params.proportional = params.proportional
        c_params.integral = params.integral
        c_params.derivative = params.derivative
        c_params.feedForward = params.feed_forward

        return c_params
    
    @staticmethod
    def pz_lnnx_notch_filter_params(params: TLMC_PZ_LnnxNotchFilterParams) -> C_TLMC_PZ_LnnxNotchFilterParams:

        c_params = C_TLMC_PZ_LnnxNotchFilterParams()
        c_params.overrideMode = c_uint8(int(params.override_mode))
        c_params.filter1CenterFrequency = params.filter1_center_frequency
        c_params.filter1QualityFactor = params.filter1_quality_factor
        c_params.filter2CenterFrequency = params.filter2_center_frequency
        c_params.filter2QualityFactor = params.filter2_quality_factor

        return c_params

    @staticmethod
    def pz_nano_trak_circle_diameter_lookup_table_data(params: TLMC_PZ_NanoTrakCircleDiameterLookupTableData) -> C_TLMC_PZ_NanoTrakCircleDiameterLookupTableData:

        Array16 = c_uint16 * 16
        c_params = C_TLMC_PZ_NanoTrakCircleDiameterLookupTableData()
        c_params.lookupTableValues = Array16(*[(int(v) & 0xFFFF) for v in params.lookup_table_values])

        return c_params
    
    @staticmethod
    def pz_nano_trak_circle_home_position_params(params: TLMC_PZ_NanoTrakCircleHomePositionParams) -> C_TLMC_PZ_NanoTrakCircleHomePositionParams:
        c_params = C_TLMC_PZ_NanoTrakCircleHomePositionParams()
        c_params.circleHomePositionA = c_uint16(params.circle_home_position_a)
        c_params.circleHomePositionB = c_uint16(params.circle_home_position_b)
        return c_params
    
    @staticmethod
    def pz_nano_trak_circle_params(params: TLMC_PZ_NanoTrakCircleParams) -> C_TLMC_PZ_NanoTrakCircleParams:
        c_params = C_TLMC_PZ_NanoTrakCircleParams()
        c_params.circleDiameterMode = c_uint16(int(params.circle_diameter_mode))
        c_params.circleDiameterSoftware = c_uint16(params.circle_diameter_software)
        c_params.circleOscillationFrequency = c_uint16(params.circle_oscillation_frequency)
        c_params.absolutePowerMinCircleDiameter = c_uint16(params.absolute_power_min_circle_diameter)
        c_params.absolutePowerMaxCircleDiameter = c_uint16(params.absolute_power_max_circle_diameter)
        c_params.absolutePowerAdjustType = c_uint16(int(params.absolute_power_adjust_type))
        return c_params
    
    @staticmethod
    def pz_nano_trak_eeprom_params(params: TLMC_PZ_NanoTrakEEPROMParams) -> C_TLMC_PZ_NanoTrakEEPROMParams:
        c_params = C_TLMC_PZ_NanoTrakEEPROMParams()
        c_params.channelIdentifier = c_uint16(params.channel_identifier)
        c_params.messageId = c_uint16(params.message_id)
        return c_params
    
    @staticmethod
    def pz_nano_trak_gain_params(params: TLMC_PZ_NanoTrakGainParams) -> C_TLMC_PZ_NanoTrakGainParams:
        
        c_params = C_TLMC_PZ_NanoTrakGainParams()
        c_params.gainControlMode = c_uint16(int(params.gain_control_mode))
        c_params.gain = c_int16(params.gain)

        return c_params
    
    @staticmethod
    def pz_nano_trak_mode(params: TLMC_PZ_NanoTrakMode) -> C_TLMC_PZ_NanoTrakMode:

        c_params = C_TLMC_PZ_NanoTrakMode()
        c_params.mode = c_uint8(int(params.mode))
        c_params.state = c_uint8(int(params.state))

        return c_params
    
    @staticmethod
    def pz_nano_trak_phase_compensation_params(params: TLMC_PZ_NanoTrakPhaseCompensationParams) -> C_TLMC_PZ_NanoTrakPhaseCompensationParams:

        c_params = C_TLMC_PZ_NanoTrakPhaseCompensationParams()
        c_params.phaseCompensationMode = c_uint16(int(params.phase_compensation_mode))
        c_params.phaseCompensationASoftware = c_int16(params.phase_compensation_a_software)
        c_params.phaseCompensationBSoftware = c_int16(params.phase_compensation_b_software)

        return c_params
    
    @staticmethod
    def pz_nano_trak_range_params(params: TLMC_PZ_NanoTrakRangeParams) -> C_TLMC_PZ_NanoTrakRangeParams:
        
        c_params = C_TLMC_PZ_NanoTrakRangeParams()
        c_params.rangeMode = c_uint16(int(params.range_mode))
        c_params.rangeUpLimit = c_int16(params.range_up_limit)
        c_params.rangeDownLimit = c_int16(params.range_down_limit)
        c_params.settleSamples = c_int16(params.settle_samples)
        c_params.rangeChangeType = c_uint16(params.range_change_type)
        c_params.rangeType = c_uint16(params.range_type)

        return c_params
    
    @staticmethod
    def pz_nano_trak_tna_io_settings(params: TLMC_PZ_NanoTrakTnaIoSettings) -> C_TLMC_PZ_NanoTrakTnaIoSettings:

        c_params = C_TLMC_PZ_NanoTrakTnaIoSettings()
        c_params.outRangeType = c_uint8(int(params.out_range_type))
        c_params.outRouteType = c_uint8(int(params.out_route_type))
        c_params.signalSourceMode = c_uint8(int(params.signal_source_mode))
        c_params.signalSourceBoostType = c_uint8(int(params.signal_source_boost_type))
        c_params.signalOutputMode = c_uint8(int(params.signal_output_mode))
        c_params.channel1SignalRangeType = c_uint8(int(params.channel_1_signal_range_type))
        c_params.channel2SignalRangeType = c_uint8(int(params.channel_2_signal_range_type))

        return c_params
    
    @staticmethod
    def pz_nano_trak_track_threshold(params: TLMC_PZ_NanoTrakTrackThresholdParams) -> C_TLMC_PZ_NanoTrakTrackThresholdParams:

        c_params = C_TLMC_PZ_NanoTrakTrackThresholdParams()
        c_params.trackThreshold = c_uint32(params.track_threshold)

        return c_params
    
    @staticmethod
    def pz_output_voltage_control_source_params(params: TLMC_PZ_OutputVoltageControlSourceParams) -> C_TLMC_PZ_OutputVoltageControlSourceParams:

        c_params = C_TLMC_PZ_OutputVoltageControlSourceParams()
        c_params.source = c_uint16(int(params.source))

        return c_params
    
    @staticmethod
    def pz_output_waveform_lookup_table_sample(params: TLMC_PZ_OutputWaveformLoopTableSample) -> C_TLMC_PZ_OutputWaveformLoopTableSample:

        c_params = C_TLMC_PZ_OutputWaveformLoopTableSample()
        c_params.index = c_uint16(params.index)
        c_params.voltage = c_uint16(params.voltage)

        return c_params
    
    @staticmethod
    def pz_output_waveform_params(params: TLMC_PZ_OutputWaveformParams) -> C_TLMC_PZ_OutputWaveformParams:

        c_params = C_TLMC_PZ_OutputWaveformParams()
        c_params.interSampleDelay = c_int32(params.inter_sample_delay)
        c_params.mode = c_uint16(int(params.mode))
        c_params.numberOfCycles = c_int32(params.number_of_cycles)
        c_params.numberOfSamplesBetweenTriggerRepetition = c_uint16(params.number_of_samples_between_trigger_repetition)
        c_params.numberOfSamplesPerCycle = c_uint16(params.number_of_samples_per_cycle)
        c_params.outputTriggerStartIndex = c_uint16(params.output_trigger_start_index)
        c_params.outputTriggerWidth = c_int32(params.output_trigger_width)
        c_params.postCycleDelay = c_int32(params.post_cycle_delay)
        c_params.preCycleDelay = c_int32(params.pre_cycle_delay)

        return c_params
    
    @staticmethod
    def pz_position_loop_params(params: TLMC_PZ_PositionLoopParams) -> C_TLMC_PZ_PositionLoopParams:

        c_params = C_TLMC_PZ_PositionLoopParams()
        c_params.proportional = c_uint16(params.proportional)
        c_params.integral = c_uint16(params.integral)

        return c_params
    
    @staticmethod
    def pz_slew_rate_params(params: TLMC_PZ_SlewRateParams) -> C_TLMC_PZ_SlewRateParams:

        c_params = C_TLMC_PZ_SlewRateParams()
        c_params.openSlewRate = c_uint16(params.open_slew_rate)
        c_params.closedLoopSlewRate = c_uint16(params.closed_loop_slew_rate)

        return c_params

    @staticmethod
    def pz_stage_info_params(params: TLMC_PZ_StageInfoParams) -> C_TLMC_PZ_StageInfoParams:

        c_params = C_TLMC_PZ_StageInfoParams()
        c_params.productId = c_uint16(int(params.product_id))
        c_params.stageName = MapPythonToNative.string(c_params.stage_name)
        c_params.serialNumber = params.serial_number
        c_params.maxVoltage = params.max_voltage
        c_params.minNegativeVoltage = params.min_negative_voltage
        c_params.sensorType = c_uint8(int(params.sensor_type))
        c_params.axisType = c_uint16(int(params.axis_type))
        c_params.nominalTravel = params.nominal_travel
        c_params.homePosition = params.home_position

        return c_params

    @staticmethod
    def value(params: TLMC_Value) -> C_TLMC_Value:

        c_params = C_TLMC_Value()

        val = params.value

        if isinstance(val, bool):
            c_params.boolValue = c_bool(val)
        elif isinstance(val, int):
            c_params.int64Value = c_longlong(val)
        else:
            encoded = val.encode("utf-8")[:24]
            padded = encoded + b"\x00" * (24 - len(encoded))
            c_params.String = (c_char * 24).from_buffer_copy(padded)

        return c_params
    
    @staticmethod
    def stage_axis_params(params: TLMC_StageAxisParams) -> C_TLMC_StageAxisParams:

        c_params = C_TLMC_StageAxisParams()
        c_params.typeId = c_uint16(int(params.type_id))
        c_params.axisId = c_uint16(int(params.axis_id))
        c_params.partNumber = MapPythonToNative.string(params.part_number)
        c_params.serialNumber = c_uint32(params.serial_number)
        c_params.countsPerUnit = c_uint32(params.counts_per_unit)
        c_params.minPosition = c_int32(params.min_position)
        c_params.maxPosition = c_int32(params.max_position)
        c_params.maxAcceleration = c_uint32(params.max_acceleration)
        c_params.maxDecceleration = c_uint32(params.max_deceleration)
        c_params.maxVelocity = c_uint32(params.max_velocity)
        c_params.gearBoxRatio = c_uint16(params.gear_box_ratio)

        return c_params
    
    @staticmethod
    def stepper_loop_params(params: TLMC_StepperLoopParams) -> C_TLMC_StepperLoopParams:

        c_params = C_TLMC_StepperLoopParams()
        c_params.loopMode = c_uint16(int(params.loop_mode))
        c_params.proportional = c_int32(params.proportional)
        c_params.integral = c_int32(params.integral)
        c_params.differential = c_int32(params.differential)
        c_params.outputClip = c_int32(params.output_clip)
        c_params.outputTolerance = c_int32(params.output_tolerance)
        c_params.microstepsPerEncoderCount = c_int32(params.microsteps_per_encoder_count)

        return c_params
    
    @staticmethod
    def track_settle_params(params: TLMC_TrackSettleParams) -> C_TLMC_TrackSettleParams:

        c_params = C_TLMC_TrackSettleParams()
        c_params.settleTime = c_uint16(params.settle_time)
        c_params.settleWindow = c_uint16(params.settle_window)
        c_params.trackWindow = c_uint16(params.track_window)

        return c_params
    
    @staticmethod
    def trigger_params_for_dc_brushless(params: TLMC_TriggerParamsForDcBrushless) -> C_TLMC_TriggerParamsForDcBrushless:

        c_params = C_TLMC_TriggerParamsForDcBrushless()
        c_params.modes = c_uint8(int(params.modes))

        return c_params
    
    @staticmethod
    def trigger_params_for_stepper(params: TLMC_TriggerParamsForStepper) -> C_TLMC_TriggerParamsForStepper:

        c_params = C_TLMC_TriggerParamsForStepper()
        c_params.modes = c_uint8(int(params.modes))

        return c_params
    
    @staticmethod
    def velocity_params(params: TLMC_VelocityParams) -> C_TLMC_VelocityParams:

        c_params = C_TLMC_VelocityParams()
        c_params.minVelocity = c_uint32(params.min_velocity)
        c_params.acceleration = c_uint32(params.acceleration)
        c_params.maxVelocity = c_uint32(params.max_velocity)

        return c_params