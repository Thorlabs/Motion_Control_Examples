from typing import Sequence

from thorlabs_xa.shared.enums import TLMC_AnalogMonitorMotorChannel, TLMC_AnalogMonitorSystemVariable, TLMC_ButtonMode, TLMC_ConnectedProductAxisType, TLMC_ConnectedProductMovementType, TLMC_CurrentLoopPhase, TLMC_DeviceFamily, TLMC_DeviceType, TLMC_HardLimitOperatingMode, TLMC_HomeDirection, TLMC_HomeLimitSwitch, TLMC_IoPortMode, TLMC_IoPortSource, TLMC_IoTriggerPolarity, TLMC_IoTriggerPortNumber, TLMC_JogMode, TLMC_JogStopMode, TLMC_JoystickAxis, TLMC_JoystickDirectionSense, TLMC_JoystickModel, TLMC_JoystickSerialInterface, TLMC_KcubeIoTriggerMode, TLMC_KcubeIoTriggerPolarity, TLMC_KcubeMmi_JoystickDirectionSense, TLMC_KcubeMmi_JoystickGear, TLMC_KcubeMmi_JoystickMode, TLMC_MonitorOutput, TLMC_PZ_IoTriggerMode, TLMC_PZ_KpcAnalogInputSource, TLMC_PZ_KpcIoTriggerMode, TLMC_PZ_KpcMmi_JoystickDirectionSense, TLMC_PZ_KpcMmi_JoystickMode, TLMC_PZ_KpcMonitorOutputMode, TLMC_PZ_KpcStrainGaugeOption, TLMC_PZ_KpcVoltageRange, TLMC_PZ_LnnxControlLoopParamsOverrideMode, TLMC_PZ_LnnxNotchFilterParamsOverrideMode, TLMC_PZ_NanoTrakAbsolutePowerAdjustType, TLMC_PZ_NanoTrakCircleDiameterMode, TLMC_PZ_NanoTrakGainControlMode, TLMC_PZ_NanoTrakPhaseCompensationMode, TLMC_PZ_NanoTrakRange, TLMC_PZ_NanoTrakRangeChangeType, TLMC_PZ_NanoTrakRangeMode, TLMC_PZ_NanoTrakStatusBit, TLMC_PZ_NanoTrakTrackingMode, TLMC_PZ_NanoTrakTrackingState, TLMC_PZ_NanoTrakUnderOverReadType, TLMC_PZ_OutputVoltageControlSource, TLMC_PZ_OutputWaveformOperatingMode, TLMC_PZ_SensorType, TLMC_PZ_StageProductId, TLMC_PZ_StatusBit, TLMC_PZ_TnaIoOutRangeType, TLMC_PZ_TnaIoOutRouteType, TLMC_PZ_TnaIoSignalOutputMode, TLMC_PZ_TnaIoSignalRangeType, TLMC_PZ_TnaIoSignalSourceBoostType, TLMC_PZ_TnaIoSignalSourceMode, TLMC_PZ_VoltageLimit, TLMC_PortType, TLMC_ProfileMode, TLMC_SoftLimitOperatingMode, TLMC_StageAxis_AxisId, TLMC_StageAxis_TypeId, TLMC_StatusItemId, TLMC_StepperLoopParams_LoopMode, TLMC_TriggerModesForDcBrushless, TLMC_TriggerModesForStepper, TLMC_Unit, TLMC_UniversalStatusBit, TLMC_ValueType
    
class TLMC_AnalogMonitorConfigurationParams():
    def __init__(self):
        self._motor_channel = TLMC_AnalogMonitorMotorChannel.TLMC_AnalogMonitorMotorChannel_1
        self._system_variable = TLMC_AnalogMonitorSystemVariable.TLMC_AnalogMonitorSystemVariable_PositionError
        self._scale = 0
        self._offset = 0

    @property
    def motor_channel(self) -> TLMC_AnalogMonitorMotorChannel:
        return self._motor_channel

    @motor_channel.setter
    def motor_channel(self, val: TLMC_AnalogMonitorMotorChannel):
        self._motor_channel = val

    @property
    def system_variable(self) -> TLMC_AnalogMonitorSystemVariable:
        return self._system_variable

    @system_variable.setter
    def system_variable(self, val: TLMC_AnalogMonitorSystemVariable):
        self._system_variable = val

    @property
    def scale(self) -> int:
        return self._scale

    @scale.setter
    def scale(self, val: int):
        self._scale = val

    @property
    def offset(self) -> int:
        return self._offset

    @offset.setter
    def offset(self, val: int):
        self._offset = val


class TLMC_ApiVersion():
    def __init__(self):
        self._major = 0
        self._minor = 0
        self._patch = 0
        self._build = 0
        self._prerelease_label = ""
        self._display_string = ""

    @property
    def major(self) -> int:
        return self._major
    
    @major.setter
    def major(self, val: int):
        self._major = val

    @property
    def minor(self) -> int:
        return self._minor
    
    @minor.setter
    def minor(self, val: int):
        self._minor = val

    @property
    def patch(self) -> int:
        return self._patch
    
    @patch.setter
    def patch(self, val: int):
        self._patch = val

    @property
    def build(self) -> int:
        return self._build
    
    @build.setter
    def build(self, val: int):
        self._build = val

    @property
    def prerelease_label(self) -> str:
        return self._prerelease_label
    
    @prerelease_label.setter
    def prerelease_label(self, val: str):
        self._prerelease_label = val

    @property
    def display_string(self) -> str:
        return self._display_string
    
    @display_string.setter
    def display_string(self, val: str):
        self._display_string = val


class TLMC_ButtonParams():
    def __init__(self):
        self._button_mode = TLMC_ButtonMode.TLMC_ButtonMode_Jog
        self._position_1 = 0
        self._position_2 = 0
        self._timeout_1_milliseconds = 0
        self._timeout_2_milliseconds = 0

    @property
    def button_mode(self) -> TLMC_ButtonMode:
        return self._button_mode

    @button_mode.setter
    def button_mode(self, val: TLMC_ButtonMode):
        self._button_mode = val

    @property
    def position_1(self) -> int:
        return self._position_1
    
    @position_1.setter
    def position_1(self, val: int):
        self._position_1 = val

    @property
    def position_2(self) -> int:
        return self._position_2
    
    @position_2.setter
    def position_2(self, val: int):
        self._position_2 = val

    @property
    def timeout_1_milliseconds(self) -> int:
        return self._timeout_1_milliseconds
    
    @timeout_1_milliseconds.setter
    def timeout_1_milliseconds(self, val: int):
        self._timeout_1_milliseconds = val

    @property
    def timeout_2_milliseconds(self) -> int:
        return self._timeout_2_milliseconds
    
    @timeout_2_milliseconds.setter
    def timeout_2_milliseconds(self, val: int):
        self._timeout_2_milliseconds = val


class TLMC_ConnectedProductInfo():
    def __init__(self):
        self._product_name = ""
        self._part_number = ""
        self._axis_type = TLMC_ConnectedProductAxisType.TLMC_ConnectedProductAxisType_Unknown
        self._movement_type = TLMC_ConnectedProductMovementType.TLMC_ConnectedProductMovementType_Unknown
        self._unit_type = TLMC_Unit.TLMC_Unit_Unspecified
        self._distance_scale_factor = 0.0
        self._velocity_scale_factor = 0.0
        self._acceleration_scale_factor = 0.0
        self._min_position = 0.0
        self._max_position = 0.0
        self._max_velocity = 0.0
        self._max_acceleration = 0.0

    @property
    def product_name(self) -> str:
        return self._product_name

    @product_name.setter
    def product_name(self, val: str):
        self._product_name = val

    @property
    def part_number(self) -> str:
        return self._part_number
    
    @part_number.setter
    def part_number(self, val: str):
        self._part_number = val

    @property
    def axis_type(self) -> TLMC_ConnectedProductAxisType:
        return self._axis_type

    @axis_type.setter
    def axis_type(self, val: TLMC_ConnectedProductAxisType):
        self._axis_type = val

    @property
    def movement_type(self) -> TLMC_ConnectedProductMovementType:
        return self._movement_type

    @movement_type.setter
    def movement_type(self, val: TLMC_ConnectedProductMovementType):
        self._movement_type = val

    @property
    def unit_type(self) -> TLMC_Unit:
        return self._unit_type

    @unit_type.setter
    def unit_type(self, val: TLMC_Unit):
        self._unit_type = val

    @property
    def distance_scale_factor(self) -> float:
        return self._distance_scale_factor

    @distance_scale_factor.setter
    def distance_scale_factor(self, val: float):
        self._distance_scale_factor = val

    @property
    def velocity_scale_factor(self) -> float:
        return self._velocity_scale_factor

    @velocity_scale_factor.setter
    def velocity_scale_factor(self, val: float):
        self._velocity_scale_factor = val

    @property
    def acceleration_scale_factor(self) -> float:
        return self._acceleration_scale_factor

    @acceleration_scale_factor.setter
    def acceleration_scale_factor(self, val: float):
        self._acceleration_scale_factor = val

    @property
    def min_position(self) -> float:
        return self._min_position

    @min_position.setter
    def min_position(self, val: float):
        self._min_position = val

    @property
    def max_position(self) -> float:
        return self._max_position

    @max_position.setter
    def max_position(self, val: float):
        self._max_position = val

    @property
    def max_velocity(self) -> float:
        return self._max_velocity

    @max_velocity.setter
    def max_velocity(self, val: float):
        self._max_velocity = val

    @property
    def max_acceleration(self) -> float:
        return self._max_acceleration

    @max_acceleration.setter
    def max_acceleration(self, val: float):
        self._max_acceleration = val


class TLMC_TriggerParamsForDcBrushless():
    def __init__(self):
        self._modes = TLMC_TriggerModesForDcBrushless.TLMC_TriggerModesForDcBrushless_InputActiveIsLogicHigh

    @property
    def modes(self) -> TLMC_TriggerModesForDcBrushless:
        return self._modes

    @modes.setter
    def modes(self, val: TLMC_TriggerModesForDcBrushless):
        self._modes = val


class TLMC_DeviceInfo():
    def __init__(self):
        self._device_family = TLMC_DeviceFamily.TLMC_DeviceFamily_ThorlabsMotionControl
        self._device_type = TLMC_DeviceType.TLMC_DeviceType_Bbd30xBaseUnit
        self._part_number = ""
        self._device = ""
        self._transport = ""
        self._parent_device = ""
        self._device_type_description = ""

    @property
    def device_family(self) -> TLMC_DeviceFamily:
        return self._device_family

    @device_family.setter
    def device_family(self, val: TLMC_DeviceFamily):
        self._device_family = val

    @property
    def device_type(self) -> TLMC_DeviceType:
        return self._device_type

    @device_type.setter
    def device_type(self, val: TLMC_DeviceType):
        self._device_type = val

    @property
    def part_number(self) -> str:
        return self._part_number

    @part_number.setter
    def part_number(self, val: str):
        self._part_number = val

    @property
    def device(self) -> str:
        return self._device

    @device.setter
    def device(self, val: str):
        self._device = val

    @property
    def transport(self) -> str:
        return self._transport

    @transport.setter
    def transport(self, val: str):
        self._transport = val

    @property
    def parent_device(self) -> str:
        return self._parent_device

    @parent_device.setter
    def parent_device(self, val: str):
        self._parent_device = val

    @property
    def device_type_description(self) -> str:
        return self._device_type_description
    
    @device_type_description.setter
    def device_type_description(self, val: str):
        self._device_type_description = val


