import ctypes

from typing import TypeAlias, Union

from thorlabs_xa.shared.c_params import C_TLMC_AdcInputs, C_TLMC_AnalogMonitorConfigurationParams, C_TLMC_ApiVersion, C_TLMC_ButtonParams, C_TLMC_ConnectedProductInfo, C_TLMC_CurrentLoopParams, C_TLMC_DcPidParams, C_TLMC_DeviceInfo, C_TLMC_FirmwareVersion, C_TLMC_GeneralMoveParams, C_TLMC_HardwareInfo, C_TLMC_HomeParams, C_TLMC_IoConfigurationParams, C_TLMC_IoTriggerParams, C_TLMC_JogParams, C_TLMC_JoystickParams, C_TLMC_JoystickSettingsParams, C_TLMC_KcubeIoTriggerParams, C_TLMC_KcubeMmiParams, C_TLMC_KcubePositionTriggerParams, C_TLMC_LcdDisplayParams, C_TLMC_LcdMoveParams, C_TLMC_LimitSwitchParams, C_TLMC_MonitorOutputParams, C_TLMC_MotorOutputParams, C_TLMC_MoveAbsoluteParams, C_TLMC_MoveRelativeParams, C_TLMC_PZ_IoTriggerParams, C_TLMC_PZ_KpcIoSettingsParams, C_TLMC_PZ_KpcIoTriggerParams, C_TLMC_PZ_KpcMmiParams, C_TLMC_PZ_LnnxControlLoopParams, C_TLMC_PZ_LnnxNotchFilterParams, C_TLMC_PZ_MaxOutputVoltageParams, C_TLMC_PZ_NanoTrakCircleDiameterLookupTableData, C_TLMC_PZ_NanoTrakCircleHomePositionParams, C_TLMC_PZ_NanoTrakCircleParams, C_TLMC_PZ_NanoTrakGainParams, C_TLMC_PZ_NanoTrakMode, C_TLMC_PZ_NanoTrakPhaseCompensationParams, C_TLMC_PZ_NanoTrakRangeParams, C_TLMC_PZ_NanoTrakStatus, C_TLMC_PZ_NanoTrakTnaIoSettings, C_TLMC_PZ_NanoTrakTrackThresholdParams, C_TLMC_PZ_OutputVoltageControlSourceParams, C_TLMC_PZ_OutputWaveformParams, C_TLMC_PZ_PositionLoopParams, C_TLMC_PZ_SlewRateParams, C_TLMC_PZ_StageInfoParams, C_TLMC_PZ_Status, C_TLMC_PositionLoopParams, C_TLMC_PotentiometerParams, C_TLMC_PowerParams, C_TLMC_ProfileModeParams, C_TLMC_RichResponse, C_TLMC_Setting, C_TLMC_StageAxisParams, C_TLMC_StatusItem, C_TLMC_StepperLoopParams, C_TLMC_StepperStatus, C_TLMC_TrackSettleParams, C_TLMC_TriggerParamsForDcBrushless, C_TLMC_TriggerParamsForStepper, C_TLMC_UniversalStatus, C_TLMC_VelocityParams
from thorlabs_xa.shared.params import TLMC_AdcInputs, TLMC_AnalogMonitorConfigurationParams, TLMC_ApiVersion, TLMC_ButtonParams, TLMC_ConnectedProductInfo, TLMC_CurrentLoopParams, TLMC_DcPidParams, TLMC_DeviceInfo, TLMC_FirmwareVersion, TLMC_GeneralMoveParams, TLMC_HardwareInfo, TLMC_HomeParams, TLMC_IoConfigurationParams, TLMC_IoTriggerParams, TLMC_JogParams, TLMC_JoystickParams, TLMC_JoystickSettingsParams, TLMC_KcubeIoTriggerParams, TLMC_KcubeMmiParams, TLMC_KcubePositionTriggerParams, TLMC_LcdDisplayParams, TLMC_LcdMoveParams, TLMC_LimitSwitchParams, TLMC_MonitorOutputParams, TLMC_MotorOutputParams, TLMC_MoveAbsoluteParams, TLMC_MoveRelativeParams, TLMC_PZ_IoTriggerParams, TLMC_PZ_KpcIoSettingsParams, TLMC_PZ_KpcIoTriggerParams, TLMC_PZ_KpcMmiParams, TLMC_PZ_LnnxControlLoopParams, TLMC_PZ_LnnxNotchFilterParams, TLMC_PZ_MaxOutputVoltageParams, TLMC_PZ_NanoTrakCircleDiameterLookupTableData, TLMC_PZ_NanoTrakCircleHomePositionParams, TLMC_PZ_NanoTrakCircleParams, TLMC_PZ_NanoTrakGainParams, TLMC_PZ_NanoTrakMode, TLMC_PZ_NanoTrakPhaseCompensationParams, TLMC_PZ_NanoTrakRangeParams, TLMC_PZ_NanoTrakStatus, TLMC_PZ_NanoTrakTnaIoSettings, TLMC_PZ_NanoTrakTrackThresholdParams, TLMC_PZ_OutputVoltageControlSourceParams, TLMC_PZ_OutputWaveformParams, TLMC_PZ_PositionLoopParams, TLMC_PZ_SlewRateParams, TLMC_PZ_StageInfoParams, TLMC_PZ_Status, TLMC_PositionLoopParams, TLMC_PotentiometerParams, TLMC_PowerParams, TLMC_ProfileModeParams, TLMC_RichResponse, TLMC_Setting, TLMC_StageAxisParams, TLMC_StatusItem, TLMC_StepperLoopParams, TLMC_StepperStatus, TLMC_TrackSettleParams, TLMC_TriggerParamsForDcBrushless, TLMC_TriggerParamsForStepper, TLMC_UniversalStatus, TLMC_VelocityParams