class TLMC_DcPidParams():
    def __init__(self):
        self._proportional = 0
        self._integral = 0
        self._derivative = 0
        self._integralLimit = 0
        self._filterControl = 0

    @property
    def proportional(self) -> int:
        return self._proportional
    
    @proportional.setter
    def proportional(self, value: int):
        self._proportional = value

    @property
    def integral(self) -> int:
        return self._integral
    
    @integral.setter
    def integral(self, value: int):
        self._integral = value

    @property
    def derivative(self) -> int:
        return self._derivative

    @derivative.setter
    def derivative(self, value: int):
        self._derivative = value

    @property
    def integral_limit(self) -> int:
        return self._integralLimit

    @integral_limit.setter
    def integral_limit(self, value: int):
        self._integralLimit = value

    @property
    def filter_control(self) -> int:
        return self._filterControl
      
    @filter_control.setter
    def filter_control(self, value: int):
        self._filterControl = value


class TLMC_FirmwareVersion():
    def __init__(self):
        self._minor_version = 0
        self._interim_version = 0
        self._major_version = 0

    @property
    def minor_version(self) -> int:
        return self._minor_version

    @minor_version.setter
    def minor_version(self, val: int) -> None:
        self._minor_version = val

    @property
    def interim_version(self) -> int:
        return self._interim_version

    @interim_version.setter
    def interim_version(self, val: int) -> None:
        self._interim_version = val

    @property
    def major_version(self) -> int:
        return self._major_version

    @major_version.setter
    def major_version(self, val: int) -> None:
        self._major_version = val

            
class TLMC_GeneralMoveParams():
    def __init__(self):
        self._backlash_distance = 0

    @property
    def backlash_distance(self) -> int:
        return self._backlash_distance

    @backlash_distance.setter
    def backlash_distance(self, val: int):
        self._backlash_distance = val


class TLMC_HardwareInfo():
    def __init__(self):
        self._serial_number = 0
        self._part_number = ""
        self._type = 0
        self._firmware_version = TLMC_FirmwareVersion()
        self._notes = ""
        self._device_dependent_data = ""
        self._hardware_version = 0
        self._modification_state = 0
        self._number_of_channels = 0

    @property
    def serial_number(self) -> int:
        return self._serial_number

    @serial_number.setter
    def serial_number(self, val: int):
        self._serial_number = val

    @property
    def part_number(self) -> str:
        return self._part_number

    @part_number.setter
    def part_number(self, val: str):
        self._part_number = val

    @property
    def type(self) -> int:
        return self._type

    @type.setter
    def type(self, val: int):
        self._type = val

    @property
    def firmware_version(self) -> TLMC_FirmwareVersion:
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, val: TLMC_FirmwareVersion):
        self._firmware_version = val

    @property
    def notes(self) -> str:
        return self._notes

    @notes.setter
    def notes(self, val: str):
        self._notes = val

    @property
    def device_dependent_data(self) -> str:
        return self._device_dependent_data

    @device_dependent_data.setter
    def device_dependent_data(self, val: str):
        self._device_dependent_data = val

    @property
    def hardware_version(self) -> int:
        return self._hardware_version

    @hardware_version.setter
    def hardware_version(self, val: int):
        self._hardware_version = val

    @property
    def modification_state(self) -> int:
        return self._modification_state

    @modification_state.setter
    def modification_state(self, val: int):
        self._modification_state = val

    @property
    def number_of_channels(self) -> int:
        return self._number_of_channels

    @number_of_channels.setter
    def number_of_channels(self, val: int):
        self._number_of_channels = val


class TLMC_HomeParams():
    def __init__(self):
        self._direction = TLMC_HomeDirection.TLMC_HomeDirection_Forward
        self._limit_switch = TLMC_HomeLimitSwitch.TLMC_HomeLimitSwitch_Reverse
        self._offset_distance = 0
        self._velocity = 0

    @property
    def direction(self) -> TLMC_HomeDirection:
        return self._direction

    @direction.setter
    def direction(self, val: TLMC_HomeDirection) -> None:
        self._direction = val

    @property
    def limit_switch(self) -> TLMC_HomeLimitSwitch:
        return self._limit_switch

    @limit_switch.setter
    def limit_switch(self, val: TLMC_HomeLimitSwitch) -> None:
        self._limit_switch = val

    @property
    def offset_distance(self) -> int:
        return self._offset_distance

    @offset_distance.setter
    def offset_distance(self, val: int) -> None:
        self._offset_distance = val

    @property
    def velocity(self) -> int:
        return self._velocity

    @velocity.setter
    def velocity(self, val: int) -> None:
        self._velocity = val


class TLMC_IoConfigurationParams():
    def __init__(self):
        self._mode = TLMC_IoPortMode.TLMC_IoPortMode_DigitalInput
        self._trigger_out_source = TLMC_IoPortSource.TLMC_IoPortSource_Software

    @property
    def mode(self) -> TLMC_IoPortMode:
        return self._mode

    @mode.setter
    def mode(self, val: TLMC_IoPortMode) -> None:
        self._mode = val

    @property
    def trigger_out_source(self) -> TLMC_IoPortSource:
        return self._trigger_out_source

    @trigger_out_source.setter
    def trigger_out_source(self, val: TLMC_IoPortSource) -> None:
        self._trigger_out_source = val


class TLMC_IoTriggerParams():
    def __init__(self):
        self._trigger_in_mode = 0
        self._trigger_in_polarity = 0
        self._trigger_in_source = 0
        self._trigger_out_mode = 0
        self._trigger_out_polarity = 0
        self._trigger_out_forward_start_position = 0
        self._trigger_out_forward_interval = 0
        self._trigger_out_forward_number_of_pulses = 0
        self._trigger_out_reverse_start_position = 0
        self._trigger_out_reverse_interval = 0
        self._trigger_out_reverse_number_of_pulses = 0
        self._trigger_out_pulse_width = 0
        self._trigger_out_number_of_cycles = 0

    @property
    def trigger_in_mode(self) -> int:
        return self._trigger_in_mode

    @trigger_in_mode.setter
    def trigger_in_mode(self, val: int):
        self._trigger_in_mode = val

    @property
    def trigger_in_polarity(self) -> int:
        return self._trigger_in_polarity

    @trigger_in_polarity.setter
    def trigger_in_polarity(self, val: int):
        self._trigger_in_polarity = val

    @property
    def trigger_in_source(self) -> int:
        return self._trigger_in_source

    @trigger_in_source.setter
    def trigger_in_source(self, val: int):
        self._trigger_in_source = val

    @property
    def trigger_out_mode(self) -> int:
        return self._trigger_out_mode

    @trigger_out_mode.setter
    def trigger_out_mode(self, val: int):
        self._trigger_out_mode = val

    @property
    def trigger_out_polarity(self) -> int:
        return self._trigger_out_polarity

    @trigger_out_polarity.setter
    def trigger_out_polarity(self, val: int):
        self._trigger_out_polarity = val

    @property
    def trigger_out_forward_start_position(self) -> int:
        return self._trigger_out_forward_start_position

    @trigger_out_forward_start_position.setter
    def trigger_out_forward_start_position(self, val: int):
        self._trigger_out_forward_start_position = val

    @property
    def trigger_out_forward_interval(self) -> int:
        return self._trigger_out_forward_interval

    @trigger_out_forward_interval.setter
    def trigger_out_forward_interval(self, val: int):
        self._trigger_out_forward_interval = val

    @property
    def trigger_out_forward_number_of_pulses(self) -> int:
        return self._trigger_out_forward_number_of_pulses

    @trigger_out_forward_number_of_pulses.setter
    def trigger_out_forward_number_of_pulses(self, val: int):
        self._trigger_out_forward_number_of_pulses = val

    @property
    def trigger_out_reverse_start_position(self) -> int:
        return self._trigger_out_reverse_start_position

    @trigger_out_reverse_start_position.setter
    def trigger_out_reverse_start_position(self, val: int):
        self._trigger_out_reverse_start_position = val

    @property
    def trigger_out_reverse_interval(self) -> int:
        return self._trigger_out_reverse_interval

    @trigger_out_reverse_interval.setter
    def trigger_out_reverse_interval(self, val: int):
        self._trigger_out_reverse_interval = val

    @property
    def trigger_out_reverse_number_of_pulses(self) -> int:
        return self._trigger_out_reverse_number_of_pulses

    @trigger_out_reverse_number_of_pulses.setter
    def trigger_out_reverse_number_of_pulses(self, val: int):
        self._trigger_out_reverse_number_of_pulses = val

    @property
    def trigger_out_pulse_width(self) -> int:
        return self._trigger_out_pulse_width

    @trigger_out_pulse_width.setter
    def trigger_out_pulse_width(self, val: int):
        self._trigger_out_pulse_width = val

    @property
    def trigger_out_number_of_cycles(self) -> int:
        return self._trigger_out_number_of_cycles

    @trigger_out_number_of_cycles.setter
    def trigger_out_number_of_cycles(self, val: int):
        self._trigger_out_number_of_cycles = val


class TLMC_JogParams():
    def __init__(self):
        self._mode = TLMC_JogMode.TLMC_JogMode_Continuous
        self._step_size = 0
        self._min_velocity = 0
        self._acceleration = 0
        self._max_velocity = 0
        self._stop_mode = TLMC_JogStopMode.TLMC_JogStopMode_Immediate

    @property
    def mode(self) -> TLMC_JogMode:
        return self._mode

    @mode.setter
    def mode(self, val: TLMC_JogMode):
        self._mode = val

    @property
    def step_size(self) -> int:
        return self._step_size

    @step_size.setter
    def step_size(self, val: int):
        self._step_size = val

    @property
    def min_velocity(self) -> int:
        return self._min_velocity

    @min_velocity.setter
    def min_velocity(self, val: int):
        self._min_velocity = val

    @property
    def acceleration(self) -> int:
        return self._acceleration

    @acceleration.setter
    def acceleration(self, val: int):
        self._acceleration = val

    @property
    def max_velocity(self) -> int:
        return self._max_velocity

    @max_velocity.setter
    def max_velocity(self, val: int):
        self._max_velocity = val

    @property
    def stop_mode(self) -> TLMC_JogStopMode:
        return self._stop_mode

    @stop_mode.setter
    def stop_mode(self, val: TLMC_JogStopMode):
        self._stop_mode = val


class TLMC_JoystickParams():
    def __init__(self):
        self._low_gear_max_velocity = 0
        self._high_gear_max_velocity = 0
        self._low_gear_acceleration = 0
        self._high_gear_acceleration = 0
        self._direction_sense = TLMC_JoystickDirectionSense.TLMC_JoystickDirectionSense_Positive

    @property
    def low_gear_max_velocity(self) -> int:
        return self._low_gear_max_velocity

    @low_gear_max_velocity.setter
    def low_gear_max_velocity(self, val: int):
        self._low_gear_max_velocity = val

    @property
    def high_gear_max_velocity(self) -> int:
        return self._high_gear_max_velocity

    @high_gear_max_velocity.setter
    def high_gear_max_velocity(self, val: int):
        self._high_gear_max_velocity = val

    @property
    def low_gear_acceleration(self) -> int:
        return self._low_gear_acceleration

    @low_gear_acceleration.setter
    def low_gear_acceleration(self, val: int):
        self._low_gear_acceleration = val

    @property
    def high_gear_acceleration(self) -> int:
        return self._high_gear_acceleration

    @high_gear_acceleration.setter
    def high_gear_acceleration(self, val: int):
        self._high_gear_acceleration = val

    @property
    def direction_sense(self) -> TLMC_JoystickDirectionSense:
        return self._direction_sense

    @direction_sense.setter
    def direction_sense(self, val: TLMC_JoystickDirectionSense):
        self._direction_sense = val


class TLMC_JoystickSettingsParams():

    def __init__(self):

        self._joystick_serial_interface = TLMC_JoystickSerialInterface.TLMC_JoystickSerialInterface_Disabled
        self._joystick_model = TLMC_JoystickModel.TLMC_JoystickModel_NotSelected
        self._direction_sense: tuple[
            TLMC_JoystickDirectionSense,
            TLMC_JoystickDirectionSense,
            TLMC_JoystickDirectionSense,
        ] = (
            TLMC_JoystickDirectionSense.TLMC_JoystickDirectionSense_Disabled,
            TLMC_JoystickDirectionSense.TLMC_JoystickDirectionSense_Disabled,
            TLMC_JoystickDirectionSense.TLMC_JoystickDirectionSense_Disabled,
        )
        self._axis_mapping: tuple[
            TLMC_JoystickAxis,
            TLMC_JoystickAxis,
            TLMC_JoystickAxis,
        ] = (
            TLMC_JoystickAxis.TLMC_JoystickAxis_Unspecified,
            TLMC_JoystickAxis.TLMC_JoystickAxis_Unspecified,
            TLMC_JoystickAxis.TLMC_JoystickAxis_Unspecified,
        )


    @property
    def joystick_serial_interface(self) -> TLMC_JoystickSerialInterface:
        return self._joystick_serial_interface

    @joystick_serial_interface.setter
    def joystick_serial_interface(self, val: TLMC_JoystickSerialInterface):
        self._joystick_serial_interface = val

    @property
    def joystick_model(self) -> TLMC_JoystickModel:
        return self._joystick_model

    @joystick_model.setter
    def joystick_model(self, val: TLMC_JoystickModel):
        self._joystick_model = val

    @property
    def direction_sense(self) -> tuple[TLMC_JoystickDirectionSense, TLMC_JoystickDirectionSense, TLMC_JoystickDirectionSense]:
        return self._direction_sense

    @direction_sense.setter
    def direction_sense(self, val: tuple[TLMC_JoystickDirectionSense, TLMC_JoystickDirectionSense, TLMC_JoystickDirectionSense]):
        self._direction_sense = val

    @property
    def axis_mapping(self) -> tuple[TLMC_JoystickAxis, TLMC_JoystickAxis, TLMC_JoystickAxis]:
        return self._axis_mapping

    @axis_mapping.setter
    def axis_mapping(self, val: tuple[TLMC_JoystickAxis, TLMC_JoystickAxis, TLMC_JoystickAxis]):
        self._axis_mapping = val


class TLMC_KcubeIoTriggerParams():

    def __init__(self):
        self._trigger_1_mode = TLMC_KcubeIoTriggerMode.TLMC_KcubeIoTriggerMode_Disabled
        self._trigger_1_polarity = TLMC_KcubeIoTriggerPolarity.TLMC_KcubeIoTriggerPolarity_ActiveIsLogicHigh
        self._trigger_2_mode = TLMC_KcubeIoTriggerMode.TLMC_KcubeIoTriggerMode_Disabled
        self._trigger_2_polarity = TLMC_KcubeIoTriggerPolarity.TLMC_KcubeIoTriggerPolarity_ActiveIsLogicHigh

    @property
    def trigger_1_mode(self) -> TLMC_KcubeIoTriggerMode:
        return self._trigger_1_mode

    @trigger_1_mode.setter
    def trigger_1_mode(self, val: TLMC_KcubeIoTriggerMode):
        self._trigger_1_mode = val

    @property
    def trigger_1_polarity(self) -> TLMC_KcubeIoTriggerPolarity:
        return self._trigger_1_polarity

    @trigger_1_polarity.setter
    def trigger_1_polarity(self, val: TLMC_KcubeIoTriggerPolarity):
        self._trigger_1_polarity = val

    @property
    def trigger_2_mode(self) -> TLMC_KcubeIoTriggerMode:
        return self._trigger_2_mode

    @trigger_2_mode.setter
    def trigger_2_mode(self, val: TLMC_KcubeIoTriggerMode):
        self._trigger_2_mode = val

    @property
    def trigger_2_polarity(self) -> TLMC_KcubeIoTriggerPolarity:
        return self._trigger_2_polarity

    @trigger_2_polarity.setter
    def trigger_2_polarity(self, val: TLMC_KcubeIoTriggerPolarity):
        self._trigger_2_polarity = val


class TLMC_KcubeMmiParams():
    def __init__(self):
        self._joystick_mode = TLMC_KcubeMmi_JoystickMode.TLMC_KcubeMmi_JoystickMode_ControlsVelocity
        self._joystick_max_velocity = 0
        self._joystick_acceleration = 0
        self._joystick_direction_sense = TLMC_KcubeMmi_JoystickDirectionSense.TLMC_KcubeMmi_JoystickDirectionSense_Disabled
        self._preset_position_1 = 0
        self._preset_position_2 = 0
        self._display_brightness = 0
        self._display_timeout = 0
        self._display_dim_level = 0
        self._preset_position_3 = 0
        self._joystick_sensitivity = 0

    @property
    def joystick_mode(self) -> TLMC_KcubeMmi_JoystickMode:
        return self._joystick_mode

    @joystick_mode.setter
    def joystick_mode(self, val: TLMC_KcubeMmi_JoystickMode):
        self._joystick_mode = val

    @property
    def joystick_max_velocity(self) -> int:
        return self._joystick_max_velocity

    @joystick_max_velocity.setter
    def joystick_max_velocity(self, val: int):
        self._joystick_max_velocity = val

    @property
    def joystick_acceleration(self) -> int:
        return self._joystick_acceleration

    @joystick_acceleration.setter
    def joystick_acceleration(self, val: int):
        self._joystick_acceleration = val

    @property
    def joystick_direction_sense(self) -> TLMC_KcubeMmi_JoystickDirectionSense:
        return self._joystick_direction_sense

    @joystick_direction_sense.setter
    def joystick_direction_sense(self, val : TLMC_KcubeMmi_JoystickDirectionSense):
        self._joystick_direction_sense = val

    @property
    def preset_position_1(self) -> int:
        return self._preset_position_1

    @preset_position_1.setter
    def preset_position_1(self, val: int):
        self._preset_position_1 = val

    @property
    def preset_position_2(self) -> int:
        return self._preset_position_2

    @preset_position_2.setter
    def preset_position_2(self, val: int):
        self._preset_position_2 = val

    @property
    def display_brightness(self) -> int:
        return self._display_brightness

    @display_brightness.setter
    def display_brightness(self, val: int):
        self._display_brightness = val

    @property
    def display_timeout(self) -> int:
        return self._display_timeout

    @display_timeout.setter
    def display_timeout(self, val: int):
        self._display_timeout = val

    @property
    def display_dim_level(self) -> int:
        return self._display_dim_level

    @display_dim_level.setter
    def display_dim_level(self, val: int):
        self._display_dim_level = val

    @property
    def preset_position_3(self) -> int:
        return self._preset_position_3

    @preset_position_3.setter
    def preset_position_3(self, val: int):
        self._preset_position_3 = val

    @property
    def joystick_sensitivity(self) -> int:
        return self._joystick_sensitivity

    @joystick_sensitivity.setter
    def joystick_sensitivity(self, val: int):
        self._joystick_sensitivity = val


class TLMC_KcubePositionTriggerParams():
    def __init__(self):
        self._forward_start_position = 0
        self._forward_interval = 0
        self._forward_number_of_pulses = 0
        self._reverse_start_position = 0
        self._reverse_interval = 0
        self._reverse_number_of_pulses = 0
        self._pulse_width = 0
        self._number_of_cycles = 0

    @property
    def forward_start_position(self) -> int:
        return self._forward_start_position

    @forward_start_position.setter
    def forward_start_position(self, val: int):
        self._forward_start_position = val

    @property
    def forward_interval(self) -> int:
        return self._forward_interval

    @forward_interval.setter
    def forward_interval(self, val: int):
        self._forward_interval = val

    @property
    def forward_number_of_pulses(self) -> int:
        return self._forward_number_of_pulses

    @forward_number_of_pulses.setter
    def forward_number_of_pulses(self, val: int):
        self._forward_number_of_pulses = val

    @property
    def reverse_start_position(self) -> int:
        return self._reverse_start_position

    @reverse_start_position.setter
    def reverse_start_position(self, val: int):
        self._reverse_start_position = val

    @property
    def reverse_interval(self) -> int:
        return self._reverse_interval

    @reverse_interval.setter
    def reverse_interval(self, val: int):
        self._reverse_interval = val

    @property
    def reverse_number_of_pulses(self) -> int:
        return self._reverse_number_of_pulses

    @reverse_number_of_pulses.setter
    def reverse_number_of_pulses(self, val: int):
        self._reverse_number_of_pulses = val

    @property
    def pulse_width(self) -> int:
        return self._pulse_width

    @pulse_width.setter
    def pulse_width(self, val: int):
        self._pulse_width = val

    @property
    def number_of_cycles(self) -> int:
        return self._number_of_cycles

    @number_of_cycles.setter
    def number_of_cycles(self, val: int):
        self._number_of_cycles = val


class TLMC_LcdDisplayParams():
    def __init__(self):
        self._knob_sensitivity = 0
        self._display_brightness = 0
        self._display_timeout = 0
        self._display_dim_level = 0

    @property
    def knob_sensitivity(self) -> int:
        return self._knob_sensitivity

    @knob_sensitivity.setter
    def knob_sensitivity(self, val: int):
        self._knob_sensitivity = val

    @property
    def display_brightness(self) -> int:
        return self._display_brightness

    @display_brightness.setter
    def display_brightness(self, val: int):
        self._display_brightness = val

    @property
    def display_timeout(self) -> int:
        return self._display_timeout

    @display_timeout.setter
    def display_timeout(self, val: int):
        self._display_timeout = val

    @property
    def display_dim_level(self) -> int:
        return self._display_dim_level

    @display_dim_level.setter
    def display_dim_level(self, val: int):
        self._display_dim_level = val


class TLMC_LcdMoveParams():
    def __init__(self):
        self._knob_mode = 0
        self._jog_step_size = 0
        self._acceleration = 0
        self._max_velocity = 0
        self._jog_stop_mode = TLMC_JogStopMode.TLMC_JogStopMode_Immediate
        self._preset_position = []

    @property
    def knob_mode(self) -> int:
        return self._knob_mode

    @knob_mode.setter
    def knob_mode(self, val: int):
        self._knob_mode = val

    @property
    def jog_step_size(self) -> int:
        return self._jog_step_size

    @jog_step_size.setter
    def jog_step_size(self, val: int):
        self._jog_step_size = val

    @property
    def acceleration(self) -> int:
        return self._acceleration

    @acceleration.setter
    def acceleration(self, val: int):
        self._acceleration = val

    @property
    def max_velocity(self) -> int:
        return self._max_velocity

    @max_velocity.setter
    def max_velocity(self, val: int):
        self._max_velocity = val

    @property
    def jog_stop_mode(self) -> TLMC_JogStopMode:
        return self._jog_stop_mode

    @jog_stop_mode.setter
    def jog_stop_mode(self, val: TLMC_JogStopMode):
        self._jog_stop_mode = val

    @property
    def preset_position(self) -> list[int]:
        return self._preset_position

    @preset_position.setter
    def preset_position(self, vals: Sequence[int]):
        self._preset_position = [
            int(v) for i, v in enumerate(vals) # type: ignore
        ]