from thorlabs_xa.shared.enums import TLMC_AnalogMonitorMotorChannel, TLMC_AnalogMonitorSystemVariable, TLMC_ButtonMode, TLMC_ConnectedProductAxisType, TLMC_ConnectedProductMovementType, TLMC_CurrentLoopPhase, TLMC_DeviceFamily, TLMC_DeviceType, TLMC_HardLimitOperatingMode, TLMC_HomeDirection, TLMC_HomeLimitSwitch, TLMC_IoPortMode, TLMC_IoPortSource, TLMC_IoTriggerPolarity, TLMC_IoTriggerPortNumber, TLMC_JogMode, TLMC_JogStopMode, TLMC_JoystickAxis, TLMC_JoystickDirectionSense, TLMC_JoystickModel, TLMC_JoystickSerialInterface, TLMC_KcubeIoTriggerMode, TLMC_KcubeIoTriggerPolarity, TLMC_KcubeMmi_JoystickDirectionSense, TLMC_KcubeMmi_JoystickGear, TLMC_MonitorOutput, TLMC_PZ_IoTriggerMode, TLMC_PZ_KpcAnalogInputSource, TLMC_PZ_KpcIoTriggerMode, TLMC_PZ_KpcMmi_JoystickDirectionSense, TLMC_PZ_KpcMmi_JoystickMode, TLMC_PZ_KpcMonitorOutputMode, TLMC_PZ_KpcStrainGaugeOption, TLMC_PZ_KpcVoltageRange, TLMC_PZ_LnnxControlLoopParamsOverrideMode, TLMC_PZ_LnnxNotchFilterParamsOverrideMode, TLMC_PZ_NanoTrakAbsolutePowerAdjustType, TLMC_PZ_NanoTrakCircleDiameterMode, TLMC_PZ_NanoTrakGainControlMode, TLMC_PZ_NanoTrakPhaseCompensationMode, TLMC_PZ_NanoTrakRange, TLMC_PZ_NanoTrakRangeChangeType, TLMC_PZ_NanoTrakRangeMode, TLMC_PZ_NanoTrakStatusBit, TLMC_PZ_NanoTrakTrackingMode, TLMC_PZ_NanoTrakTrackingState, TLMC_PZ_NanoTrakUnderOverReadType, TLMC_PZ_OutputVoltageControlSource, TLMC_PZ_OutputWaveformOperatingMode, TLMC_PZ_SensorType, TLMC_PZ_StageProductId, TLMC_PZ_StatusBit, TLMC_PZ_TnaIoSignalOutputMode, TLMC_PZ_TnaIoSignalRangeType, TLMC_PZ_TnaIoSignalSourceBoostType, TLMC_PZ_TnaIoSignalSourceMode, TLMC_PZ_VoltageLimit, TLMC_PortType, TLMC_ScaleType, TLMC_SoftLimitOperatingMode, TLMC_StageAxis_AxisId, TLMC_StageAxis_TypeId, TLMC_StatusItemId, TLMC_StepperLoopParams_LoopMode, TLMC_TriggerModesForDcBrushless, TLMC_TriggerModesForStepper, TLMC_Unit, TLMC_UniversalStatusBit, TLMC_ValueType

BufLike: TypeAlias = (
    ctypes.Array[ctypes.c_char]
    | ctypes.Array[ctypes.c_wchar]
    | ctypes.c_char_p
    | ctypes.c_wchar_p
)