class TLMC_LimitSwitchParams():
    def __init__(self):
        self._clockwise_hard_limit_operating_mode = TLMC_HardLimitOperatingMode.TLMC_HardLimitOperatingMode_SwitchIgnored
        self._counterclockwise_hard_limit_operating_mode = TLMC_HardLimitOperatingMode.TLMC_HardLimitOperatingMode_SwitchIgnored
        self._clockwise_soft_limit = 0
        self._counterclockwise_soft_limit = 0
        self._soft_limit_operating_mode = TLMC_SoftLimitOperatingMode.TLMC_SoftLimitOperatingMode_FeatureNotSupported

    @property
    def clockwise_limit_mode(self) -> TLMC_HardLimitOperatingMode:
        return self._clockwise_hard_limit_operating_mode

    @clockwise_limit_mode.setter
    def clockwise_limit_mode(self, val: TLMC_HardLimitOperatingMode):
        self._clockwise_hard_limit_operating_mode = val

    @property
    def counterclockwise_limit_mode(self) -> TLMC_HardLimitOperatingMode:
        return self._counterclockwise_hard_limit_operating_mode

    @counterclockwise_limit_mode.setter
    def counterclockwise_limit_mode(self, val: TLMC_HardLimitOperatingMode):
        self._counterclockwise_hard_limit_operating_mode = val

    @property
    def clockwise_soft_limit(self) -> int:
        return self._clockwise_soft_limit

    @clockwise_soft_limit.setter
    def clockwise_soft_limit(self, val: int):
        self._clockwise_soft_limit = val

    @property
    def counterclockwise_soft_limit(self) -> int:
        return self._counterclockwise_soft_limit

    @counterclockwise_soft_limit.setter
    def counterclockwise_soft_limit(self, val: int):
        self._counterclockwise_soft_limit = val

    @property
    def soft_limit_operating_mode(self) -> TLMC_SoftLimitOperatingMode:
        return self._soft_limit_operating_mode

    @soft_limit_operating_mode.setter
    def soft_limit_operating_mode(self, val: TLMC_SoftLimitOperatingMode):
        self._soft_limit_operating_mode = val


class TLMC_MonitorOutputParams():

    def __init__(self):

        self._monitor_output = TLMC_MonitorOutput.TLMC_MonitorOutput_None
        self._dac = 0

    @property
    def monitor_output(self) -> TLMC_MonitorOutput:
        return self._monitor_output

    @monitor_output.setter
    def monitor_output(self, val: TLMC_MonitorOutput):
        self._monitor_output = val

    @property
    def dac(self) -> int:
        return self._dac

    @dac.setter
    def dac(self, val: int):
        self._dac = val


class TLMC_MotorOutputParams():
    def __init__(self):
        self._continuous_current_limit = 0
        self._energy_limit = 0
        self._motor_limit = 0
        self._motor_bias = 0

    @property
    def continuous_current_limit(self) -> int:
        return self._continuous_current_limit

    @continuous_current_limit.setter
    def continuous_current_limit(self, val: int):
        self._continuous_current_limit = val

    @property
    def energy_limit(self) -> int:
        return self._energy_limit

    @energy_limit.setter
    def energy_limit(self, val: int):
        self._energy_limit = val

    @property
    def motor_limit(self) -> int:
        return self._motor_limit

    @motor_limit.setter
    def motor_limit(self, val: int):
        self._motor_limit = val

    @property
    def motor_bias(self) -> int:
        return self._motor_bias

    @motor_bias.setter
    def motor_bias(self, val: int):
        self._motor_bias = val


class TLMC_MoveAbsoluteParams():
    def __init__(self):
        self._absolute_position = 0

    @property
    def absolute_position(self) -> int:
        return self._absolute_position

    @absolute_position.setter
    def absolute_position(self, val: int):
        self._absolute_position = val


class TLMC_MoveRelativeParams():
    def __init__(self):
        self._relative_distance = 0

    @property
    def relative_distance(self) -> int:
        return self._relative_distance

    @relative_distance.setter
    def relative_distance(self, val: int):
        self._relative_distance = val


class TLMC_PositionLoopParams():
    def __init__(self):
        self._proportional = 0
        self._integral = 0
        self._integral_limit = 0
        self._derivative = 0
        self._servo_cycles = 0
        self._scale = 0
        self._velocity_feed_forward = 0
        self._acceleration_feed_forward = 0
        self._error_limit = 0

    @property
    def proportional(self) -> int:
        return self._proportional

    @proportional.setter
    def proportional(self, val: int):
        self._proportional = val

    @property
    def integral(self) -> int:
        return self._integral

    @integral.setter
    def integral(self, val: int):
        self._integral = val

    @property
    def integral_limit(self) -> int:
        return self._integral_limit

    @integral_limit.setter
    def integral_limit(self, val: int):
        self._integral_limit = val

    @property
    def derivative(self) -> int:
        return self._derivative

    @derivative.setter
    def derivative(self, val: int):
        self._derivative = val

    @property
    def servo_cycles(self) -> int:
        return self._servo_cycles

    @servo_cycles.setter
    def servo_cycles(self, val: int):
        self._servo_cycles = val

    @property
    def scale(self) -> int:
        return self._scale

    @scale.setter
    def scale(self, val: int):
        self._scale = val

    @property
    def velocity_feed_forward(self) -> int:
        return self._velocity_feed_forward

    @velocity_feed_forward.setter
    def velocity_feed_forward(self, val: int):
        self._velocity_feed_forward = val

    @property
    def acceleration_feed_forward(self) -> int:
        return self._acceleration_feed_forward

    @acceleration_feed_forward.setter
    def acceleration_feed_forward(self, val: int):
        self._acceleration_feed_forward = val

    @property
    def error_limit(self) -> int:
        return self._error_limit

    @error_limit.setter
    def error_limit(self, val: int):
        self._error_limit = val


class TLMC_PZ_IoTriggerParams():

    def __init__(self):

        self._number_of_ports_per_channel = 0
        self._port_number = TLMC_IoTriggerPortNumber.TLMC_IoTriggerPortNumber_None
        self._port_type = TLMC_PortType.TLMC_PortType_Physical
        self._mode = TLMC_PZ_IoTriggerMode.TLMC_PZ_IoTriggerMode_Disabled
        self._polarity = TLMC_IoTriggerPolarity.TLMC_IoTriggerPolarity_ActiveIsLogicHigh
        self._trigger_parameter1 = 0
        self._trigger_parameter2 = 0

    @property
    def number_of_ports_per_channel(self) -> int:
        return self._number_of_ports_per_channel

    @number_of_ports_per_channel.setter
    def number_of_ports_per_channel(self, val: int):
        self._number_of_ports_per_channel = val

    @property
    def port_number(self) -> TLMC_IoTriggerPortNumber:
        return self._port_number

    @port_number.setter
    def port_number(self, val: TLMC_IoTriggerPortNumber):
        self._port_number = val

    @property
    def port_type(self) -> TLMC_PortType:
        return self._port_type

    @port_type.setter
    def port_type(self, val: TLMC_PortType):
        self._port_type = val

    @property
    def mode(self) -> TLMC_PZ_IoTriggerMode:
        return self._mode

    @mode.setter
    def mode(self, val: TLMC_PZ_IoTriggerMode):
        self._mode = val

    @property
    def polarity(self) -> TLMC_IoTriggerPolarity:
        return self._polarity

    @polarity.setter
    def polarity(self, val: TLMC_IoTriggerPolarity):
        self._polarity = val

    @property
    def trigger_parameter1(self) -> int:
        return self._trigger_parameter1

    @trigger_parameter1.setter
    def trigger_parameter1(self, val: int):
        self._trigger_parameter1 = val

    @property
    def trigger_parameter2(self) -> int:
        return self._trigger_parameter2

    @trigger_parameter2.setter
    def trigger_parameter2(self, val: int):
        self._trigger_parameter2 = val


class TLMC_PZ_KpcIoTriggerParams():
    def __init__(self):
        self._trigger_1_mode = TLMC_PZ_KpcIoTriggerMode.TLMC_PZ_KpcIoTriggerMode_Disabled
        self._trigger_1_polarity = TLMC_KcubeIoTriggerPolarity.TLMC_KcubeIoTriggerPolarity_ActiveIsLogicHigh
        self._trigger_2_mode = TLMC_PZ_KpcIoTriggerMode.TLMC_PZ_KpcIoTriggerMode_Disabled
        self._trigger_2_polarity = TLMC_KcubeIoTriggerPolarity.TLMC_KcubeIoTriggerPolarity_ActiveIsLogicHigh
        self._strain_gauge_lower_limit = 0
        self._strain_gauge_upper_limit = 0
        self._smoothing_samples = 0
        self._monitor_output_mode = TLMC_PZ_KpcMonitorOutputMode.TLMC_PZ_KpcMonitorOutputMode_Software
        self._monitor_filter_cut_off_frequency = 0
        self._monitor_output_software_value = 0

    @property
    def trigger_1_mode(self) -> TLMC_PZ_KpcIoTriggerMode:
        return self._trigger_1_mode

    @trigger_1_mode.setter
    def trigger_1_mode(self, val: TLMC_PZ_KpcIoTriggerMode):
        self._trigger_1_mode = val

    @property
    def trigger_1_polarity(self) -> TLMC_KcubeIoTriggerPolarity:
        return self._trigger_1_polarity

    @trigger_1_polarity.setter
    def trigger_1_polarity(self, val: TLMC_KcubeIoTriggerPolarity):
        self._trigger_1_polarity = val

    @property
    def trigger_2_mode(self) -> TLMC_PZ_KpcIoTriggerMode:
        return self._trigger_2_mode

    @trigger_2_mode.setter
    def trigger_2_mode(self, val: TLMC_PZ_KpcIoTriggerMode):
        self._trigger_2_mode = val

    @property
    def trigger_2_polarity(self) -> TLMC_KcubeIoTriggerPolarity:
        return self._trigger_2_polarity

    @trigger_2_polarity.setter
    def trigger_2_polarity(self, val: TLMC_KcubeIoTriggerPolarity):
        self._trigger_2_polarity = val

    @property
    def strain_gauge_lower_limit(self) -> int:
        return self._strain_gauge_lower_limit

    @strain_gauge_lower_limit.setter
    def strain_gauge_lower_limit(self, val: int):
        self._strain_gauge_lower_limit = val

    @property
    def strain_gauge_upper_limit(self) -> int:
        return self._strain_gauge_upper_limit

    @strain_gauge_upper_limit.setter
    def strain_gauge_upper_limit(self, val: int):
        self._strain_gauge_upper_limit = val

    @property
    def smoothing_samples(self) -> int:
        return self._smoothing_samples

    @smoothing_samples.setter
    def smoothing_samples(self, val: int):
        self._smoothing_samples = val

    @property
    def monitor_output_mode(self) -> TLMC_PZ_KpcMonitorOutputMode:
        return self._monitor_output_mode

    @monitor_output_mode.setter
    def monitor_output_mode(self, val: TLMC_PZ_KpcMonitorOutputMode):
        self._monitor_output_mode = val

    @property
    def monitor_filter_cut_off_frequency(self) -> int:
        return self._monitor_filter_cut_off_frequency

    @monitor_filter_cut_off_frequency.setter
    def monitor_filter_cut_off_frequency(self, val: int):
        self._monitor_filter_cut_off_frequency = val

    @property
    def monitor_output_software_value(self) -> int:
        return self._monitor_output_software_value

    @monitor_output_software_value.setter
    def monitor_output_software_value(self, val: int):
        self._monitor_output_software_value = val


class TLMC_PZ_KpcIoSettingsParams():
    def __init__(self):
        self._voltage_limit = 0
        self._analog_input_source = TLMC_PZ_KpcAnalogInputSource.TLMC_PZ_KpcAnalogInputSource_Disabled
        self._filter_cut_off_frequency = 0
        self._voltage_range = TLMC_PZ_KpcVoltageRange.TLMC_PZ_KpcVoltageRange_75Volts
        self._force_sense = 0
        self._strain_gauge_option = TLMC_PZ_KpcStrainGaugeOption.TLMC_PZ_KpcStrainGaugeOption_Position

    @property
    def voltage_limit(self) -> int:
        return self._voltage_limit

    @voltage_limit.setter
    def voltage_limit(self, val: int):
        self._voltage_limit = val

    @property
    def analog_input_source(self) -> TLMC_PZ_KpcAnalogInputSource:
        return self._analog_input_source

    @analog_input_source.setter
    def analog_input_source(self, val: TLMC_PZ_KpcAnalogInputSource):
        self._analog_input_source = val

    @property
    def filter_cut_off_frequency(self) -> int:
        return self._filter_cut_off_frequency

    @filter_cut_off_frequency.setter
    def filter_cut_off_frequency(self, val: int):
        self._filter_cut_off_frequency = val

    @property
    def voltage_range(self) -> TLMC_PZ_KpcVoltageRange:
        return self._voltage_range

    @voltage_range.setter
    def voltage_range(self, val: TLMC_PZ_KpcVoltageRange):
        self._voltage_range = val

    @property
    def force_sense(self) -> int:
        return self._force_sense

    @force_sense.setter
    def force_sense(self, val: int):
        self._force_sense = val

    @property
    def strain_gauge_option(self) -> TLMC_PZ_KpcStrainGaugeOption:
        return self._strain_gauge_option

    @strain_gauge_option.setter
    def strain_gauge_option(self, val: TLMC_PZ_KpcStrainGaugeOption):
        self._strain_gauge_option = val


class TLMC_PZ_KpcMmiParams():
    def __init__(self):
        self._joystick_mode = TLMC_PZ_KpcMmi_JoystickMode.TLMC_PZ_KpcMmiJoystickMode_ControlsVoltagePosition
        self._joystick_gear = TLMC_KcubeMmi_JoystickGear.TLMC_KcubeMmiJoystickGear_High
        self._joystick_voltage_step_size = 0
        self._joystick_position_step_size = 0
        self._joystick_direction_sense = TLMC_PZ_KpcMmi_JoystickDirectionSense.TLMC_PZ_KpcMmiJoystickDirectionSense_Disabled
        self._preset_voltage_1 = 0
        self._preset_voltage_2 = 0
        self._preset_position_1 = 0
        self._preset_position_2 = 0
        self._display_brightness = 0
        self._display_timeout = 0
        self._display_dim_level = 0

    @property
    def joystick_mode(self) -> TLMC_PZ_KpcMmi_JoystickMode:
        return self._joystick_mode

    @joystick_mode.setter
    def joystick_mode(self, val: TLMC_PZ_KpcMmi_JoystickMode) -> None:
        self._joystick_mode = val

    @property
    def joystick_gear(self) -> TLMC_KcubeMmi_JoystickGear:
        return self._joystick_gear

    @joystick_gear.setter
    def joystick_gear(self, val: TLMC_KcubeMmi_JoystickGear) -> None:
        self._joystick_gear = val

    @property
    def joystick_voltage_step_size(self) -> int:
        return self._joystick_voltage_step_size

    @joystick_voltage_step_size.setter
    def joystick_voltage_step_size(self, val: int) -> None:
        self._joystick_voltage_step_size = val

    @property
    def joystick_position_step_size(self) -> int:
        return self._joystick_position_step_size

    @joystick_position_step_size.setter
    def joystick_position_step_size(self, val: int) -> None:
        self._joystick_position_step_size = val

    @property
    def joystick_direction_sense(self) -> TLMC_PZ_KpcMmi_JoystickDirectionSense:
        return self._joystick_direction_sense

    @joystick_direction_sense.setter
    def joystick_direction_sense(self, val: TLMC_PZ_KpcMmi_JoystickDirectionSense) -> None:
        self._joystick_direction_sense = val

    @property
    def preset_voltage_1(self) -> int:
        return self._preset_voltage_1

    @preset_voltage_1.setter
    def preset_voltage_1(self, val: int) -> None:
        self._preset_voltage_1 = val

    @property
    def preset_voltage_2(self) -> int:
        return self._preset_voltage_2

    @preset_voltage_2.setter
    def preset_voltage_2(self, val: int) -> None:
        self._preset_voltage_2 = val

    @property
    def preset_position_1(self) -> int:
        return self._preset_position_1

    @preset_position_1.setter
    def preset_position_1(self, val: int) -> None:
        self._preset_position_1 = val

    @property
    def preset_position_2(self) -> int:
        return self._preset_position_2

    @preset_position_2.setter
    def preset_position_2(self, val: int) -> None:
        self._preset_position_2 = val

    @property
    def display_brightness(self) -> int:
        return self._display_brightness

    @display_brightness.setter
    def display_brightness(self, val: int) -> None:
        self._display_brightness = val

    @property
    def display_timeout(self) -> int:
        return self._display_timeout

    @display_timeout.setter
    def display_timeout(self, val: int) -> None:
        self._display_timeout = val

    @property
    def display_dim_level(self) -> int:
        return self._display_dim_level

    @display_dim_level.setter
    def display_dim_level(self, val: int) -> None:
        self._display_dim_level = val


class TLMC_PZ_LnnxControlLoopParams():

    def __init__(self):

        self._override_mode = TLMC_PZ_LnnxControlLoopParamsOverrideMode.TLMC_PZ_LnnxControlLoopParamsOverrideMode_FromStage
        self._proportional = 0
        self._integral = 0
        self._derivative = 0
        self._feed_forward = 0


    @property
    def override_mode(self) -> TLMC_PZ_LnnxControlLoopParamsOverrideMode:
        return self._override_mode

    @override_mode.setter
    def override_mode(self, val: TLMC_PZ_LnnxControlLoopParamsOverrideMode):
        self._override_mode = val

    @property
    def proportional(self) -> int:
        return self._proportional

    @proportional.setter
    def proportional(self, val: int):
        self._proportional = val

    @property
    def integral(self) -> int:
        return self._integral

    @integral.setter
    def integral(self, val: int):
        self._integral = val

    @property
    def derivative(self) -> int:
        return self._derivative

    @derivative.setter
    def derivative(self, val: int):
        self._derivative = val

    @property
    def feed_forward(self) -> int:
        return self._feed_forward

    @feed_forward.setter
    def feed_forward(self, val: int):
        self._feed_forward = val


class TLMC_PZ_LnnxNotchFilterParams():

    def __init__(self):

        self._override_mode = TLMC_PZ_LnnxNotchFilterParamsOverrideMode.TLMC_PZ_LnnxNotchFilterParamsOverrideMode_FromStage
        self._filter1_center_frequency = 0
        self._filter1_quality_factor = 0
        self._filter2_center_frequency = 0
        self._filter2_quality_factor = 0

    @property
    def override_mode(self) -> TLMC_PZ_LnnxNotchFilterParamsOverrideMode:
        return self._override_mode

    @override_mode.setter
    def override_mode(self, val: TLMC_PZ_LnnxNotchFilterParamsOverrideMode):
        self._override_mode = val

    @property
    def filter1_center_frequency(self) -> int:
        return self._filter1_center_frequency

    @filter1_center_frequency.setter
    def filter1_center_frequency(self, val: int):
        self._filter1_center_frequency = val

    @property
    def filter1_quality_factor(self) -> int:
        return self._filter1_quality_factor

    @filter1_quality_factor.setter
    def filter1_quality_factor(self, val: int):
        self._filter1_quality_factor = val

    @property
    def filter2_center_frequency(self) -> int:
        return self._filter2_center_frequency

    @filter2_center_frequency.setter
    def filter2_center_frequency(self, val: int):
        self._filter2_center_frequency = val

    @property
    def filter2_quality_factor(self) -> int:
        return self._filter2_quality_factor

    @filter2_quality_factor.setter
    def filter2_quality_factor(self, val: int):
        self._filter2_quality_factor = val


class TLMC_PZ_MaxOutputVoltageParams():
    def __init__(self):
        self._max_output_voltage = 0
        self._voltage_limit = TLMC_PZ_VoltageLimit.TLMC_PZ_VoltageLimit_75Volts

    @property
    def max_output_voltage(self) -> int:
        return self._max_output_voltage

    @max_output_voltage.setter
    def max_output_voltage(self, val: int):
        self._max_output_voltage = val

    @property
    def voltage_limit(self) -> TLMC_PZ_VoltageLimit:
        return self._voltage_limit

    @voltage_limit.setter
    def voltage_limit(self, val: TLMC_PZ_VoltageLimit):
        self._voltage_limit = val


class TLMC_PZ_NanoTrakCircleDiameterLookupTableData():
    def __init__(self):
        self._lookup_table_values = []

    @property
    def lookup_table_values(self)-> list[int]:
        return self._lookup_table_values

    @lookup_table_values.setter
    def lookup_table_values(self, val: list[int]) -> None:
        self._lookup_table_values = val


class TLMC_PZ_NanoTrakCircleHomePositionParams():
    def __init__(self):
        self._circle_home_position_a = 0
        self._circle_home_position_b = 0

    @property
    def circle_home_position_a(self) -> int:
        return self._circle_home_position_a

    @circle_home_position_a.setter
    def circle_home_position_a(self, val: int) -> None:
        self._circle_home_position_a = val

    @property
    def circle_home_position_b(self) -> int:
        return self._circle_home_position_b

    @circle_home_position_b.setter
    def circle_home_position_b(self, val: int) -> None:
        self._circle_home_position_b = val


class TLMC_PZ_NanoTrakCircleParams():
    def __init__(self):
        self._circle_diameter_mode = TLMC_PZ_NanoTrakCircleDiameterMode.TLMC_PZ_NanoTrakCircleDiameterModes_Software
        self._circle_diameter_software = 0
        self._circle_oscillation_frequency = 0
        self._absolute_power_min_circle_diameter = 0
        self._absolute_power_max_circle_diameter = 0
        self._absolute_power_adjust_type = TLMC_PZ_NanoTrakAbsolutePowerAdjustType.TLMC_PZ_NanoTrakAbsolutePowerAdjustType_LIN

    @property
    def circle_diameter_mode(self) -> TLMC_PZ_NanoTrakCircleDiameterMode:
        return self._circle_diameter_mode

    @circle_diameter_mode.setter
    def circle_diameter_mode(self, val: TLMC_PZ_NanoTrakCircleDiameterMode) -> None:
        self._circle_diameter_mode = val

    @property
    def circle_diameter_software(self) -> int:
        return self._circle_diameter_software

    @circle_diameter_software.setter
    def circle_diameter_software(self, val: int) -> None:
        self._circle_diameter_software = val

    @property
    def circle_oscillation_frequency(self) -> int:
        return self._circle_oscillation_frequency

    @circle_oscillation_frequency.setter
    def circle_oscillation_frequency(self, val: int) -> None:
        self._circle_oscillation_frequency = val

    @property
    def absolute_power_min_circle_diameter(self) -> int:
        return self._absolute_power_min_circle_diameter

    @absolute_power_min_circle_diameter.setter
    def absolute_power_min_circle_diameter(self, val: int) -> None:
        self._absolute_power_min_circle_diameter = val

    @property
    def absolute_power_max_circle_diameter(self) -> int:
        return self._absolute_power_max_circle_diameter

    @absolute_power_max_circle_diameter.setter
    def absolute_power_max_circle_diameter(self, val: int) -> None:
        self._absolute_power_max_circle_diameter = val

    @property
    def absolute_power_adjust_type(self) -> TLMC_PZ_NanoTrakAbsolutePowerAdjustType:
        return self._absolute_power_adjust_type

    @absolute_power_adjust_type.setter
    def absolute_power_adjust_type(self, val: TLMC_PZ_NanoTrakAbsolutePowerAdjustType) -> None:
        self._absolute_power_adjust_type = val