class MapNativeToPython:

    @staticmethod
    def string(arr: BufLike) -> str:
        buffer = bytes(arr)
        buffer = buffer.split(b"\x00", 1)[0]

        return buffer.decode("utf-8", errors="replace")
    
    @staticmethod
    def int(arr: Union[bytes, bytearray, ctypes.Array[ctypes.c_uint8]]) -> int:      
        b = bytes(arr)
        return ctypes.c_uint64(int.from_bytes(b, "little")).value
    
    @staticmethod
    def bool(value: Union[bytes, bytearray]) -> bool:
        return bool(value[0]) if value else False

    @staticmethod
    def adc_inputs(c_params: C_TLMC_AdcInputs) -> TLMC_AdcInputs:

        params = TLMC_AdcInputs()
        params.adc_input_1 = c_params.adcInput1
        params.adc_input_2 = c_params.adcInput2

        return params
    
    @staticmethod
    def analog_monitor_configuration_params(c_params: C_TLMC_AnalogMonitorConfigurationParams) -> TLMC_AnalogMonitorConfigurationParams:
        
        params = TLMC_AnalogMonitorConfigurationParams()
        params.motor_channel = TLMC_AnalogMonitorMotorChannel(c_params.motorChannel)
        params.system_variable = TLMC_AnalogMonitorSystemVariable(c_params.systemVariable)
        params.scale = c_params.scale
        params.offset = c_params.offset

        return params
    
    @staticmethod
    def api_version(c_params: C_TLMC_ApiVersion) -> TLMC_ApiVersion:

        params = TLMC_ApiVersion()
        params.major = c_params.major
        params.minor = c_params.minor
        params.patch = c_params.patch
        params.build = c_params.build
        params.prerelease_label = MapNativeToPython.string(c_params.prereleaseLabel)
        params.display_string = MapNativeToPython.string(c_params.displayString)

        return params
    
    @staticmethod
    def button_params(c_params: C_TLMC_ButtonParams) -> TLMC_ButtonParams:

        params = TLMC_ButtonParams()
        params.button_mode = TLMC_ButtonMode(c_params.buttonMode)
        params.position_1 = c_params.position1
        params.position_2 = c_params.position2
        params.timeout_1_milliseconds = c_params.timeout1Milliseconds
        params.timeout_2_milliseconds = c_params.timeout2Milliseconds

        return params
    
    @staticmethod
    def connected_product_info(c_params: C_TLMC_ConnectedProductInfo) -> TLMC_ConnectedProductInfo:

        params = TLMC_ConnectedProductInfo()
        params.product_name = MapNativeToPython.string(c_params.productName)
        params.part_number = MapNativeToPython.string(c_params.partNumber)
        params.axis_type = TLMC_ConnectedProductAxisType(c_params.axisType)
        params.movement_type = TLMC_ConnectedProductMovementType(c_params.movementType)
        params.unit_type = TLMC_Unit(c_params.unitType)
        params.distance_scale_factor = c_params.distanceScaleFactor
        params.velocity_scale_factor = c_params.velocityScaleFactor
        params.acceleration_scale_factor = c_params.accelerationScaleFactor
        params.min_position = c_params.minPosition
        params.max_position = c_params.maxPosition
        params.max_velocity = c_params.maxVelocity
        params.max_acceleration = c_params.maxAcceleration

        return params
    
    @staticmethod
    def current_loop_params(c_params:  C_TLMC_CurrentLoopParams) -> TLMC_CurrentLoopParams:

        params = TLMC_CurrentLoopParams()
        params.phase = TLMC_CurrentLoopPhase(c_params.phase)
        params.proportional = c_params.proportional
        params.integral_limit = c_params.integralLimit
        params.integral_dead_band = c_params.integralDeadBand
        params.feed_forward = c_params.feedForward

        return params
    
    @staticmethod
    def dc_pid_params(c_params: C_TLMC_DcPidParams) -> TLMC_DcPidParams:

        params = TLMC_DcPidParams()
        params.proportional = c_params.proportional
        params.integral = c_params.integral
        params.derivative = c_params.derivative
        params.integral_limit = c_params.integralLimit
        params.filter_control = c_params.filterControl

        return params
    
    @staticmethod
    def device_info(c_params: C_TLMC_DeviceInfo) -> TLMC_DeviceInfo:

        params = TLMC_DeviceInfo()
        params.device_family = TLMC_DeviceFamily(c_params.deviceFamily)
        params.device_type = TLMC_DeviceType(c_params.deviceType)
        params.part_number = MapNativeToPython.string(c_params.partNumber)
        params.device = MapNativeToPython.string(c_params.device)
        params.transport = MapNativeToPython.string(c_params.transport)
        params.parent_device = MapNativeToPython.string(c_params.parentDevice)
        params.device_type_description = MapNativeToPython.string(c_params.deviceTypeDescription)

        return params
    
    @staticmethod
    def firmware_version(c_params: C_TLMC_FirmwareVersion) -> TLMC_FirmwareVersion:

        params = TLMC_FirmwareVersion()

        params.major_version = c_params.majorVersion
        params.interim_version = c_params.interimVersion
        params.minor_version = c_params.minorVersion

        return params
    
    @staticmethod
    def general_move_params(c_params: C_TLMC_GeneralMoveParams) -> TLMC_GeneralMoveParams:

        params = TLMC_GeneralMoveParams()
        params.backlash_distance = c_params.backlashDistance

        return params
    
    @staticmethod
    def hardware_info(c_params: C_TLMC_HardwareInfo) -> TLMC_HardwareInfo:

        params = TLMC_HardwareInfo()
        params.serial_number = c_params.serialNumber
        params.part_number = MapNativeToPython.string(c_params.partNumber)
        params.type = c_params.type
        params.firmware_version = MapNativeToPython.firmware_version(c_params.firmwareVersion)
        params.notes = MapNativeToPython.string(c_params.notes)
        params.device_dependent_data = MapNativeToPython.string(c_params.deviceDependantData)
        params.hardware_version = c_params.hardwareVersion
        params.modification_state = c_params.modificationState
        params.number_of_channels = c_params.numChannels

        return params

    @staticmethod
    def home_params(c_params: C_TLMC_HomeParams) -> TLMC_HomeParams:

        params = TLMC_HomeParams()
        params.direction = TLMC_HomeDirection(c_params.direction)
        params.limit_switch = TLMC_HomeLimitSwitch(c_params.limitSwitch)
        params.offset_distance = c_params.offsetDistance
        params.velocity = c_params.velocity

        return params
    
    @staticmethod
    def io_configuration_params(c_params: C_TLMC_IoConfigurationParams) -> TLMC_IoConfigurationParams:

        params = TLMC_IoConfigurationParams()
        params.mode = TLMC_IoPortMode(c_params.mode)
        params.trigger_out_source = TLMC_IoPortSource(c_params.triggerOutSource)

        return params
    
    @staticmethod
    def io_trigger_params(c_params: C_TLMC_IoTriggerParams) -> TLMC_IoTriggerParams:

        params = TLMC_IoTriggerParams()
        params.trigger_in_mode = c_params.triggerInMode
        params.trigger_in_polarity = c_params.triggerInPolarity
        params.trigger_in_source = c_params.triggerInSource
        params.trigger_out_mode = c_params.triggerOutMode
        params.trigger_out_polarity = c_params.triggerOutPolarity
        params.trigger_out_forward_start_position = c_params.triggerOutForwardStartPosition
        params.trigger_out_forward_interval = c_params.triggerOutForwardInterval
        params.trigger_out_forward_number_of_pulses = c_params.triggerOutForwardNumberOfPulses
        params.trigger_out_reverse_start_position = c_params.triggerOutReverseStartPosition
        params.trigger_out_reverse_interval = c_params.triggerOutReverseInterval
        params.trigger_out_reverse_number_of_pulses = c_params.triggerOutReverseNumberOfPulses
        params.trigger_out_pulse_width = c_params.triggerOutPulseWidth
        params.trigger_out_number_of_cycles = c_params.triggerOutNumberOfCycles

        return params
    
    @staticmethod
    def jog_params(c_params: C_TLMC_JogParams) -> TLMC_JogParams:

        params = TLMC_JogParams()
        params.acceleration = c_params.acceleration
        params.max_velocity = c_params.maxVelocity
        params.min_velocity = c_params.minVelocity
        params.mode = TLMC_JogMode(c_params.mode)
        params.step_size = c_params.stepSize
        params.stop_mode = TLMC_JogStopMode(c_params.stopMode)

        return params
    
    @staticmethod
    def joystick_params(c_params: C_TLMC_JoystickParams) -> TLMC_JoystickParams:

        params = TLMC_JoystickParams()
        params.direction_sense = TLMC_JoystickDirectionSense(c_params.directionSense)
        params.high_gear_acceleration = c_params.highGearAcceleration
        params.high_gear_max_velocity = c_params.highGearMaxVelocity
        params.low_gear_acceleration = c_params.lowGearAcceleration
        params.low_gear_max_velocity = c_params.lowGearMaxVelocity

        return params
    
    @staticmethod
    def joystick_settings_params(c_params: C_TLMC_JoystickSettingsParams) -> TLMC_JoystickSettingsParams:

        params = TLMC_JoystickSettingsParams()
        params.joystick_serial_interface = TLMC_JoystickSerialInterface(c_params.joystickSerialInterface)
        params.joystick_model = TLMC_JoystickModel(c_params.joystickModel)
        params.direction_sense = (
            TLMC_JoystickDirectionSense(int(c_params.directionSense[0])),
            TLMC_JoystickDirectionSense(int(c_params.directionSense[1])),
            TLMC_JoystickDirectionSense(int(c_params.directionSense[2])),
        )
        params.axis_mapping = (
            TLMC_JoystickAxis(int(c_params.axisMapping[0])),
            TLMC_JoystickAxis(int(c_params.axisMapping[1])),
            TLMC_JoystickAxis(int(c_params.axisMapping[2])),
        )

        return params
    
    @staticmethod
    def kcube_io_trigger_params(c_params: C_TLMC_KcubeIoTriggerParams) -> TLMC_KcubeIoTriggerParams:

        params = TLMC_KcubeIoTriggerParams()
        params.trigger_1_mode = TLMC_KcubeIoTriggerMode(c_params.trigger1Mode)
        params.trigger_1_polarity = TLMC_KcubeIoTriggerPolarity(c_params.trigger1Polarity)
        params.trigger_2_mode = TLMC_KcubeIoTriggerMode(c_params.trigger2Mode)
        params.trigger_2_polarity = TLMC_KcubeIoTriggerPolarity(c_params.trigger2Polarity)

        return params
    
    @staticmethod
    def kcube_mmi_params(c_params: C_TLMC_KcubeMmiParams) -> TLMC_KcubeMmiParams:

        params = TLMC_KcubeMmiParams()
        params.display_brightness = c_params.displayBrightness
        params.display_dim_level = c_params.displayDimLevel
        params.display_timeout = c_params.displayTimeout
        params.joystick_acceleration = c_params.joystickAcceleration
        params.joystick_direction_sense = TLMC_KcubeMmi_JoystickDirectionSense(c_params.joystickDirectionSense)
        params.joystick_max_velocity = c_params.joystickMaxVelocity
        params.joystick_mode = c_params.joystickMode
        params.joystick_sensitivity = c_params.joystickSensitivity
        params.preset_position_1 = c_params.presetPosition1
        params.preset_position_2 = c_params.presetPosition2
        params.preset_position_3 = c_params.presetPosition3
        
        return params

    @staticmethod
    def kcube_position_trigger_params(c_params: C_TLMC_KcubePositionTriggerParams) -> TLMC_KcubePositionTriggerParams:
        
        params = TLMC_KcubePositionTriggerParams()
        params.forward_interval = c_params.forwardInterval
        params.forward_number_of_pulses = c_params.forwardNumberOfPulses
        params.forward_start_position = c_params.forwardStartPosition
        params.number_of_cycles = c_params.numberOfCycles
        params.pulse_width = c_params.pulseWidth
        params.reverse_interval = c_params.reverseInterval
        params.reverse_number_of_pulses = c_params.reverseNumberOfPulses
        params.reverse_start_position = c_params.reverseStartPosition

        return params
        
    @staticmethod
    def lcd_display_params(c_params: C_TLMC_LcdDisplayParams) -> TLMC_LcdDisplayParams:

        params = TLMC_LcdDisplayParams()
        params.display_brightness = c_params.displayBrightness
        params.display_dim_level = c_params.displayDimLevel
        params.display_timeout = c_params.displayTimeout
        params.knob_sensitivity = c_params.knobSensitivity

        return params
    
    @staticmethod
    def lcd_move_params(c_params: C_TLMC_LcdMoveParams) -> TLMC_LcdMoveParams:

        params = TLMC_LcdMoveParams()
        params.knob_mode = c_params.knobMode
        params.jog_step_size = c_params.jogStepSize
        params.acceleration = c_params.acceleration
        params.max_velocity = c_params.maxVelocity
        params.preset_position = c_params.presetPosition

        return params
    
    @staticmethod
    def limit_switch_params(c_params: C_TLMC_LimitSwitchParams) -> TLMC_LimitSwitchParams:

        params = TLMC_LimitSwitchParams()
        params.clockwise_limit_mode = TLMC_HardLimitOperatingMode(c_params.clockwiseHardLimitOperatingMode)
        params.counterclockwise_limit_mode = TLMC_HardLimitOperatingMode(c_params.counterclockwiseHardLimitOperatingMode)
        params.clockwise_soft_limit = c_params.clockwiseSoftLimit
        params.counterclockwise_soft_limit = c_params.counterclockwiseSoftLimit
        params.soft_limit_operating_mode = TLMC_SoftLimitOperatingMode(c_params.softLimitOperatingMode)

        return params
    
    @staticmethod
    def monitor_output_params(c_params: C_TLMC_MonitorOutputParams) -> TLMC_MonitorOutputParams:

        params = TLMC_MonitorOutputParams()
        params.monitor_output = TLMC_MonitorOutput(c_params.monitorOutput)
        params.dac = c_params.dac

        return params

    @staticmethod
    def motor_output_params(c_params: C_TLMC_MotorOutputParams) -> TLMC_MotorOutputParams:

        params = TLMC_MotorOutputParams()
        params.continuous_current_limit = c_params.continuousCurrentLimit
        params.energy_limit = c_params.energyLimit
        params.motor_bias = c_params.motorBias
        params.motor_limit = c_params.motorLimit

        return params
    
    @staticmethod
    def move_absolute_params(c_params: C_TLMC_MoveAbsoluteParams) -> TLMC_MoveAbsoluteParams:

        params = TLMC_MoveAbsoluteParams()
        params.absolute_position = c_params.absolutePosition

        return params
    
    @staticmethod
    def move_relative_params(c_params: C_TLMC_MoveRelativeParams) -> TLMC_MoveRelativeParams:
        
        params = TLMC_MoveRelativeParams()
        params.relative_distance = c_params.relativeDistance

        return params
    
    @staticmethod
    def position_loop_params(c_params: C_TLMC_PositionLoopParams) -> TLMC_PositionLoopParams:

        params = TLMC_PositionLoopParams()
        params.acceleration_feed_forward = c_params.accelerationFeedForward
        params.derivative = c_params.derivative
        params.error_limit = c_params.errorLimit
        params.integral = c_params.integral
        params.integral_limit = c_params.integralLimit
        params.proportional = c_params.proportional
        params.scale = c_params.scale
        params.servo_cycles = c_params.servoCycles
        params.velocity_feed_forward = c_params.velocityFeedForward

        return params
        
    @staticmethod
    def potentiometer_params(c_params: C_TLMC_PotentiometerParams) -> TLMC_PotentiometerParams:

        params = TLMC_PotentiometerParams()
        params.deflection_0 = c_params.deflection0
        params.velocity_1 = c_params.velocity1
        params.deflection_1 = c_params.deflection1
        params.velocity_2 = c_params.velocity2
        params.deflection_2 = c_params.deflection2
        params.velocity_3 = c_params.velocity3
        params.deflection_3 = c_params.deflection3
        params.velocity_4 = c_params.velocity4

        return params

    @staticmethod
    def power_params(c_params: C_TLMC_PowerParams) -> TLMC_PowerParams:

        params = TLMC_PowerParams()
        params.move_factor = c_params.moveFactor
        params.rest_factor = c_params.restFactor

        return params
    
    @staticmethod
    def profile_mode_params(c_params: C_TLMC_ProfileModeParams) -> TLMC_ProfileModeParams:

        params = TLMC_ProfileModeParams()
        params.mode = c_params.mode
        params.jerk = c_params.jerk

        return params

    @staticmethod
    def pz_io_trigger_params(c_params: C_TLMC_PZ_IoTriggerParams) -> TLMC_PZ_IoTriggerParams:

        params = TLMC_PZ_IoTriggerParams()
        params.number_of_ports_per_channel = c_params.numberOfPortsPerChannel
        params.port_number = TLMC_IoTriggerPortNumber(c_params.portNumber)
        params.port_type = TLMC_PortType(c_params.portType)
        params.mode = TLMC_PZ_IoTriggerMode(c_params.mode)
        params.polarity = TLMC_IoTriggerPolarity(c_params.polarity)
        params.trigger_parameter1 = c_params.triggerParameter1
        params.trigger_parameter2 = c_params.triggerParameter2

        return params

    @staticmethod
    def pz_lnnx_control_loop_params(c_params: C_TLMC_PZ_LnnxControlLoopParams) -> TLMC_PZ_LnnxControlLoopParams:

        params = TLMC_PZ_LnnxControlLoopParams()
        params.override_mode = TLMC_PZ_LnnxControlLoopParamsOverrideMode(c_params.overrideMode)
        params.proportional = c_params.proportional
        params.integral = c_params.integral
        params.derivative = c_params.derivative
        params.feed_forward = c_params.feedForward

        return params 
    
    @staticmethod
    def pz_lnnx_notch_filter_params(c_params: C_TLMC_PZ_LnnxNotchFilterParams) -> TLMC_PZ_LnnxNotchFilterParams:

        params = TLMC_PZ_LnnxNotchFilterParams()
        params.override_mode = TLMC_PZ_LnnxNotchFilterParamsOverrideMode(c_params.overrideMode)
        params.filter1_center_frequency = c_params.filter1CenterFrequency
        params.filter1_quality_factor = c_params.filter1QualityFactor
        params.filter2_center_frequency = c_params.filter2CenterFrequency
        params.filter2_quality_factor = c_params.filter2QualityFactor

        return params

    @staticmethod
    def pz_kpc_io_settings_params(c_params: C_TLMC_PZ_KpcIoSettingsParams) -> TLMC_PZ_KpcIoSettingsParams:

        params = TLMC_PZ_KpcIoSettingsParams()
        params.voltage_limit = c_params.voltageLimit
        params.analog_input_source = TLMC_PZ_KpcAnalogInputSource(c_params.analogInputSource)
        params.filter_cut_off_frequency = c_params.filterCutOffFrequency
        params.voltage_range = TLMC_PZ_KpcVoltageRange(c_params.voltageRange)
        params.force_sense = c_params.forceSense
        params.strain_gauge_option = TLMC_PZ_KpcStrainGaugeOption(c_params.strainGaugeOption)

        return params
    
    @staticmethod
    def pz_kpc_io_trigger_params(c_params: C_TLMC_PZ_KpcIoTriggerParams) -> TLMC_PZ_KpcIoTriggerParams:

        params = TLMC_PZ_KpcIoTriggerParams()
        params.trigger_1_mode = TLMC_PZ_KpcIoTriggerMode(c_params.trigger1Mode)
        params.trigger_1_polarity = TLMC_KcubeIoTriggerPolarity(c_params.trigger1Polarity)
        params.trigger_2_mode = TLMC_PZ_KpcIoTriggerMode(c_params.trigger2Mode)
        params.trigger_2_polarity = TLMC_KcubeIoTriggerPolarity(c_params.trigger2Polarity)
        params.strain_gauge_lower_limit = c_params.strainGaugeLowerLimit
        params.strain_gauge_upper_limit = c_params.strainGaugeUpperLimit
        params.smoothing_samples = c_params.smoothingSamples
        params.monitor_output_mode = TLMC_PZ_KpcMonitorOutputMode(c_params.monitorOutputMode)
        params.monitor_filter_cut_off_frequency = c_params.monitorFilterCutOffFrequency
        params.monitor_output_software_value = c_params.monitorOutputSoftwareValue

        return params
    
    @staticmethod
    def pz_kpc_mmi_params(c_params: C_TLMC_PZ_KpcMmiParams) -> TLMC_PZ_KpcMmiParams:

        params = TLMC_PZ_KpcMmiParams()
        params.display_brightness = c_params.displayBrightness
        params.display_dim_level = c_params.displayDimLevel
        params.display_timeout = c_params.displayTimeout
        params.joystick_direction_sense = TLMC_PZ_KpcMmi_JoystickDirectionSense(c_params.joystickDirectionSense)
        params.joystick_gear = TLMC_KcubeMmi_JoystickGear(c_params.joystickGear)
        params.joystick_mode = TLMC_PZ_KpcMmi_JoystickMode(c_params.joystickMode)
        params.joystick_position_step_size = c_params.joystickPositionStepSize
        params.joystick_voltage_step_size = c_params.joystickVoltageStepSize
        params.preset_position_1 = c_params.presetPosition1
        params.preset_position_2 = c_params.presetPosition2
        params.preset_voltage_1 = c_params.presetVoltage1
        params.preset_voltage_2 = c_params.presetVoltage2
        
        return params
    
    @staticmethod
    def pz_max_output_voltage_params(c_params: C_TLMC_PZ_MaxOutputVoltageParams) -> TLMC_PZ_MaxOutputVoltageParams:

        params = TLMC_PZ_MaxOutputVoltageParams()
        params.max_output_voltage = c_params.maxOutputVoltage
        params.voltage_limit = TLMC_PZ_VoltageLimit(c_params.voltageLimit)

        return params
    
    @staticmethod
    def pz_nano_trak_circle_diameter_lookup_table_data(c_params: C_TLMC_PZ_NanoTrakCircleDiameterLookupTableData) -> TLMC_PZ_NanoTrakCircleDiameterLookupTableData:

        params = TLMC_PZ_NanoTrakCircleDiameterLookupTableData()
        params.lookup_table_values = [int(v) for v in c_params.lookupTableValues]

        return params

    @staticmethod
    def pz_nano_trak_circle_home_position_params(c_params: C_TLMC_PZ_NanoTrakCircleHomePositionParams) -> TLMC_PZ_NanoTrakCircleHomePositionParams:

        params = TLMC_PZ_NanoTrakCircleHomePositionParams()
        params.circle_home_position_a = c_params.circleHomePositionA
        params.circle_home_position_b = c_params.circleHomePositionB

        return params
    
    @staticmethod
    def pz_nano_trak_circle_params(c_params: C_TLMC_PZ_NanoTrakCircleParams) -> TLMC_PZ_NanoTrakCircleParams:

        params = TLMC_PZ_NanoTrakCircleParams()
        params.absolute_power_adjust_type = TLMC_PZ_NanoTrakAbsolutePowerAdjustType(c_params.absolutePowerAdjustType)
        params.absolute_power_max_circle_diameter = c_params.absolutePowerMaxCircleDiameter
        params.absolute_power_min_circle_diameter = c_params.absolutePowerMinCircleDiameter
        params.circle_diameter_mode = TLMC_PZ_NanoTrakCircleDiameterMode(c_params.circleDiameterMode)
        params.circle_oscillation_frequency = c_params.circleOscillationFrequency
        params.circle_diameter_software = c_params.circleDiameterSoftware

        return params
    
    @staticmethod
    def pz_nano_trak_gain_params(c_params: C_TLMC_PZ_NanoTrakGainParams) -> TLMC_PZ_NanoTrakGainParams:

        params = TLMC_PZ_NanoTrakGainParams()
        params.gain = c_params.gain
        params.gain_control_mode = TLMC_PZ_NanoTrakGainControlMode(c_params.gainControlMode)

        return params
    
    @staticmethod
    def pz_nano_trak_mode(c_params: C_TLMC_PZ_NanoTrakMode) -> TLMC_PZ_NanoTrakMode:

        params = TLMC_PZ_NanoTrakMode()
        params.mode = TLMC_PZ_NanoTrakTrackingMode(c_params.mode)
        params.state = TLMC_PZ_NanoTrakTrackingState(c_params.state)

        return params
    
    @staticmethod
    def pz_nano_trak_phase_compensation_params(c_params: C_TLMC_PZ_NanoTrakPhaseCompensationParams) -> TLMC_PZ_NanoTrakPhaseCompensationParams:

        params = TLMC_PZ_NanoTrakPhaseCompensationParams()
        params.phase_compensation_a_software = c_params.phaseCompensationASoftware
        params.phase_compensation_b_software = c_params.phaseCompensationBSoftware
        params.phase_compensation_mode = TLMC_PZ_NanoTrakPhaseCompensationMode(c_params.phaseCompensationMode)

        return params
    
    @staticmethod
    def pz_nano_trak_range_params(c_params: C_TLMC_PZ_NanoTrakRangeParams) -> TLMC_PZ_NanoTrakRangeParams:

        params = TLMC_PZ_NanoTrakRangeParams()
        params.range_change_type = TLMC_PZ_NanoTrakRangeChangeType(c_params.rangeChangeType)
        params.range_down_limit = c_params.rangeDownLimit
        params.range_mode = TLMC_PZ_NanoTrakRangeMode(c_params.rangeMode)
        params.range_type = TLMC_PZ_NanoTrakRange(c_params.rangeType)
        params.range_up_limit = c_params.rangeUpLimit
        params.settle_samples = c_params.settleSamples

        return params

    @staticmethod
    def pz_nano_trak_status(c_params: C_TLMC_PZ_NanoTrakStatus) -> TLMC_PZ_NanoTrakStatus:

        params = TLMC_PZ_NanoTrakStatus()
        params.absolute_reading = c_params.absoluteReading
        params.circle_diameter = c_params.circleDiameter
        params.circle_position_a = c_params.circlePositionA
        params.circle_position_b = c_params.circlePositionB
        params.nano_trak_gain = c_params.nanoTrakGain
        params.phase_compensation_a = c_params.phaseCompensationA
        params.phase_compensation_b = c_params.phaseCompensationB
        params.range = TLMC_PZ_NanoTrakRange(c_params.range)
        params.relative_reading = c_params.relativeReading
        params.status_bits = TLMC_PZ_NanoTrakStatusBit(c_params.statusBits)
        params.under_over_read = TLMC_PZ_NanoTrakUnderOverReadType(c_params.underOverRead)

        return params
    
    @staticmethod
    def pz_nano_trak_tna_io_settings(c_params: C_TLMC_PZ_NanoTrakTnaIoSettings) -> TLMC_PZ_NanoTrakTnaIoSettings:

        params = TLMC_PZ_NanoTrakTnaIoSettings()
        params.channel_1_signal_range_type = TLMC_PZ_TnaIoSignalRangeType(c_params.channel1SignalRangeType)
        params.channel_2_signal_range_type = TLMC_PZ_TnaIoSignalRangeType(c_params.channel2SignalRangeType)
        params.signal_output_mode = TLMC_PZ_TnaIoSignalOutputMode(c_params.signalOutputMode)
        params.signal_source_boost_type = TLMC_PZ_TnaIoSignalSourceBoostType(c_params.signalSourceBoostType)
        params.signal_source_mode = TLMC_PZ_TnaIoSignalSourceMode(c_params.signalSourceMode)

        return params
    
    @staticmethod
    def pz_nano_trak_track_threshold(c_params: C_TLMC_PZ_NanoTrakTrackThresholdParams) -> TLMC_PZ_NanoTrakTrackThresholdParams:

        params = TLMC_PZ_NanoTrakTrackThresholdParams()
        params.track_threshold = c_params.trackThreshold

        return params
    
    @staticmethod
    def pz_output_voltage_control_source_params(c_params: C_TLMC_PZ_OutputVoltageControlSourceParams) -> TLMC_PZ_OutputVoltageControlSourceParams:

        params = TLMC_PZ_OutputVoltageControlSourceParams()
        params.source = TLMC_PZ_OutputVoltageControlSource(c_params.source)

        return params

    @staticmethod
    def pz_output_waveform_params(c_params: C_TLMC_PZ_OutputWaveformParams) -> TLMC_PZ_OutputWaveformParams:

        params = TLMC_PZ_OutputWaveformParams()
        params.inter_sample_delay = c_params.interSampleDelay
        params.mode = TLMC_PZ_OutputWaveformOperatingMode(c_params.mode)
        params.number_of_cycles = c_params.numberOfCycles
        params.number_of_samples_between_trigger_repetition = c_params.numberOfSamplesBetweenTriggerRepetition
        params.number_of_samples_per_cycle = c_params.numberOfSamplesPerCycle
        params.output_trigger_start_index = c_params.outputTriggerStartIndex
        params.output_trigger_width = c_params.outputTriggerWidth
        params.post_cycle_delay = c_params.postCycleDelay
        params.pre_cycle_delay = c_params.preCycleDelay

        return params
    
    @staticmethod
    def pz_position_loop_params(c_params: C_TLMC_PZ_PositionLoopParams) -> TLMC_PZ_PositionLoopParams:

        params = TLMC_PZ_PositionLoopParams()
        params.integral = c_params.integral
        params.proportional = c_params.proportional

        return params
    
    @staticmethod
    def pz_slew_rate_params(c_params: C_TLMC_PZ_SlewRateParams) -> TLMC_PZ_SlewRateParams:

        params = TLMC_PZ_SlewRateParams()
        params.closed_loop_slew_rate = c_params.closedLoopSlewRate
        params.open_slew_rate = c_params.openSlewRate

        return params
    
    @staticmethod
    def pz_stage_info_params(c_params: C_TLMC_PZ_StageInfoParams) -> TLMC_PZ_StageInfoParams:

        params = TLMC_PZ_StageInfoParams()
        params.product_id = TLMC_PZ_StageProductId(c_params.productId)
        params.stage_name = MapNativeToPython.string(c_params.stageName)
        params.serial_number = c_params.serialNumber
        params.max_voltage = c_params.maxVoltage
        params.min_negative_voltage = c_params.minNegativeVoltage
        params.sensor_type = TLMC_PZ_SensorType(c_params.sensorType)
        params.axis_type = TLMC_ConnectedProductAxisType(c_params.axisType)
        params.nominal_travel = c_params.nominalTravel
        params.home_position = c_params.homePosition

        return params

    @staticmethod
    def pz_status(c_params: C_TLMC_PZ_Status) -> TLMC_PZ_Status:

        params = TLMC_PZ_Status()
        params.output_voltage = c_params.outputVoltage
        params.position = c_params.position
        params.status_bits = TLMC_PZ_StatusBit(c_params.statusBits)

        return params

    @staticmethod
    def rich_response(c_params: C_TLMC_RichResponse) -> TLMC_RichResponse:
        
        params = TLMC_RichResponse()
        params.code = c_params.code
        params.message_id = c_params.messageId
        params.notes = c_params.notes

        return params
    
   
    @staticmethod
    def setting(c_params: C_TLMC_Setting) -> TLMC_Setting:

        params = TLMC_Setting()
        params.display_name = MapNativeToPython.string(c_params.DisplayName)
        params.has_discrete_values = c_params.hasDiscreteValues
        params.has_max = c_params.hasMax
        params.has_min = c_params.hasMin
        params.is_read_only = c_params.isReadOnly
        params.is_value_set = c_params.isValueSet
        params.name = MapNativeToPython.string(c_params.Name)
        params.scale_type = TLMC_ScaleType(c_params.ScaleType)
        params.unit_type = TLMC_Unit(c_params.UnitType)        
        params.value_type = TLMC_ValueType(c_params.valueType)
        params.is_value_set = c_params.isValueSet
        
        if params.value_type == TLMC_ValueType.TLMC_ValueType_int64:
            params.value = int(c_params.Value.int64Value)
            if params.has_min == True:
                params.min_value = int(c_params.minValue.int64Value)
            if params.has_max == True:
                params.max_value = int(c_params.maxValue.int64Value)
        elif params.value_type == TLMC_ValueType.TLMC_ValueType_float:
            params.value = float(c_params.Value.floatValue)
            if params.has_min == True:
                params.min_value = int(c_params.minValue.floatValue)
            if params.has_max == True:
                params.max_value = int(c_params.maxValue.floatValue)
        elif params.value_type == TLMC_ValueType.TLMC_ValueType_bool:
            params.value = bool(c_params.Value.boolValue)
        elif params.value_type == TLMC_ValueType.TLMC_ValueType_string:
            params.value = MapNativeToPython.string(c_params.Value.string)

        return params
    
    @staticmethod
    def status_item(c_params: C_TLMC_StatusItem) -> TLMC_StatusItem:

        params = TLMC_StatusItem()
        params.id = TLMC_StatusItemId(c_params.id)
        params.value_type = TLMC_ValueType(c_params.valueType)

        if params.value_type == TLMC_ValueType.TLMC_ValueType_int64:
            params.value = int(c_params.value.int64Value)
        elif params.value_type == TLMC_ValueType.TLMC_ValueType_float:
            params.value = float(c_params.value.floatValue)
        elif params.value_type == TLMC_ValueType.TLMC_ValueType_bool:
            params.value = bool(c_params.value.boolValue)
        elif params.value_type == TLMC_ValueType.TLMC_ValueType_string:
            params.value = MapNativeToPython.string(c_params.value.string)

        return params
    
    @staticmethod
    def stage_axis_params(c_params: C_TLMC_StageAxisParams) -> TLMC_StageAxisParams:

        params = TLMC_StageAxisParams()
        params.axis_id = TLMC_StageAxis_AxisId(c_params.axisId)
        params.counts_per_unit = c_params.countsPerUnit
        params.gear_box_ratio = c_params.gearBoxRatio
        params.max_acceleration = c_params.maxAcceleration
        params.max_deceleration = c_params.maxDeceleation
        params.min_position = c_params.minPosition
        params.max_position = c_params.maxPosition
        params.max_velocity = c_params.maxVelocity
        params.part_number = MapNativeToPython.string(c_params.partNumber)
        params.serial_number = c_params.serialNumber
        params.type_id = TLMC_StageAxis_TypeId(c_params.typeId)

        return params
    
    @staticmethod
    def stepper_loop_params(c_params: C_TLMC_StepperLoopParams) -> TLMC_StepperLoopParams:

        params = TLMC_StepperLoopParams()
        params.differential = c_params.differential
        params.integral = c_params.integral
        params.loop_mode = TLMC_StepperLoopParams_LoopMode(c_params.loopMode)
        params.output_tolerance = c_params.outputTolerance
        params.proportional = c_params.proportional
        params.microsteps_per_encoder_count = c_params.microstepsPerEncoderCount

        return params
    
    @staticmethod
    def stepper_status(c_params: C_TLMC_StepperStatus) -> TLMC_StepperStatus:

        params = TLMC_StepperStatus()
        params.position = c_params.position
        params.encoder_count = c_params.encoderCount
        params.status_bits = TLMC_UniversalStatusBit(c_params.statusBits)

        return params
    
    @staticmethod
    def track_settle_params(c_params: C_TLMC_TrackSettleParams) -> TLMC_TrackSettleParams:

        params = TLMC_TrackSettleParams()
        params.settle_time = c_params.settleTime
        params.settle_window = c_params.settleWindow
        params.track_window = c_params.trackWindow

        return params
    
    @staticmethod
    def trigger_params_for_dc_brushless(c_params: C_TLMC_TriggerParamsForDcBrushless) -> TLMC_TriggerParamsForDcBrushless:

        params = TLMC_TriggerParamsForDcBrushless()
        params.modes = TLMC_TriggerModesForDcBrushless(c_params.modes)

        return params
    
    @staticmethod
    def trigger_params_for_stepper(c_params: C_TLMC_TriggerParamsForStepper) -> TLMC_TriggerParamsForStepper:

        params = TLMC_TriggerParamsForStepper()
        params.modes = TLMC_TriggerModesForStepper(c_params.modes)

        return params
    
    @staticmethod
    def universal_status(c_params: C_TLMC_UniversalStatus) -> TLMC_UniversalStatus:
        
        params = TLMC_UniversalStatus()
        params.motor_current = c_params.motorCurrent
        params.position = c_params.position
        params.status_bits = TLMC_UniversalStatusBit(c_params.statusBits)
        params.velocity = c_params.velocity

        return params
    
    @staticmethod
    def velocity_params(c_params: C_TLMC_VelocityParams) -> TLMC_VelocityParams:

        params = TLMC_VelocityParams()
        params.acceleration = c_params.acceleration
        params.max_velocity = c_params.maxVelocity
        params.min_velocity = c_params.minVelocity

        return params