class TLMC_PZ_NanoTrakEEPROMParams():
    def __init__(self):
        self._channel_identifier = 0
        self._message_id = 0

    @property
    def channel_identifier(self) -> int:
        return self._channel_identifier

    @channel_identifier.setter
    def channel_identifier(self, val: int) -> None:
        self._channel_identifier = val

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, val: int) -> None:
        self._message_id = val


class TLMC_PZ_NanoTrakGainParams():
    def __init__(self):
        self._gain_control_mode = TLMC_PZ_NanoTrakGainControlMode.TLMC_PZ_NanoTrakGainControlMode_Software
        self._gain = 0

    @property
    def gain_control_mode(self) -> TLMC_PZ_NanoTrakGainControlMode:
        return self._gain_control_mode

    @gain_control_mode.setter
    def gain_control_mode(self, val: TLMC_PZ_NanoTrakGainControlMode) -> None:
        self._gain_control_mode = val

    @property
    def gain(self) -> int:
        return self._gain

    @gain.setter
    def gain(self, val: int) -> None:
        self._gain = val


class TLMC_PZ_NanoTrakMode():
    def __init__(self):
        self._state = TLMC_PZ_NanoTrakTrackingState.TLMC_PZ_NanoTrakTrackingState_ModeUndefined
        self._mode = TLMC_PZ_NanoTrakTrackingMode.TLMC_PZ_NanoTrakTrackingMode_DualAxisTracking

    @property
    def state(self) -> TLMC_PZ_NanoTrakTrackingState:
        return self._state

    @state.setter
    def state(self, val: TLMC_PZ_NanoTrakTrackingState) -> None:
        self._state = val

    @property
    def mode(self) -> TLMC_PZ_NanoTrakTrackingMode:
        return self._mode

    @mode.setter
    def mode(self, val: TLMC_PZ_NanoTrakTrackingMode) -> None:
        self._mode = val


class TLMC_PZ_NanoTrakPhaseCompensationParams():
    def __init__(self):
        self._phase_compensation_mode = TLMC_PZ_NanoTrakPhaseCompensationMode.TLMC_PZ_NanoTrakPhaseCompensationMode_Manual
        self._phase_compensation_a_software = 0
        self._phase_compensation_b_software = 0

    @property
    def phase_compensation_mode(self) -> TLMC_PZ_NanoTrakPhaseCompensationMode:
        return self._phase_compensation_mode

    @phase_compensation_mode.setter
    def phase_compensation_mode(self, val: TLMC_PZ_NanoTrakPhaseCompensationMode) -> None:
        self._phase_compensation_mode = val

    @property
    def phase_compensation_a_software(self) -> int:
        return self._phase_compensation_a_software

    @phase_compensation_a_software.setter
    def phase_compensation_a_software(self, val: int) -> None:
        self._phase_compensation_a_software = val

    @property
    def phase_compensation_b_software(self) -> int:
        return self._phase_compensation_b_software

    @phase_compensation_b_software.setter
    def phase_compensation_b_software(self, val: int) -> None:
        self._phase_compensation_b_software = val


class TLMC_PZ_NanoTrakRangeParams():
    def __init__(self):
        self._range_mode = TLMC_PZ_NanoTrakRangeMode.TLMC_PZ_NanoTrakRangeMode_Auto
        self._range_up_limit = 0
        self._range_down_limit = 0
        self._settle_samples = 0
        self._range_change_type = TLMC_PZ_NanoTrakRangeChangeType.TLMC_PZ_NanoTrakRangeChangeType_All
        self._range_type = TLMC_PZ_NanoTrakRange.TLMC_PZ_NanoTrakRange_Range1

    @property
    def range_mode(self) -> TLMC_PZ_NanoTrakRangeMode:
        return self._range_mode

    @range_mode.setter
    def range_mode(self, val: TLMC_PZ_NanoTrakRangeMode) -> None:
        self._range_mode = val

    @property
    def range_up_limit(self) -> int:
        return self._range_up_limit

    @range_up_limit.setter
    def range_up_limit(self, val: int) -> None:
        self._range_up_limit = val

    @property
    def range_down_limit(self) -> int:
        return self._range_down_limit

    @range_down_limit.setter
    def range_down_limit(self, val: int) -> None:
        self._range_down_limit = val

    @property
    def settle_samples(self) -> int:
        return self._settle_samples

    @settle_samples.setter
    def settle_samples(self, val: int) -> None:
        self._settle_samples = val

    @property
    def range_change_type(self) -> TLMC_PZ_NanoTrakRangeChangeType:
        return self._range_change_type

    @range_change_type.setter
    def range_change_type(self, val: TLMC_PZ_NanoTrakRangeChangeType) -> None:
        self._range_change_type = val

    @property
    def range_type(self) -> TLMC_PZ_NanoTrakRange:
        return self._range_type

    @range_type.setter
    def range_type(self, val: TLMC_PZ_NanoTrakRange) -> None:
        self._range_type = val


class TLMC_PZ_NanoTrakStatus():
    def __init__(self):
        self._circle_position_a = 0
        self._circle_position_b = 0
        self._circle_diameter = 0
        self._absolute_reading = 0
        self._relative_reading = 0
        self._range = TLMC_PZ_NanoTrakRange.TLMC_PZ_NanoTrakRange_Range1
        self._under_over_read = TLMC_PZ_NanoTrakUnderOverReadType.TLMC_PZ_NanoTrakUnderOverReadType_InRange
        self._status_bits = TLMC_PZ_NanoTrakStatusBit.TLMC_PZ_NanoTrakStatusBit_Tracking
        self._nano_trak_gain = 0
        self._phase_compensation_a = 0
        self._phase_compensation_b = 0

    @property
    def circle_position_a(self) -> int:
        return self._circle_position_a

    @circle_position_a.setter
    def circle_position_a(self, val: int) -> None:
        self._circle_position_a = val

    @property
    def circle_position_b(self) -> int:
        return self._circle_position_b

    @circle_position_b.setter
    def circle_position_b(self, val: int) -> None:
        self._circle_position_b = val

    @property
    def circle_diameter(self) -> int:
        return self._circle_diameter

    @circle_diameter.setter
    def circle_diameter(self, val: int) -> None:
        self._circle_diameter = val

    @property
    def absolute_reading(self) -> int:
        return self._absolute_reading

    @absolute_reading.setter
    def absolute_reading(self, val: int) -> None:
        self._absolute_reading = val

    @property
    def relative_reading(self) -> int:
        return self._relative_reading

    @relative_reading.setter
    def relative_reading(self, val: int) -> None:
        self._relative_reading = val

    @property
    def range(self) -> TLMC_PZ_NanoTrakRange:
        return self._range

    @range.setter
    def range(self, val: TLMC_PZ_NanoTrakRange) -> None:
        self._range = val

    @property
    def under_over_read(self) -> TLMC_PZ_NanoTrakUnderOverReadType:
        return self._under_over_read

    @under_over_read.setter
    def under_over_read(self, val: TLMC_PZ_NanoTrakUnderOverReadType) -> None:
        self._under_over_read = val

    @property
    def status_bits(self) -> TLMC_PZ_NanoTrakStatusBit:
        return self._status_bits

    @status_bits.setter
    def status_bits(self, val: TLMC_PZ_NanoTrakStatusBit) -> None:
        self._status_bits = val

    @property
    def nano_trak_gain(self) -> int:
        return self._nano_trak_gain

    @nano_trak_gain.setter
    def nano_trak_gain(self, val: int) -> None:
        self._nano_trak_gain = val

    @property
    def phase_compensation_a(self) -> int:
        return self._phase_compensation_a

    @phase_compensation_a.setter
    def phase_compensation_a(self, val: int) -> None:
        self._phase_compensation_a = val

    @property
    def phase_compensation_b(self) -> int:
        return self._phase_compensation_b

    @phase_compensation_b.setter
    def phase_compensation_b(self, val: int) -> None:
        self._phase_compensation_b = val


class TLMC_PZ_NanoTrakTnaIoSettings():
    def __init__(self):
        self._out_range_type = TLMC_PZ_TnaIoOutRangeType.TLMC_PZ_TnaIoOutRangeType_5V
        self._out_route_type = TLMC_PZ_TnaIoOutRouteType.TLMC_PZ_TnaIoOutRouteType_SmaConnectorsOnly
        self._signal_source_mode = TLMC_PZ_TnaIoSignalSourceMode.TLMC_PZ_TnaIoSignalSourceMode_InternalPin
        self._signal_source_boost_type = TLMC_PZ_TnaIoSignalSourceBoostType.TLMC_PZ_TnaIoSignalSourceBoostType_Disabled
        self._signal_output_mode = TLMC_PZ_TnaIoSignalOutputMode.TLMC_PZ_TnaIoSignalOutputMode_Disabled
        self._channel_1_signal_range_type = TLMC_PZ_TnaIoSignalRangeType.TLMC_PZ_TnaIoSignalRangeType_75V
        self._channel_2_signal_range_type = TLMC_PZ_TnaIoSignalRangeType.TLMC_PZ_TnaIoSignalRangeType_75V

    @property
    def out_range_type(self) -> TLMC_PZ_TnaIoOutRangeType:
        return self._out_range_type

    @out_range_type.setter
    def out_range_type(self, val: TLMC_PZ_TnaIoOutRangeType) -> None:
        self._out_range_type = val

    @property
    def out_route_type(self) -> TLMC_PZ_TnaIoOutRouteType:
        return self._out_route_type

    @out_route_type.setter
    def out_route_type(self, val: TLMC_PZ_TnaIoOutRouteType) -> None:
        self._out_route_type = val

    @property
    def signal_source_mode(self) -> TLMC_PZ_TnaIoSignalSourceMode:
        return self._signal_source_mode

    @signal_source_mode.setter
    def signal_source_mode(self, val: TLMC_PZ_TnaIoSignalSourceMode) -> None:
        self._signal_source_mode = val

    @property
    def signal_source_boost_type(self) -> TLMC_PZ_TnaIoSignalSourceBoostType:
        return self._signal_source_boost_type

    @signal_source_boost_type.setter
    def signal_source_boost_type(self, val: TLMC_PZ_TnaIoSignalSourceBoostType) -> None:
        self._signal_source_boost_type = val

    @property
    def signal_output_mode(self) -> TLMC_PZ_TnaIoSignalOutputMode:
        return self._signal_output_mode

    @signal_output_mode.setter
    def signal_output_mode(self, val: TLMC_PZ_TnaIoSignalOutputMode) -> None:
        self._signal_output_mode = val

    @property
    def channel_1_signal_range_type(self) -> TLMC_PZ_TnaIoSignalRangeType:
        return self._channel_1_signal_range_type

    @channel_1_signal_range_type.setter
    def channel_1_signal_range_type(self, val: TLMC_PZ_TnaIoSignalRangeType) -> None:
        self._channel_1_signal_range_type = val

    @property
    def channel_2_signal_range_type(self) -> TLMC_PZ_TnaIoSignalRangeType:
        return self._channel_2_signal_range_type

    @channel_2_signal_range_type.setter
    def channel_2_signal_range_type(self, val: TLMC_PZ_TnaIoSignalRangeType) -> None:
        self._channel_2_signal_range_type = val


class TLMC_PZ_NanoTrakTrackThresholdParams():
    def __init__(self):
        self._track_threshold = 0

    @property
    def track_threshold(self) -> int:
        return self._track_threshold

    @track_threshold.setter
    def track_threshold(self, val: int) -> None:
        self._track_threshold = val


class TLMC_PZ_OutputVoltageControlSourceParams():
    def __init__(self):
        self._source = TLMC_PZ_OutputVoltageControlSource.TLMC_PZ_OutputVoltageControlSource_SoftwareOnly

    @property
    def source(self) -> TLMC_PZ_OutputVoltageControlSource:
        return self._source

    @source.setter
    def source(self, val: TLMC_PZ_OutputVoltageControlSource):
        self._source = val


class TLMC_PZ_OutputWaveformLoopTableSample():
    def __init__(self):
        self._index = 0
        self._voltage = 0

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, val: int):
        self._index = val

    @property
    def voltage(self) -> int:
        return self._voltage

    @voltage.setter
    def voltage(self, val: int):
        self._voltage = val


class TLMC_PZ_OutputWaveformParams():
    def __init__(self):
        self._mode = TLMC_PZ_OutputWaveformOperatingMode.TLMC_PZ_OutputWaveformOperatingMode_Continuous
        self._number_of_samples_per_cycle = 0
        self._number_of_cycles = 0
        self._inter_sample_delay = 0
        self._pre_cycle_delay = 0
        self._post_cycle_delay = 0
        self._output_trigger_start_index = 0
        self._output_trigger_width = 0
        self._number_of_samples_between_trigger_repetition = 0

    @property
    def mode(self) -> TLMC_PZ_OutputWaveformOperatingMode:
        return self._mode

    @mode.setter
    def mode(self, val: TLMC_PZ_OutputWaveformOperatingMode):
        self._mode = val

    @property
    def number_of_samples_per_cycle(self) -> int:
        return self._number_of_samples_per_cycle

    @number_of_samples_per_cycle.setter
    def number_of_samples_per_cycle(self, val: int):
        self._number_of_samples_per_cycle = val

    @property
    def number_of_cycles(self) -> int:
        return self._number_of_cycles

    @number_of_cycles.setter
    def number_of_cycles(self, val: int):
        self._number_of_cycles = val

    @property
    def inter_sample_delay(self) -> int:
        return self._inter_sample_delay

    @inter_sample_delay.setter
    def inter_sample_delay(self, val: int):
        self._inter_sample_delay = val

    @property
    def pre_cycle_delay(self) -> int:
        return self._pre_cycle_delay

    @pre_cycle_delay.setter
    def pre_cycle_delay(self, val: int):
        self._pre_cycle_delay = val

    @property
    def post_cycle_delay(self) -> int:
        return self._post_cycle_delay

    @post_cycle_delay.setter
    def post_cycle_delay(self, val: int):
        self._post_cycle_delay = val

    @property
    def output_trigger_start_index(self) -> int:
        return self._output_trigger_start_index

    @output_trigger_start_index.setter
    def output_trigger_start_index(self, val: int):
        self._output_trigger_start_index = val

    @property
    def output_trigger_width(self) -> int:
        return self._output_trigger_width

    @output_trigger_width.setter
    def output_trigger_width(self, val: int):
        self._output_trigger_width = val

    @property
    def number_of_samples_between_trigger_repetition(self) -> int:
        return self._number_of_samples_between_trigger_repetition

    @number_of_samples_between_trigger_repetition.setter
    def number_of_samples_between_trigger_repetition(self, val: int):
        self._number_of_samples_between_trigger_repetition = val


class TLMC_PZ_PositionLoopParams():
    def __init__(self):
        self._proportional = 0
        self._integral = 0

    @property
    def proportional(self) -> int:
        return self._proportional

    @proportional.setter
    def proportional(self, val: int):
        self._proportional = val

    @property
    def integral(self) -> int:
        return self._integral

    @integral.setter
    def integral(self, val: int):
        self._integral = val


class TLMC_PZ_SlewRateParams():
    def __init__(self):
        self._open_slew_rate = 0
        self._closed_loop_slew_rate = 0

    @property
    def open_slew_rate(self) -> int:
        return self._open_slew_rate

    @open_slew_rate.setter
    def open_slew_rate(self, val: int):
        self._open_slew_rate = val

    @property
    def closed_loop_slew_rate(self) -> int:
        return self._closed_loop_slew_rate

    @closed_loop_slew_rate.setter
    def closed_loop_slew_rate(self, val: int):
        self._closed_loop_slew_rate = val


class TLMC_PZ_StageInfoParams():

    def __init__(self):

        self._product_id = TLMC_PZ_StageProductId.TLMC_PZ_StageProductId_Unknown
        self._stage_name = ""
        self._serial_number = 0
        self._max_voltage = 0
        self._min_negative_voltage = 0
        self._sensor_type = TLMC_PZ_SensorType.TLMC_PZ_SensorType_Unknown
        self._axis_type = TLMC_ConnectedProductAxisType.TLMC_ConnectedProductAxisType_Unknown
        self._nominal_travel = 0
        self._home_position = 0

    @property
    def product_id(self) -> TLMC_PZ_StageProductId:
        return self._product_id

    @product_id.setter
    def product_id(self, val: TLMC_PZ_StageProductId):
        self._product_id = val

    @property
    def stage_name(self) -> str:
        return self._stage_name

    @stage_name.setter
    def stage_name(self, val: str):
        self._stage_name = val

    @property
    def serial_number(self) -> int:
        return self._serial_number

    @serial_number.setter
    def serial_number(self, val: int):
        self._serial_number = val

    @property
    def max_voltage(self) -> int:
        return self._max_voltage

    @max_voltage.setter
    def max_voltage(self, val: int):
        self._max_voltage = val

    @property
    def min_negative_voltage(self) -> int:
        return self._min_negative_voltage

    @min_negative_voltage.setter
    def min_negative_voltage(self, val: int):
        self._min_negative_voltage = val

    @property
    def sensor_type(self) -> TLMC_PZ_SensorType:
        return self._sensor_type

    @sensor_type.setter
    def sensor_type(self, val: TLMC_PZ_SensorType):
        self._sensor_type = val

    @property
    def axis_type(self) -> TLMC_ConnectedProductAxisType:
        return self._axis_type

    @axis_type.setter
    def axis_type(self, val: TLMC_ConnectedProductAxisType):
        self._axis_type = val

    @property
    def nominal_travel(self) -> int:
        return self._nominal_travel

    @nominal_travel.setter
    def nominal_travel(self, val: int):
        self._nominal_travel = val

    @property
    def home_position(self) -> int:
        return self._home_position

    @home_position.setter
    def home_position(self, val: int):
        self._home_position = val


class TLMC_PZ_Status():
    def __init__(self):
        self._output_voltage = 0
        self._position = 0
        self._status_bits = TLMC_PZ_StatusBit.TLMC_PZ_StatusBit_ActuatorConnected

    @property
    def output_voltage(self) -> int:
        return self._output_voltage

    @output_voltage.setter
    def output_voltage(self, val: int) -> None:
        self._output_voltage = val

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, val: int) -> None:
        self._position = val

    @property
    def status_bits(self) -> TLMC_PZ_StatusBit:
        return self._status_bits

    @status_bits.setter
    def status_bits(self, val: TLMC_PZ_StatusBit) -> None:
        self._status_bits = val


class TLMC_StageAxisParams():
    def __init__(self):
        self._type_id = TLMC_StageAxis_TypeId.TLMC_StageAxisType_Unknown
        self._axis_id = TLMC_StageAxis_AxisId.TLMC_StageAxisId_Unknown
        self._part_number = ""
        self._serial_number = 0
        self._counts_per_unit = 0
        self._min_position = 0
        self._max_position = 0
        self._max_acceleration = 0
        self._max_deceleration = 0
        self._max_velocity = 0
        self._gear_box_ratio = 0

    @property
    def type_id(self) -> TLMC_StageAxis_TypeId:
        return self._type_id

    @type_id.setter
    def type_id(self, val: TLMC_StageAxis_TypeId):
        self._type_id = val

    @property
    def axis_id(self) -> TLMC_StageAxis_AxisId:
        return self._axis_id

    @axis_id.setter
    def axis_id(self, val: TLMC_StageAxis_AxisId):
        self._axis_id = val

    @property
    def part_number(self) -> str:
        return self._part_number

    @part_number.setter
    def part_number(self, val: str):
        self._part_number = val

    @property
    def serial_number(self) -> int:
        return self._serial_number

    @serial_number.setter
    def serial_number(self, val: int):
        self._serial_number = val

    @property
    def counts_per_unit(self) -> int:
        return self._counts_per_unit

    @counts_per_unit.setter
    def counts_per_unit(self, val: int):
        self._counts_per_unit = val

    @property
    def min_position(self) -> int:
        return self._min_position

    @min_position.setter
    def min_position(self, val: int):
        self._min_position = val

    @property
    def max_position(self) -> int:
        return self._max_position

    @max_position.setter
    def max_position(self, val: int):
        self._max_position = val

    @property
    def max_acceleration(self) -> int:
        return self._max_acceleration

    @max_acceleration.setter
    def max_acceleration(self, val: int):
        self._max_acceleration = val

    @property
    def max_deceleration(self) -> int:
        return self._max_deceleration

    @max_deceleration.setter
    def max_deceleration(self, val: int):
        self._max_deceleration = val

    @property
    def max_velocity(self) -> int:
        return self._max_velocity

    @max_velocity.setter
    def max_velocity(self, val: int):
        self._max_velocity = val

    @property
    def gear_box_ratio(self) -> int:
        return self._gear_box_ratio

    @gear_box_ratio.setter
    def gear_box_ratio(self, val: int):
        self._gear_box_ratio = val


class TLMC_TriggerParamsForStepper():
    def __init__(self):
        self._modes = TLMC_TriggerModesForStepper.TLMC_TriggerModesForStepper_None

    @property
    def modes(self) -> TLMC_TriggerModesForStepper:
        return self._modes

    @modes.setter
    def modes(self, val: TLMC_TriggerModesForStepper):
        self._modes = val


class TLMC_StepperLoopParams():
    def __init__(self):
        self._loop_mode = TLMC_StepperLoopParams_LoopMode.TLMC_StepperLoopParams_LoopMode_Open
        self._proportional = 0
        self._integral = 0
        self._differential = 0
        self._output_clip = 0
        self._output_tolerance = 0
        self._microsteps_per_encoder_count = 0

    @property
    def loop_mode(self) -> TLMC_StepperLoopParams_LoopMode:
        return self._loop_mode

    @loop_mode.setter
    def loop_mode(self, val: TLMC_StepperLoopParams_LoopMode):
        self._loop_mode = val

    @property
    def proportional(self) -> int:
        return self._proportional

    @proportional.setter
    def proportional(self, val: int):
        self._proportional = val

    @property
    def integral(self) -> int:
        return self._integral

    @integral.setter
    def integral(self, val: int):
        self._integral = val

    @property
    def differential(self) -> int:
        return self._differential

    @differential.setter
    def differential(self, val: int):
        self._differential = val

    @property
    def output_clip(self) -> int:
        return self._output_clip

    @output_clip.setter
    def output_clip(self, val: int):
        self._output_clip = val

    @property
    def output_tolerance(self) -> int:
        return self._output_tolerance

    @output_tolerance.setter
    def output_tolerance(self, val: int):
        self._output_tolerance = val

    @property
    def microsteps_per_encoder_count(self) -> int:
        return self._microsteps_per_encoder_count

    @microsteps_per_encoder_count.setter
    def microsteps_per_encoder_count(self, val: int):
        self._microsteps_per_encoder_count = val


class TLMC_StepperStatus():
    def __init__(self):
        self._position = 0
        self._encoder_count = 0
        self._status_bits = TLMC_UniversalStatusBit.TLMC_UniversalStatusBit_ClockwiseHardLimit

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, val: int):
        self._position = val

    @property
    def encoder_count(self) -> int:
        return self._encoder_count

    @encoder_count.setter
    def encoder_count(self, val: int):
        self._encoder_count = val

    @property
    def status_bits(self) -> TLMC_UniversalStatusBit:
        return self._status_bits

    @status_bits.setter
    def status_bits(self, val: TLMC_UniversalStatusBit):
        self._status_bits = val


class TLMC_AdcInputs():
    def __init__(self):
        self._adc_input_1 = 0
        self._adc_input_2 = 0

    @property
    def adc_input_1(self) -> int:
        return self._adc_input_1

    @adc_input_1.setter
    def adc_input_1(self, val: int):
        self._adc_input_1 = val

    @property
    def adc_input_2(self) -> int:
        return self._adc_input_2

    @adc_input_2.setter
    def adc_input_2(self, val: int):
        self._adc_input_2 = val


class TLMC_CurrentLoopParams():
    def __init__(self):
        self._phase = TLMC_CurrentLoopPhase.TLMC_CurrentLoopPhase_A
        self._proportional = 0
        self._integral = 0
        self._integral_limit = 0
        self._integral_dead_band = 0
        self._feed_forward = 0

    @property
    def phase(self) -> TLMC_CurrentLoopPhase:
        return self._phase

    @phase.setter
    def phase(self, val: TLMC_CurrentLoopPhase):
        self._phase = val

    @property
    def proportional(self) -> int:
        return self._proportional

    @proportional.setter
    def proportional(self, val: int):
        self._proportional = val

    @property
    def integral(self) -> int:
        return self._integral

    @integral.setter
    def integral(self, val: int):
        self._integral = val

    @property
    def integral_limit(self) -> int:
        return self._integral_limit

    @integral_limit.setter
    def integral_limit(self, val: int):
        self._integral_limit = val

    @property
    def integral_dead_band(self) -> int:
        return self._integral_dead_band

    @integral_dead_band.setter
    def integral_dead_band(self, val: int):
        self._integral_dead_band = val

    @property
    def feed_forward(self) -> int:
        return self._feed_forward

    @feed_forward.setter
    def feed_forward(self, val: int):
        self._feed_forward = val


class TLMC_PotentiometerParams:
    def __init__(self):
        self._deflection_0 = 0
        self._velocity_1 = 0
        self._deflection_1 = 0
        self._velocity_2 = 0
        self._deflection_2 = 0
        self._velocity_3 = 0
        self._deflection_3 = 0
        self._velocity_4 = 0

    @property
    def deflection_0(self) -> int:
        return self._deflection_0

    @deflection_0.setter
    def deflection_0(self, val: int):
        self._deflection_0 = val  

    @property
    def velocity_1(self) -> int:
        return self._velocity_1

    @velocity_1.setter
    def velocity_1(self, val: int):
        self._velocity_1 = val

    @property
    def deflection_1(self) -> int:
        return self._deflection_1

    @deflection_1.setter
    def deflection_1(self, val: int):
        self._deflection_1 = val

    @property
    def velocity_2(self) -> int:
        return self._velocity_2

    @velocity_2.setter
    def velocity_2(self, val: int):
        self._velocity_2 = val

    @property
    def deflection_2(self) -> int:
        return self._deflection_2

    @deflection_2.setter
    def deflection_2(self, val: int):
        self._deflection_2 = val

    @property
    def velocity_3(self) -> int:
        return self._velocity_3

    @velocity_3.setter
    def velocity_3(self, val: int):
        self._velocity_3 = val

    @property
    def deflection_3(self) -> int:
        return self._deflection_3

    @deflection_3.setter
    def deflection_3(self, val: int):
        self._deflection_3 = val

    @property
    def velocity_4(self) -> int:
        return self._velocity_4

    @velocity_4.setter
    def velocity_4(self, val: int):
        self._velocity_4 = val


class TLMC_PowerParams():
    def __init__(self):
        self._rest_factor = 0
        self._move_factor = 0

    @property
    def rest_factor(self) -> int:
        return self._rest_factor

    @rest_factor.setter
    def rest_factor(self, val: int):
        self._rest_factor = val

    @property
    def move_factor(self) -> int:
        return self._move_factor

    @move_factor.setter
    def move_factor(self, val: int):
        self._move_factor = val


class TLMC_ProfileModeParams():
    def __init__(self):
        self._mode = TLMC_ProfileMode.TLMC_ProfileMode_Trapezoidal
        self._jerk = 0

    @property
    def mode(self) -> TLMC_ProfileMode:
        return self._mode
    
    @mode.setter
    def mode(self, val: TLMC_ProfileMode):
        self._mode = val

    @property
    def jerk(self) -> int:
        return self._jerk
    
    @jerk.setter
    def jerk(self, val: int):
        self._jerk = val


class TLMC_RichResponse():
    def __init__(self):
        self._message_id = 0
        self._code = 0
        self._notes = ""

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, val: int):
        self._message_id = val

    @property
    def code(self) -> int:
        return self._code

    @code.setter
    def code(self, val: int):
        self._code = val

    @property
    def notes(self) -> str:
        return self._notes

    @notes.setter
    def notes(self, val: str):
        self._notes = val


class TLMC_Setting():
    def __init__(self):
        self._value_type = 0
        self._is_value_set = False
        self._value = 0
        self._scale_type = 0
        self._unit_type = 0
        self._name = ""
        self._display_name = ""
        self._is_read_only = False
        self._has_discrete_values = False
        self._has_min = False
        self._has_max = False
        self._min_value = 0
        self._max_value = 0

    @property
    def value_type(self) -> int:
        return self._value_type

    @value_type.setter
    def value_type(self, val: int) -> None:
        self._value_type = val

    @property
    def is_value_set(self) -> bool:
        return self._is_value_set

    @is_value_set.setter
    def is_value_set(self, val: bool) -> None:
        self._is_value_set = val

    @property
    def value(self) -> int | bool | str | float:
        return self._value

    @value.setter
    def value(self, val: int | bool | str | float) -> None:
        self._value = val

    @property
    def scale_type(self) -> int:
        return self._scale_type

    @scale_type.setter
    def scale_type(self, val: int) -> None:
        self._scale_type = val

    @property
    def unit_type(self) -> int:
        return self._unit_type

    @unit_type.setter
    def unit_type(self, val: int) -> None:
        self._unit_type = val

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str) -> None:
        self._name = val

    @property
    def display_name(self) -> str:
        return self._display_name

    @display_name.setter
    def display_name(self, val: str) -> None:
        self._display_name = val

    @property
    def is_read_only(self) -> bool:
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, val: bool) -> None:
        self._is_read_only = val

    @property
    def has_discrete_values(self) -> bool:
        return self._has_discrete_values

    @has_discrete_values.setter
    def has_discrete_values(self, val: bool) -> None:
        self._has_discrete_values = val

    @property
    def has_min(self) -> bool:
        return self._has_min

    @has_min.setter
    def has_min(self, val: bool) -> None:
        self._has_min = val

    @property
    def has_max(self) -> bool:
        return self._has_max

    @has_max.setter
    def has_max(self, val: bool) -> None:
        self._has_max = val

    @property
    def min_value(self) -> int:
        return self._min_value

    @min_value.setter
    def min_value(self, val: int) -> None:
        self._min_value = val

    @property
    def max_value(self) -> int:
        return self._max_value

    @max_value.setter
    def max_value(self, val: int) -> None:
        self._max_value = val


class TLMC_StatusItem():
    def __init__(self):
        self._id = TLMC_StatusItemId.TLMC_StatusItemId_Active
        self._value_type = TLMC_ValueType.TLMC_ValueType_int64
        self._value = 0

    @property
    def id(self) -> TLMC_StatusItemId:
        return self._id

    @id.setter
    def id(self, val: TLMC_StatusItemId) -> None:
        self._id = val

    @property
    def value_type(self) -> TLMC_ValueType:
        return self._value_type

    @value_type.setter
    def value_type(self, val: TLMC_ValueType) -> None:
        self._value_type = val

    @property
    def value(self) -> int | bool | str | float:
        return self._value

    @value.setter
    def value(self, val: int | bool | str | float) -> None:
        self._value = val


class TLMC_TrackSettleParams():
    def __init__(self):
        self._settle_time = 0
        self._settle_window = 0
        self._track_window = 0

    @property
    def settle_time(self) -> int:
        return self._settle_time

    @settle_time.setter
    def settle_time(self, val: int):
        self._settle_time = val

    @property
    def settle_window(self) -> int:
        return self._settle_window

    @settle_window.setter
    def settle_window(self, val: int):
        self._settle_window = val

    @property
    def track_window(self) -> int:
        return self._track_window

    @track_window.setter
    def track_window(self, val: int):
        self._track_window = val


class TLMC_UniversalStatus():
    def __init__(self):
        self._position = 0
        self._velocity = 0
        self._motor_current = 0
        self._status_bits = 0

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, val: int):
        self._position = val

    @property
    def velocity(self) -> int:
        return self._velocity

    @velocity.setter
    def velocity(self, val: int):
        self._velocity = val

    @property
    def motor_current(self) -> int:
        return self._motor_current

    @motor_current.setter
    def motor_current(self, val: int):
        self._motor_current = val

    @property
    def status_bits(self) -> int:
        return self._status_bits

    @status_bits.setter
    def status_bits(self, val: int):
        self._status_bits = val
    

class TLMC_Value():
    def __init__(self):
        self._value = 0

    @property
    def value(self) -> int | str | bool:
        return self._value
    
    @value.setter
    def value(self, val: int | str | bool):
        self._value = val


class TLMC_VelocityParams():
    def __init__(self):
        self._min_velocity = 0
        self._acceleration = 0
        self._max_velocity = 0

    @property
    def min_velocity(self) -> int:
        return self._min_velocity

    @min_velocity.setter
    def min_velocity(self, val: int):
        self._min_velocity = val

    @property
    def acceleration(self) -> int:
        return self._acceleration

    @acceleration.setter
    def acceleration(self, val: int):
        self._acceleration = val

    @property
    def max_velocity(self) -> int:
        return self._max_velocity

    @max_velocity.setter
    def max_velocity(self, val: int):
        self._max_velocity = val
