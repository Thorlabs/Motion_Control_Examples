from enum import IntEnum, IntFlag, auto

class TLMC_AnalogMonitorMotorChannel(IntEnum):
    TLMC_AnalogMonitorMotorChannel_1 = 0x0001
    TLMC_AnalogMonitorMotorChannel_2 = 0x0002


class TLMC_AnalogMonitorNumber(IntEnum):
    TLMC_AnalogueMonitorNumber_1 = 0x0001
    TLMC_AnalogueMonitorNumber_2 = 0x0002


class TLMC_AnalogMonitorSystemVariable(IntEnum):
    TLMC_AnalogMonitorSystemVariable_PositionError = 0x0001
    TLMC_AnalogMonitorSystemVariable_Position = 0x0002
    TLMC_AnalogMonitorSystemVariable_MotorCurrentPhaseA = 0x0003
    TLMC_AnalogMonitorSystemVariable_MotorCurrentPhaseB = 0x0004
    TLMC_AnalogMonitorSystemVariable_MotorCurrentPhaseC = 0x0005
    TLMC_AnalogMonitorSystemVariable_MotorCurrent = 0x0006


class TLMC_AuxIoPortMode(IntEnum):
    TLMC_AuxIoPortMode_None = 0x0000
    TLMC_AuxIoPortMode_SoftwareControlled = 0x0001
    TLMC_AuxIoPortMode_EncoderOutput = 0x0002


class TLMC_AuxIoPortNumber(IntEnum):
    TLMC_AuxIoPortNumber_None = 0x0000
    TLMC_AuxIoPortNumber_Port1 = 0x0001
    TLMC_AuxIoPortNumber_Port2 = 0x0002
    TLMC_AuxIoPortNumber_Port3 = 0x0004


class TLMC_ButtonMode(IntEnum):

    TLMC_ButtonMode_Jog = 0x0001
    TLMC_ButtonMode_PresetPosition = 0x0002


class TLMC_BowIndex(IntEnum):
    TLMC_BowIndex_Trapezoidal = 0
    TLMC_BowIndex_SCurve1 = 1
    TLMC_BowIndex_SCurve2 = 2
    TLMC_BowIndex_SCurve3 = 3
    TLMC_BowIndex_SCurve4 = 4
    TLMC_BowIndex_SCurve5 = 5
    TLMC_BowIndex_SCurve6 = 6
    TLMC_BowIndex_SCurve7 = 7
    TLMC_BowIndex_SCurve8 = 8
    TLMC_BowIndex_SCurve9 = 9
    TLMC_BowIndex_SCurve10 = 10
    TLMC_BowIndex_SCurve11 = 11
    TLMC_BowIndex_SCurve12 = 12
    TLMC_BowIndex_SCurve13 = 13
    TLMC_BowIndex_SCurve14 = 14
    TLMC_BowIndex_SCurve15 = 15
    TLMC_BowIndex_SCurve16 = 16
    TLMC_BowIndex_SCurve17 = 17
    TLMC_BowIndex_SCurve18 = 18


class TLMC_CalibrationState(IntEnum):
    TLMC_CalibrationState_Unknown = 0x00
    TLMC_CalibrationState_FileNotPresent = 0x01
    TLMC_CalibrationState_Active = 0x02
    TLMC_CalibrationState_Inactive = 0x03


class TLMC_ChannelEnableStates(IntEnum):
    ChannelEnabled = 0x01
    ChannelDisabled = 0x02


class TLMC_ConnectedProductAxisType(IntEnum):
    TLMC_ConnectedProductAxisType_Unknown = 0
    TLMC_ConnectedProductAxisType_Single = 1
    TLMC_ConnectedProductAxisType_Rotary = 2
    TLMC_ConnectedProductAxisType_X = 3
    TLMC_ConnectedProductAxisType_Y = 4
    TLMC_ConnectedProductAxisType_Z = 5
    TLMC_ConnectedProductAxisType_Pitch = 6
    TLMC_ConnectedProductAxisType_Roll = 7
    TLMC_ConnectedProductAxisType_Yaw = 8
    TLMC_ConnectedProductAxisType_Goniometer = 9


class TLMC_ConnectedProductMovementType(IntEnum):
    TLMC_ConnectedProductMovementType_Unknown = 0
    TLMC_ConnectedProductMovementType_Linear = 1
    TLMC_ConnectedProductMovementType_RotaryContinuous = 2
    TLMC_ConnectedProductMovementType_RotaryFixedRange = 3


class TLMC_ConversionMeasure(IntEnum):
    TLMC_ConversionMeasure_Distance = 0x0000
    TLMC_ConversionMeasure_Velocity = 0x0001
    TLMC_ConversionMeasure_Acceleration = 0x0002


class TLMC_CurrentLoopPhase(IntEnum):
    TLMC_CurrentLoopPhase_A = 0x0000
    TLMC_CurrentLoopPhase_B = 0x0001
    TLMC_CurrentLoopPhase_AB = 0x0002


class TLMC_CurrentLoopScenario(IntEnum):
    TLMC_CurrentLoopScenario_Single = 0x0000
    TLMC_CurrentLoopScenario_Normal = 0x0001
    TLMC_CurrentLoopScenario_Settled = 0x0002


class TLMC_DcPidUpdateFilter(IntFlag):
    TLMC_DcPidUpdateFilter_None = 0x0000
    TLMC_DcPidUpdateFilter_IntegralLimit = 0x0001
    TLMC_DcPidUpdateFilter_Derivative = 0x0002
    TLMC_DcPidUpdateFilter_Integral = 0x0004
    TLMC_DcPidUpdateFilter_Proportional = 0x0008
    TLMC_DcPidUpdateFilter_All = (TLMC_DcPidUpdateFilter_IntegralLimit
                                  | TLMC_DcPidUpdateFilter_Derivative
                                  | TLMC_DcPidUpdateFilter_Integral
                                  | TLMC_DcPidUpdateFilter_Proportional)


class TLMC_DeviceFamily(IntEnum):
    TLMC_DeviceFamily_ThorlabsMotionControl = 0


class TLMC_DeviceType(IntEnum):
    TLMC_DeviceType_Bbd30xBaseUnit = 0
    TLMC_DeviceType_Bbd30xLogicalChannel = 1
    TLMC_DeviceType_Bpc301 = 2
    TLMC_DeviceType_Bpc30xBaseUnit = 3
    TLMC_DeviceType_Bpc30xLogicalChannel = 4
    TLMC_DeviceType_Bsc20xBaseUnit = 5
    TLMC_DeviceType_Bsc20xLogicalChannel = 6
    TLMC_DeviceType_Kbd101 = 7
    TLMC_DeviceType_Kdc101 = 8
    TLMC_DeviceType_Kpz101 = 9
    TLMC_DeviceType_Kst101 = 10
    TLMC_DeviceType_Kst201 = 11
    TLMC_DeviceType_Tbd001 = 12
    TLMC_DeviceType_LinearTranslationStage = 13
    TLMC_DeviceType_Bsc20xv4LogicalChannel = 14
    TLMC_DeviceType_Bsc201 = 15
    TLMC_DeviceType_Bsc201v4 = 16
    TLMC_DeviceType_Kpc101 = 17
    TLMC_DeviceType_Pdxc2 = 18
    TLMC_DeviceType_Pdxc3 = 19
    TLMC_DeviceType_Kna101 = 20
    TLMC_DeviceType_LnnxBaseUnit = 21
    TLMC_DeviceType_LnnxLogicalChannel = 22


class TLMC_DeviceListChange(IntEnum):
    TLMC_DeviceListChange_EntryAdded = 0
    TLMC_DeviceListChange_EntryRemoved = 1


class TLMC_DigitalInput(IntFlag):
    TLMC_DigitalInput_None = 0x00000000
    TLMC_DigitalInput_1 = 0x00000001
    TLMC_DigitalInput_2 = 0x00000002
    TLMC_DigitalInput_3 = 0x00000004
    TLMC_DigitalInput_4 = 0x00000008
    TLMC_DigitalInput_All = (TLMC_DigitalInput_1
                             | TLMC_DigitalInput_2
                             | TLMC_DigitalInput_3
                             | TLMC_DigitalInput_4)


class TLMC_DigitalOutput(IntFlag):
    TLMC_DigitalOutput_None = 0x00
    TLMC_DigitalOutput_1 = 0x01
    TLMC_DigitalOutput_2 = 0x02
    TLMC_DigitalOutput_3 = 0x04
    TLMC_DigitalOutput_4 = 0x08
    TLMC_DigitalOutput_All = (TLMC_DigitalOutput_1
                              | TLMC_DigitalOutput_2
                              | TLMC_DigitalOutput_3
                              | TLMC_DigitalOutput_4)


class TLMC_EnableState(IntEnum):
    TLMC_Enabled = 0x01
    TLMC_Disabled = 0x02


class TLMC_EndOfMoveMessagesMode(IntEnum):
    TLMC_EndOfMoveMessagesMode_Enabled = 0x01
    TLMC_EndOfMoveMessagesMode_Disabled = 0x02


class TLMC_HardLimitOperatingMode(IntEnum):
    TLMC_HardLimitOperatingMode_SwitchIgnored = 0x0001
    TLMC_HardLimitOperatingMode_SwitchContactMakes = 0x0002
    TLMC_HardLimitOperatingMode_SwitchContactBreaks = 0x0003
    TLMC_HardLimitOperatingMode_SwitchContactMakesWhenHoming = 0x0004
    TLMC_HardLimitOperatingMode_SwitchContactBreaksWhenHoming = 0x0005
    TLMC_HardLimitOperatingMode_SwitchUseIndexMarkForHoming = 0x0006
    TLMC_HardLimitOperatingMode_SwitchesSwapped = 0x0080


class TLMC_HomeDirection(IntEnum):
    TLMC_HomeDirection_Forward = 0x0001
    TLMC_HomeDirection_Reverse = 0x0002


class TLMC_HomeLimitSwitch(IntEnum):
    TLMC_HomeLimitSwitch_Reverse = 0x0001
    TLMC_HomeLimitSwitch_Forward = 0x0004


class TLMC_IoPortMode(IntEnum):
    TLMC_IoPortMode_DigitalInput = 0x0000
    TLMC_IoPortMode_DigitalOutput = 0x0001
    TLMC_IoPortMode_AnalogOutput = 0x0002


class TLMC_IoPortNumber(IntEnum):
    TLMC_IoPortNumber_Port1 = 0x0001
    TLMC_IoPortNumber_Port2 = 0x0002
    TLMC_IoPortNumber_Port3 = 0x0003


class TLMC_IoPortSource(IntEnum):
    TLMC_IoPortSource_Software = 0x0000
    TLMC_IoPortSource_Channel1 = 0x0001
    TLMC_IoPortSource_Channel2 = 0x0002
    TLMC_IoPortSource_Channel3 = 0x0003


class TLMC_IoPositionTriggerEnableState(IntEnum):
    TLMC_IoPositionTriggerEnableState_Armed = 0x01
    TLMC_IoPositionTriggerEnableState_Canceled = 0x02


class TLMC_IoTriggerInMode(IntEnum):
    TLMC_IoTriggerInMode_Disabled = 0x0000
    TLMC_IoTriggerInMode_GeneralPurpose = 0x0001
    TLMC_IoTriggerInMode_TriggersRelativeMove = 0x0002
    TLMC_IoTriggerInMode_TriggersAbsoluteMove = 0x0003
    TLMC_IoTriggerInMode_TriggersHomeMove = 0x0004


class TLMC_IoTriggerInSource(IntEnum):
    TLMC_IoTriggerInSource_Software = 0x0000
    TLMC_IoTriggerInSource_BNC1 = 0x0001
    TLMC_IoTriggerInSource_BNC2 = 0x0002
    TLMC_IoTriggerInSource_BNC3 = 0x0003


class TLMC_IoTriggerOutMode(IntEnum):
    TLMC_IoTriggerOutMode_GeneralPurpose = 0x000A
    TLMC_IoTriggerOutMode_ActiveDuringMotion = 0x000B
    TLMC_IoTriggerOutMode_ActiveAtMaxVelocity = 0x000C
    TLMC_IoTriggerOutMode_PulsedInForwardDirection = 0x000D
    TLMC_IoTriggerOutMode_PulsedInReverseDirection = 0x000E
    TLMC_IoTriggerOutMode_PulsedInBothDirections = 0x000F
    TLMC_IoTriggerOutMode_ActiveAtForwardLimit = 0x0010
    TLMC_IoTriggerOutMode_ActiveAtReverseLimit = 0x0011
    TLMC_IoTriggerOutMode_ActiveAtBothLimits = 0x0012


class TLMC_IoTriggerPolarity(IntEnum):
    TLMC_IoTriggerPolarity_ActiveIsLogicHigh = 0x0001
    TLMC_IoTriggerPolarity_ActiveIsLogicLow = 0x0002


class TLMC_IoTriggerPortNumber(IntFlag):
    TLMC_IoTriggerPortNumber_None = 0x0000
    TLMC_IoTriggerPortNumber_Port1 = 0x0001
    TLMC_IoTriggerPortNumber_Port2 = 0x0002
    TLMC_IoTriggerPortNumber_Port3 = 0x0004
    TLMC_IoTriggerPortNumber_Port4 = 0x0008
    TLMC_IoTriggerPortNumber_Port5 = 0x0010
    TLMC_IoTriggerPortNumber_Port6 = 0x0020
    TLMC_IoTriggerPortNumber_Port7 = 0x0040


class TLMC_JogMode(IntEnum):
    TLMC_JogMode_Continuous = 0x0001
    TLMC_JogMode_SingleStep = 0x0002


class TLMC_JogStopMode(IntEnum):
    TLMC_JogStopMode_Immediate = 0x0001
    TLMC_JogStopMode_Profiled = 0x0002


class TLMC_JoystickAxis(IntEnum):
    TLMC_JoystickAxis_Unspecified = 0
    TLMC_JoystickAxis_X = 1
    TLMC_JoystickAxis_Y = 2
    TLMC_JoystickAxis_Z = 3


class TLMC_JoystickDirectionSense(IntEnum):
    TLMC_JoystickDirectionSense_Disabled = 0x0000
    TLMC_JoystickDirectionSense_Positive = 0x0001
    TLMC_JoystickDirectionSense_Negative = 0x0002


class TLMC_JoystickModel(IntEnum):
    TLMC_JoystickModel_NotSelected = 0
    TLMC_JoystickModel_MJC1 = 1
    TLMC_JoystickModel_MJC2 = 2
    TLMC_JoystickModel_MJC3 = 3
    TLMC_JoystickModel_MCMJ1 = 128
    TLMC_JoystickModel_MCMK1 = 129
    TLMC_JoystickModel_MCMK4 = 130
    TLMC_JoystickModel_MCMK3 = 131


class TLMC_JoystickSerialInterface(IntEnum):
    TLMC_JoystickSerialInterface_Disabled = 0
    TLMC_JoystickSerialInterface_SerialJoystick = 1
    TLMC_JoystickSerialInterface_Master = 2


class TLMC_KcubeIoTriggerMode(IntEnum):
    TLMC_KcubeIoTriggerMode_Disabled = 0x0000
    TLMC_KcubeIoTriggerMode_GeneralPurposeInput = 0x0001
    TLMC_KcubeIoTriggerMode_InputTriggersRelativeMove = 0x0002
    TLMC_KcubeIoTriggerMode_InputTriggersAbsoluteMove = 0x0003
    TLMC_KcubeIoTriggerMode_InputTriggersHomeMove = 0x0004
    TLMC_KcubeIoTriggerMode_GeneralPurposeOutput = 0x000A
    TLMC_KcubeIoTriggerMode_OutputActiveDuringMotion = 0x000B
    TLMC_KcubeIoTriggerMode_OutputActiveAtMaxVelocity = 0x000C
    TLMC_KcubeIoTriggerMode_OutputPulsedInForwardDirection = 0x000D
    TLMC_KcubeIoTriggerMode_OutputPulsedInReverseDirection = 0x000E
    TLMC_KcubeIoTriggerMode_OutputPulsedInBothDirections = 0x000F


class TLMC_KcubeIoTriggerPolarity(IntEnum):
    TLMC_KcubeIoTriggerPolarity_ActiveIsLogicHigh = 0x0001
    TLMC_KcubeIoTriggerPolarity_ActiveIsLogicLow = 0x0002


class TLMC_KcubeMmi_JoystickDirectionSense(IntEnum):
    TLMC_KcubeMmi_JoystickDirectionSense_Disabled = 0x0000
    TLMC_KcubeMmi_JoystickDirectionSense_Normal = 0x0001
    TLMC_KcubeMmi_JoystickDirectionSense_Inverted = 0x0002

    
class TLMC_KcubeMmi_JoystickGear(IntEnum):
    TLMC_KcubeMmiJoystickGear_High = 0x0001
    TLMC_KcubeMmiJoystickGear_Medium = 0x0002
    TLMC_KcubeMmiJoystickGear_Low = 0x0003


class TLMC_KcubeMmi_JoystickMode(IntEnum):
    TLMC_KcubeMmi_JoystickMode_ControlsVelocity = 0x0001
    TLMC_KcubeMmi_JoystickMode_Jogs = 0x0002
    TLMC_KcubeMmi_JoystickMode_GoesToPosition = 0x0003


class TLMC_KcubeMmiLockState(IntEnum):
    TLMC_KcubeMmiLockState_Locked = 0x01
    TLMC_KcubeMmiLockState_Unlocked = 0x02


class TLMC_PZ_KpcIoTriggerMode(IntEnum):
    TLMC_PZ_KpcIoTriggerMode_Disabled = 0x0000
    TLMC_PZ_KpcIoTriggerMode_GeneralPurposeInput = 0x0001
    TLMC_PZ_KpcIoTriggerMode_InputTriggersVoltagePositionStepUp = 0x0002
    TLMC_PZ_KpcIoTriggerMode_InputTriggersVoltagePositionStepDown = 0x0003
    TLMC_PZ_KpcIoTriggerMode_GeneralPurposeOutput = 0x000A
    TLMC_PZ_KpcIoTriggerMode_OutputActiveStrainGaugeLessThanLowerLimit = 0x000B
    TLMC_PZ_KpcIoTriggerMode_OutputActiveStrainGaugeMoreThanLowerLimit = 0x000C
    TLMC_PZ_KpcIoTriggerMode_OutputActiveStrainGaugeLessThanUpperLimit = 0x000D
    TLMC_PZ_KpcIoTriggerMode_OutputActiveStrainGaugeMoreThanUpperLimit = 0x000E
    TLMC_PZ_KpcIoTriggerMode_OutputActiveStrainGaugeWithinLimits = 0x000F


class TLMC_PZ_KpcMonitorOutputMode(IntEnum):
    TLMC_PZ_KpcMonitorOutputMode_Software = 0x0000
    TLMC_PZ_KpcMonitorOutputMode_HighVoltage = 0x0001
    TLMC_PZ_KpcMonitorOutputMode_Position = 0x0002


class TLMC_PZ_KpcMmi_JoystickDirectionSense(IntEnum):
    TLMC_PZ_KpcMmiJoystickDirectionSense_Disabled = 0x0000
    TLMC_PZ_KpcMmiJoystickDirectionSense_Normal = 0x0001
    TLMC_PZ_KpcMmiJoystickDirectionSense_Invert = 0x0002


class TLMC_PZ_KpcMmi_JoystickMode(IntEnum):
    TLMC_PZ_KpcMmiJoystickMode_ControlsVoltagePosition = 0x0001
    TLMC_PZ_KpcMmiJoystickMode_Jogs = 0x0002
    TLMC_PZ_KpcMmiJoystickMode_GoesToVoltagePosition = 0x0003


class TLMC_PZ_KpcAnalogInputSource(IntEnum):
    TLMC_PZ_KpcAnalogInputSource_Disabled = 0x0000
    TLMC_PZ_KpcAnalogInputSource_HubInputA = 0x0001
    TLMC_PZ_KpcAnalogInputSource_HubInputB = 0x0002
    TLMC_PZ_KpcAnalogInputSource_External = 0x0003


class TLMC_PZ_KpcStrainGaugeOption(IntEnum):
    TLMC_PZ_KpcStrainGaugeOption_Position = 0x0000
    TLMC_PZ_KpcStrainGaugeOption_Force = 0x0001


class TLMC_PZ_KpcVoltageRange(IntEnum):
    TLMC_PZ_KpcVoltageRange_75Volts = 0x4B
    TLMC_PZ_KpcVoltageRange_150Volts = 0x96


class TLMC_PZ_LnnxControlLoopParamsOverrideMode(IntFlag):
    TLMC_PZ_LnnxControlLoopParamsOverrideMode_FromStage = 0
    TLMC_PZ_LnnxControlLoopParamsOverrideMode_Override = 4


class TLMC_PZ_LnnxNotchFilterParamsOverrideMode(IntFlag):
    TLMC_PZ_LnnxNotchFilterParamsOverrideMode_FromStage = 0
    TLMC_PZ_LnnxNotchFilterParamsOverrideMode_Filter1Disabled = 1
    TLMC_PZ_LnnxNotchFilterParamsOverrideMode_Filter2Disabled = 2
    TLMC_PZ_LnnxNotchFilterParamsOverrideMode_Override = 4


class TLMC_PZ_NanoTrakCircleDiameterMode(IntEnum):
    TLMC_PZ_NanoTrakCircleDiameterModes_Software = 0x0001
    TLMC_PZ_NanoTrakCircleDiameterModes_AbsolutePower = 0x0002
    TLMC_PZ_NanoTrakCircleDiameterModes_Lut = 0x0003


class TLMC_PZ_NanoTrakAbsolutePowerAdjustType(IntEnum):
    TLMC_PZ_NanoTrakAbsolutePowerAdjustType_LIN = 0x0001
    TLMC_PZ_NanoTrakAbsolutePowerAdjustType_LOG = 0x0002
    TLMC_PZ_NanoTrakAbsolutePowerAdjustType_X2 = 0x0003
    TLMC_PZ_NanoTrakAbsolutePowerAdjustType_X3 = 0x0004


class TLMC_PZ_NanoTrakFeedbackSource(IntEnum):
    TLMC_PZ_NanoTrakFeedbackSource_TiaInput = 0x01
    TLMC_PZ_NanoTrakFeedbackSource_ExternalInput1V = 0x02
    TLMC_PZ_NanoTrakFeedbackSource_ExternalInput2V = 0x03
    TLMC_PZ_NanoTrakFeedbackSource_ExternalInput5V = 0x04
    TLMC_PZ_NanoTrakFeedbackSource_ExternalInput10V = 0x05


class TLMC_PZ_NanoTrakGainControlMode(IntEnum):
    TLMC_PZ_NanoTrakGainControlMode_Software = 0x02


class TLMC_PZ_NanoTrakTrackingState(IntEnum):
    TLMC_PZ_NanoTrakTrackingState_ModeUndefined = 0
    TLMC_PZ_NanoTrakTrackingState_TrackingOff = 1
    TLMC_PZ_NanoTrakTrackingState_LatchMode = 2
    TLMC_PZ_NanoTrakTrackingState_NoSignal = 3
    TLMC_PZ_NanoTrakTrackingState_Signal = 4


class TLMC_PZ_NanoTrakTrackingMode(IntEnum):
    TLMC_PZ_NanoTrakTrackingMode_DualAxisTracking = 1
    TLMC_PZ_NanoTrakTrackingMode_HorizontalAxisTracking = 2
    TLMC_PZ_NanoTrakTrackingMode_VerticalAxisTracking = 3


class TLMC_PZ_NanoTrakPhaseCompensationMode(IntEnum):
    TLMC_PZ_NanoTrakPhaseCompensationMode_Manual = 0x0002


class TLMC_PZ_NanoTrakRangeMode(IntEnum):
    TLMC_PZ_NanoTrakRangeMode_Auto = 0x0001
    TLMC_PZ_NanoTrakRangeMode_Software = 0x0002
    TLMC_PZ_NanoTrakRangeMode_SoftwareSet = 0x0003
    TLMC_PZ_NanoTrakRangeMode_AutoSet = 0x0004


class TLMC_PZ_NanoTrakRangeChangeType(IntEnum):
    TLMC_PZ_NanoTrakRangeChangeType_All = 0x0001
    TLMC_PZ_NanoTrakRangeChangeType_Odd = 0x0002
    TLMC_PZ_NanoTrakRangeChangeType_Even = 0x0004


class TLMC_PZ_SensorType(IntEnum):
    TLMC_PZ_SensorType_Unknown = 0xFF
    TLMC_PZ_SensorType_StrainGauge = 0
    TLMC_PZ_SensorType_Capacitive = 1
    TLMC_PZ_SensorType_Optical = 2
    TLMC_PZ_SensorType_DirectCurrentFuture = 3
    TLMC_PZ_SensorType_QuadratureEncoder = 4


class TLMC_PZ_StageProductId(IntEnum):
    TLMC_PZ_StageProductId_Unknown = 0
    TLMC_PZ_StageProductId_PGM100 = 100
    TLMC_PZ_StageProductId_PSF200 = 200
    TLMC_PZ_StageProductId_MAX400 = 400
    TLMC_PZ_StageProductId_PFM450 = 450
    TLMC_PZ_StageProductId_LPS710 = 710


class TLMC_PZ_SetNanoTrakModeType(IntEnum):
    TLMC_PZ_SetNanoTrakModeType_PiezoMode = 1
    TLMC_PZ_SetNanoTrakModeType_LatchMode = 2
    TLMC_PZ_SetNanoTrakModeType_TrackMode = 3
    TLMC_PZ_SetNanoTrakModeType_HorizontalTrackMode = 4
    TLMC_PZ_SetNanoTrakModeType_VerticalTrackMode = 5


class TLMC_PZ_TnaIoOutRangeType(IntEnum):
    TLMC_PZ_TnaIoOutRangeType_5V = 0x01
    TLMC_PZ_TnaIoOutRangeType_10V = 0x02


class TLMC_PZ_TnaIoOutRouteType(IntEnum):
    TLMC_PZ_TnaIoOutRouteType_SmaConnectorsOnly=0x01
    TLMC_PZ_TnaIoOutRouteType_SmaConnectorsAndHubRouting=0x02


class TLMC_PZ_TnaIoSignalSourceMode(IntEnum):
    TLMC_PZ_TnaIoSignalSourceMode_InternalPin = 0x00
    TLMC_PZ_TnaIoSignalSourceMode_ExternalIo1 = 0x01


class TLMC_PZ_TnaIoSignalSourceBoostType(IntEnum):
    TLMC_PZ_TnaIoSignalSourceBoostType_Disabled = 0x00
    TLMC_PZ_TnaIoSignalSourceBoostType_Enabled = 0x01


class TLMC_PZ_TnaIoSignalOutputMode(IntEnum):
    TLMC_PZ_TnaIoSignalOutputMode_Disabled = 0x00
    TLMC_PZ_TnaIoSignalOutputMode_Io2 = 0x01


class TLMC_PZ_TnaIoSignalRangeType(IntEnum):
    TLMC_PZ_TnaIoSignalRangeType_75V = 0x00
    TLMC_PZ_TnaIoSignalRangeType_150V = 0x01


class TLMC_PZ_NanoTrakRange(IntEnum):
    TLMC_PZ_NanoTrakRange_Range1 = 0x0003
    TLMC_PZ_NanoTrakRange_Range2 = 0x0004
    TLMC_PZ_NanoTrakRange_Range3 = 0x0005
    TLMC_PZ_NanoTrakRange_Range4 = 0x0006
    TLMC_PZ_NanoTrakRange_Range5 = 0x0007
    TLMC_PZ_NanoTrakRange_Range6 = 0x0008
    TLMC_PZ_NanoTrakRange_Range7 = 0x0009
    TLMC_PZ_NanoTrakRange_Range8 = 0x000A
    TLMC_PZ_NanoTrakRange_Range9 = 0x000B
    TLMC_PZ_NanoTrakRange_Range10 = 0x000C
    TLMC_PZ_NanoTrakRange_Range11 = 0x000D
    TLMC_PZ_NanoTrakRange_Range12 = 0x000E
    TLMC_PZ_NanoTrakRange_Range13 = 0x000F
    TLMC_PZ_NanoTrakRange_Range14 = 0x0010


class TLMC_PZ_NanoTrakUnderOverReadType(IntEnum):
    TLMC_PZ_NanoTrakUnderOverReadType_InRange = 0x0001
    TLMC_PZ_NanoTrakUnderOverReadType_UnderRange = 0x0002
    TLMC_PZ_NanoTrakUnderOverReadType_OverRange = 0x0003


class TLMC_PZ_NanoTrakStatusBit(IntFlag):
    TLMC_PZ_NanoTrakStatusBit_Tracking = 0x0001
    TLMC_PZ_NanoTrakStatusBit_TrackingWithSignal = 0x0002
    TLMC_PZ_NanoTrakStatusBit_TrackingOnlyChannelA = 0x0004
    TLMC_PZ_NanoTrakStatusBit_TrackingOnlyChannelB = 0x0008
    TLMC_PZ_NanoTrakStatusBit_AutoRange = 0x0010
    TLMC_PZ_NanoTrakStatusBit_UnderRead = 0x0020
    TLMC_PZ_NanoTrakStatusBit_OverRead = 0x0040
    TLMC_PZ_NanoTrakStatusBit_ChannelAConnected = 0x00010000
    TLMC_PZ_NanoTrakStatusBit_ChannelBConnected = 0x00020000
    TLMC_PZ_NanoTrakStatusBit_ChannelAEnabled = 0x00040000
    TLMC_PZ_NanoTrakStatusBit_ChannelBEnabled = 0x00080000
    TLMC_PZ_NanoTrakStatusBit_ChannelAControlMode = 0x00100000
    TLMC_PZ_NanoTrakStatusBit_ChannelBControlMode = 0x00200000


class TLMC_LcdKnobMode(IntEnum):
    TLMC_LcdKnobMode_Velocity = 0x0001
    TLMC_LcdKnobMode_Jog = 0x0002


class TLMC_LogLevel(IntEnum):
    TLMC_LogLevel_Critical = 0x0002
    TLMC_LogLevel_Error = 0x0003
    TLMC_LogLevel_Warning = 0x0004
    TLMC_LogLevel_Information = 0x0005


class TLMC_LogCatagoryFilter(IntEnum):
    TLMC_LogCategoryFilter_User = 0x00000001
    TLMC_LogCategoryFilter_Internal = 0x00000002
    TLMC_LogCategoryFilter_Communication = 0x00000004
    TLMC_LogCategoryFilter_NativeApi = 0x00000008
    TLMC_LogCategoryFilter_All = 0xFFFFFFFF


class TLMC_MonitorOutput(IntEnum):
    TLMC_MonitorOutput_None = 0
    TLMC_MonitorOutput_Voltage = 1
    TLMC_MonitorOutput_Position = 2
    TLMC_MonitorOutput_Current = 3
    TLMC_MonitorOutput_Software = 5
    TLMC_MonitorOutput_NanoTrakPosition = 0x80
    TLMC_MonitorOutput_Optical = 0x81


class TLMC_MoveMode(IntEnum):
    TLMC_MoveMode_Absolute = 0
    TLMC_MoveMode_AbsoluteToProgrammedPosition = auto()
    TLMC_MoveMode_Relative = auto()
    TLMC_MoveMode_RelativeByProgrammedDistance = auto()
    TLMC_MoveMode_ContinuousForward = auto()
    TLMC_MoveMode_ContinuousReverse = auto()
    TLMC_MoveMode_JogForward = auto()
    TLMC_MoveMode_JogReverse = auto()

class TLMC_MoveDirection(IntEnum):
    Move_Direction_Forward = 0
    Move_Direction_Reverse = 1
    
class TLMC_NotificationId(IntEnum):
    TLMC_NotificationId_AnalogMonitorConfigurationParamsChanged = 0
    TLMC_NotificationId_AuxIoPortModeChanged = 1
    TLMC_NotificationId_AuxIoSoftwareStatesChanged = 2
    TLMC_NotificationId_BowIndexChanged = 3
    TLMC_NotificationId_CurrentLoopParamsChanged = 4
    TLMC_NotificationId_DcPidParamsChanged = 5
    TLMC_NotificationId_DigitalInputsChanged = 6
    TLMC_NotificationId_DigitalOutputsChanged = 7
    TLMC_NotificationId_EncoderCounterChanged = 8
    TLMC_NotificationId_GeneralMoveParamsChanged = 9
    TLMC_NotificationId_HardwareInfoChanged = 10
    TLMC_NotificationId_HomeParamsChanged = 11
    TLMC_NotificationId_IoConfigurationParamsChanged = 12
    TLMC_NotificationId_IoPositionTriggerEnableStateChanged = 13
    TLMC_NotificationId_IoTriggerParamsChanged = 14
    TLMC_NotificationId_JogParamsChanged = 15
    TLMC_NotificationId_JoystickParamsChanged = 16
    TLMC_NotificationId_KcubeIoTriggerParamsChanged = 17
    TLMC_NotificationId_KcubeMmiLockStateChanged = 18
    TLMC_NotificationId_KcubeMmiParamsChanged = 19
    TLMC_NotificationId_KcubePositionTriggerParamsChanged = 20
    TLMC_NotificationId_LcdDisplayParamsChanged = 21
    TLMC_NotificationId_LcdMoveParamsChanged = 22
    TLMC_NotificationId_LimitSwitchParamsChanged = 23
    TLMC_NotificationId_MotorOutputParamsChanged = 24
    TLMC_NotificationId_MoveAbsoluteParamsChanged = 25
    TLMC_NotificationId_MoveRelativeParamsChanged = 26
    TLMC_NotificationId_PiezoMaxOutputVoltageParamsChanged = 27
    TLMC_NotificationId_PiezoMaxTravelChanged = 28
    TLMC_NotificationId_PiezoOutputVoltageChanged = 29
    TLMC_NotificationId_PiezoOutputVoltageControlSourceChanged = 30
    TLMC_NotificationId_PiezoOutputWaveformParamsChanged = 31
    TLMC_NotificationId_PiezoPositionChanged = 32
    TLMC_NotificationId_PiezoPositionControlModeChanged = 33
    TLMC_NotificationId_PiezoPositionLoopParamsChanged = 34
    TLMC_NotificationId_PiezoSlewRateParamsChanged = 35
    TLMC_NotificationId_PiezoStatusChanged = 36
    TLMC_NotificationId_PiezoStatusBitsChanged = 37
    TLMC_NotificationId_PositionCounterChanged = 38
    TLMC_NotificationId_PositionLoopParamsChanged = 39
    TLMC_NotificationId_PowerParamsChanged = 40
    TLMC_NotificationId_ProfileModeParamsChanged = 41
    TLMC_NotificationId_RichResponseChanged = 42
    TLMC_NotificationId_StageAxisParamsChanged = 43
    TLMC_NotificationId_StepperStatusChanged = 44
    TLMC_NotificationId_TrackSettleParamsChanged = 45
    TLMC_NotificationId_TriggerParamsForDcBrushlessChanged = 46
    TLMC_NotificationId_UniversalStatusChanged = 47
    TLMC_NotificationId_UniversalStatusBitsChanged = 48
    TLMC_NotificationId_VelocityParamsChanged = 49
    TLMC_NotificationId_StatusItemChanged = 50
    TLMC_NotificationId_SettingItemChanged = 51
    TLMC_NotificationId_ConnectedProductChanged = 52
    TLMC_NotificationId_StepperLoopParamsChanged = 53
    TLMC_NotificationId_AdcInputsChanged = 54
    TLMC_NotificationId_TriggerParamsForStepperChanged = 55
    TLMC_NotificationId_ResponseChanged = 56
    TLMC_NotificationId_ButtonParamsChanged = 57
    TLMC_NotificationId_PotentiometerParamsChanged = 58
    TLMC_NotificationId_CalibrationStateChanged = 59
    TLMC_NotificationId_PiezoKpcIoSettingsChanged = 60
    TLMC_NotificationId_PiezoKpcIoTriggerParamsChanged = 61
    TLMC_NotificationId_PiezoKpcMmiParamsChanged = 62
    TLMC_NotificationId_NanoTrakModeChanged = 63
    TLMC_NotificationId_NanoTrakStatusChanged = 64
    TLMC_NotificationId_NanoTrakCircleParamsChanged = 65
    TLMC_NotificationId_NanoTrakRangeParamsChanged = 66
    TLMC_NotificationId_NanoTrakPhaseCompensationParamsChanged = 67
    TLMC_NotificationId_PiezoKnaIoTriggerParamsChanged = 68
    TLMC_NotificationId_NanoTrakCircleHomePositionChanged = 69
    TLMC_NotificationId_NanoTrakGainChanged = 70
    TLMC_NotificationId_NanoTrakTrackThresholdChanged = 71
    TLMC_NotificationId_TNAIoSettingsChanged = 72
    TLMC_NotificationId_PiezoKnaMmiParamsChanged = 73
    TLMC_NotificationId_PiezoXyScanDataChanged = 74
    TLMC_NotificationId_NanoTrakCircleDiameterLutDataChanged = 75
    TLMC_NotificationId_NanoTrakStatusBitsChanged = 76
    TLMC_NotificationId_NanoTrakFeedbackSourceChanged = 77
    TLMC_NotificationId_MonitorOutputParamsChanged = 78
    TLMC_NotificationId_LnnxControlLoopParamsChanged = 79
    TLMC_NotificationId_LnnxNotchFilterParamsChanged = 80
    TLMC_NotificationId_PiezoIoTriggerParamsChanged = 81

class TLMC_OperatingMode(IntFlag):
    TLMC_OperatingMode_StatusPushedByController = 0x00000000
    TLMC_OperatingMode_ManualStatusPolling = 0x00000001
    TLMC_OperatingMode_AutomaticStatusPolling = 0x00000002
    TLMC_OperatingMode_DoNotChangeStatusPollingMode = 0x00000004
    TLMC_OperatingMode_SendEndOfMoveMessages = 0x00000100
    TLMC_OperatingMode_DoNotSendEndOfMoveMessages = 0x00000200
    TLMC_OperatingMode_DoNotLoadParamsOnConnect = 0x00010000
    TLMC_OperatingMode_DoNotSendDisconnectOnFinalClose = 0x00020000
    TLMC_OperatingMode_DoNotAutoSetConnectedProduct = 0x00040000
    TLMC_OperatingMode_DoNotSendNoFlashProgrammingOnConnect = 0x00080000
    TLMC_OperatingMode_Apt = (TLMC_OperatingMode_StatusPushedByController | TLMC_OperatingMode_SendEndOfMoveMessages)
    TLMC_OperatingMode_Kinesis = (TLMC_OperatingMode_AutomaticStatusPolling | TLMC_OperatingMode_SendEndOfMoveMessages)
    TLMC_OperatingMode_Default = TLMC_OperatingMode_Apt
    TLMC_OperatingMode_Expert = (
        TLMC_OperatingMode_DoNotChangeStatusPollingMode | TLMC_OperatingMode_DoNotLoadParamsOnConnect |
        TLMC_OperatingMode_DoNotSendDisconnectOnFinalClose | TLMC_OperatingMode_DoNotAutoSetConnectedProduct)


class TLMC_ParameterGroupId(IntEnum):
    TLMC_ParameterGroupId_Unspecified = 0x0000
    TLMC_ParameterGroupId_JogParams = 0x0416
    TLMC_ParameterGroupId_LimitSwitchParams = 0x0423
    TLMC_ParameterGroupId_GenMoveParams = 0x043A
    TLMC_ParameterGroupId_HomeParams = 0x0440
    TLMC_ParameterGroupId_JoystickParams = 0x04E6
    TLMC_ParameterGroupId_BowIndex = 0x04F4
    TLMC_ParameterGroupId_StepperLoopParams = 0x0529


class TLMC_PortType(IntEnum):
    TLMC_PortType_Physical = 0
    TLMC_PortType_Virtual = 1
    TLMC_PortType_NotPresent = 2


class TLMC_PositionLoopScenario(IntEnum):
    TLMC_PositionLoopScenario_Single = 0x0000
    TLMC_PositionLoopScenario_Stationary = 0x0001
    TLMC_PositionLoopScenario_Accelerating = 0x0002
    TLMC_PositionLoopScenario_AtConstantVelocity = 0x0003


class TLMC_ProfileMode(IntEnum):
    TLMC_ProfileMode_Trapezoidal = 0x0000
    TLMC_ProfileMode_VelocityContouring = 0x0001
    TLMC_ProfileMode_SCurve = 0x0002
    TLMC_ProfileMode_ElectronicGear = 0x0003


class TLMC_PZ_IoTriggerMode(IntEnum):
    TLMC_PZ_IoTriggerMode_Disabled = 0
    TLMC_PZ_IoTriggerMode_GeneralPurposeInput = 1
    TLMC_PZ_IoTriggerMode_InputTriggersTracking = 2
    TLMC_PZ_IoTriggerMode_InputTriggersHomeCircle = 3
    TLMC_PZ_IoTriggerMode_InputTriggersVoltageToggle = 4
    TLMC_PZ_IoTriggerMode_InputTriggersPositionToggle = 5
    TLMC_PZ_IoTriggerMode_GeneralPurposeOutput = 0x0A
    TLMC_PZ_IoTriggerMode_OutputActiveDuringTracking = 0x0B


class TLMC_PZ_OutputVoltageControlSource(IntEnum):
    TLMC_PZ_OutputVoltageControlSource_SoftwareOnly = 0x0000
    TLMC_PZ_OutputVoltageControlSource_ExternalSignal = 0x0001
    TLMC_PZ_OutputVoltageControlSource_Knob = 0x0002


class TLMC_PZ_OutputWaveformOperatingMode(IntEnum):
    TLMC_PZ_OutputWaveformOperatingMode_Continuous = 0x0001
    TLMC_PZ_OutputWaveformOperatingMode_FixedNumberOfCycles = 0x0002
    TLMC_PZ_OutputWaveformOperatingMode_OutputTriggerEnabled = 0x0004
    TLMC_PZ_OutputWaveformOperatingMode_InputTriggerEnabled = 0x0008
    TLMC_PZ_OutputWaveformOperatingMode_OutputTriggerRisingEdge = 0x0010
    TLMC_PZ_OutputWaveformOperatingMode_InputTriggerRisingEdge = 0x0020
    TLMC_PZ_OutputWaveformOperatingMode_OutputGated = 0x0040
    TLMC_PZ_OutputWaveformOperatingMode_TriggerRepeats = 0x0080


class TLMC_PZ_PositionControlMode(IntEnum):
    TLMC_PZ_PositionControlMode_OpenLoop = 0x01
    TLMC_PZ_PositionControlMode_ClosedLoop = 0x02
    TLMC_PZ_PositionControlMode_OpenLoopSmooth = 0x03
    TLMC_PZ_PositionControlMode_ClosedLoopSmooth = 0x04


class TLMC_PZ_StatusBit(IntFlag):
    TLMC_PZ_StatusBit_ActuatorConnected = 0x00000001
    TLMC_PZ_StatusBit_Zeroed = 0x00000010
    TLMC_PZ_StatusBit_Zeroing = 0x00000020
    TLMC_PZ_StatusBit_ExternalStrainGaugeConnected = 0x00000100
    TLMC_PZ_StatusBit_ClosedLoopPositionControl = 0x00000400
    TLMC_PZ_StatusBit_MaxOutputVoltageLow = 0x00001000
    TLMC_PZ_StatusBit_PositionUnderTravel = 0x00001000
    TLMC_PZ_StatusBit_MaxOutputVoltageMedium = 0x00002000
    TLMC_PZ_StatusBit_PositionOverTravel = 0x00002000
    TLMC_PZ_StatusBit_MaxOutputVoltageHigh = 0x00004000
    TLMC_PZ_StatusBit_DigitalInput1 = 0x00100000
    TLMC_PZ_StatusBit_DigitalInput2 = 0x00200000
    TLMC_PZ_StatusBit_DigitalInput3 = 0x00400000
    TLMC_PZ_StatusBit_DigitalInput4 = 0x00800000
    TLMC_PZ_StatusBit_DigitalInput5 = 0x01000000
    TLMC_PZ_StatusBit_DigitalInput6 = 0x02000000
    TLMC_PZ_StatusBit_DigitalInput7 = 0x04000000
    TLMC_PZ_StatusBit_DigitalInput8 = 0x08000000
    TLMC_PZ_StatusBit_PowerOk = 0x10000000
    TLMC_PZ_StatusBit_Active = 0x20000000
    TLMC_PZ_StatusBit_Error = 0x40000000
    TLMC_PZ_StatusBit_Enabled = 0x80000000


class TLMC_PZ_VoltageLimit(IntEnum):
    TLMC_PZ_VoltageLimit_75Volts = 0x0002
    TLMC_PZ_VoltageLimit_100Volts = 0x0004
    TLMC_PZ_VoltageLimit_150Volts = 0x0008


class TLMC_RackBayNumber(IntEnum):
    TLMC_RackBayNumber_1 = 0x0000
    TLMC_RackBayNumber_2 = 0x0001
    TLMC_RackBayNumber_3 = 0x0002
    TLMC_RackBayNumber_4 = 0x0003
    TLMC_RackBayNumber_5 = 0x0004
    TLMC_RackBayNumber_6 = 0x0005
    TLMC_RackBayNumber_7 = 0x0006
    TLMC_RackBayNumber_8 = 0x0007
    TLMC_RackBayNumber_9 = 0x0008
    TLMC_RackBayNumber_10 = 0x0009
    TLMC_RackBayNumber_11 = 0x000A
    TLMC_RackBayNumber_12 = 0x000B


class TLMC_RackBayOccupiedState(IntEnum):
    TLMC_RackBayState_Occupied = 0x0001
    TLMC_RackBayState_Empty = 0x0002


class TLMC_ResultCode(IntEnum):
    TLMC_Success = 0
    TLMC_FunctionNotSupported = 1
    TLMC_DeviceNotFound = 2
    TLMC_DeviceNotSupported = 3
    TLMC_Timeout = 4
    TLMC_Fail = 5
    TLMC_InsufficientFirmware = 6
    TLMC_AlreadyStarted = 7
    TLMC_StartRequired = 8
    TLMC_AllocationError = 9
    TLMC_InternalError = 10
    TLMC_InvalidHandle = 11
    TLMC_InvalidArgument = 12
    TLMC_ItemIsReadOnly = 13
    TLMC_LoadParamsError = 14
    TLMC_TransportError = 15
    TLMC_TransportClosed = 16
    TLMC_TransportNotAvailable = 17
    TLMC_SharingModeNotAvailable = 18
    TLMC_NotInitialized = 19
    TLMC_NoFreeHandles = 20
    TLMC_VerificationFailure = 21
    TLMC_DataNotLoaded = 22
    TLMC_ConnectedProductNotSupported = 23
    TLMC_SimulationCreationError = 24
    TLMC_ConnectedProductNotSet = 25
    TLMC_CalibrationFileNotPresent = 26


class TLMC_ScaleType(IntEnum):
    TLMC_ScaleType_None = 0
    TLMC_ScaleType_Distance = 1
    TLMC_ScaleType_Velocity = 2
    TLMC_ScaleType_Acceleration = 3
    TLMC_ScaleType_Voltage = 4
    TLMC_ScaleType_Brightness = 5
    TLMC_ScaleType_Time = 6
    TLMC_ScaleType_Deceleration = 7
    TLMC_ScaleType_Jerk = 8
    TLMC_ScaleType_RescaledProportion = 9
    TLMC_ScaleType_SlewRate = 10
    TLMC_ScaleType_Force = 11
    TLMC_ScaleType_NormalizedStrainGauge = 12
    TLMC_ScaleType_RescaledVoltage = 13
    TLMC_ScaleType_RescaledDistance = 14
    TLMC_ScaleType_Phase = 15
    TLMC_ScaleType_Frequency = 16
    TLMC_ScaleType_Current = 17
    TLMC_ScaleType_UserDiameter = 18
    TLMC_ScaleType_NanoTrak = 19
    TLMC_ScaleType_Pid = 20
    TLMC_ScaleType_QFactor = 21


class TLMC_SettingStringFormat(IntEnum):
    TLMC_SettingStringFormat_SemiStructured = 0
    TLMC_SettingStringFormat_Json = 1


class TLMC_SoftLimitOperatingMode(IntEnum):
    TLMC_SoftLimitOperatingMode_FeatureNotSupported = 0x0000
    TLMC_SoftLimitOperatingMode_Ignored = 0x0001
    TLMC_SoftLimitOperatingMode_StopImmediate = 0x0002
    TLMC_SoftLimitOperatingMode_StopProfiled = 0x0003
    TLMC_SoftLimitOperatingMode_RestrictMoves = 0x0004
    TLMC_SoftLimitOperatingMode_FilterWheelConnected = 0x0040
    TLMC_SoftLimitOperatingMode_RotationStageLimit = 0x0080


class TLMC_StageAxis_AxisId(IntEnum):
    TLMC_StageAxisId_Unknown = 0x0001
    TLMC_StageAxisId_Rotary = 0x0003
    TLMC_StageAxisId_X = 0x0010
    TLMC_StageAxisId_Y = 0x0011
    TLMC_StageAxisId_Single = 0x0012


class TLMC_StageAxis_TypeId(IntEnum):
    TLMC_StageAxisType_Unknown = 0x0001
    TLMC_StageAxisType_MLS203_X = 0x0010
    TLMC_StageAxisType_MLS203_Y = 0x0011
    TLMC_StageAxisType_DDS = 0x0012
    TLMC_StageAxisType_DDR = 0x0075


class TLMC_StatusItemId(IntEnum):
    TLMC_StatusItemId_Active = 0
    TLMC_StatusItemId_ActuatorConnected = 1
    TLMC_StatusItemId_BusOvercurrent = 2
    TLMC_StatusItemId_BusCurrentFault = 3
    TLMC_StatusItemId_BusVoltageFault = 4
    TLMC_StatusItemId_ClockwiseHardLimit = 5
    TLMC_StatusItemId_CounterclockwiseHardLimit = 6
    TLMC_StatusItemId_ClockwiseSoftLimit = 7
    TLMC_StatusItemId_CommutationError = 8
    TLMC_StatusItemId_Connected = 9
    TLMC_StatusItemId_CounterclockwiseSoftLimit = 10
    TLMC_StatusItemId_ClosedLoopPositionControl = 11
    TLMC_StatusItemId_DigitalInput1 = 12
    TLMC_StatusItemId_DigitalInput2 = 13
    TLMC_StatusItemId_DigitalInput3 = 14
    TLMC_StatusItemId_DigitalInput4 = 15
    TLMC_StatusItemId_DigitalInput5 = 16
    TLMC_StatusItemId_DigitalInput6 = 17
    TLMC_StatusItemId_DigitalInput7 = 18
    TLMC_StatusItemId_DigitalInput8 = 19
    TLMC_StatusItemId_E2PROMFailure = 20
    TLMC_StatusItemId_Enabled = 21
    TLMC_StatusItemId_EncoderCount = 22
    TLMC_StatusItemId_EncoderFault = 23
    TLMC_StatusItemId_Error = 24
    TLMC_StatusItemId_ExternalStrainGaugeConnected = 25
    TLMC_StatusItemId_Homing = 26
    TLMC_StatusItemId_HomingFailed = 27
    TLMC_StatusItemId_Homed = 28
    TLMC_StatusItemId_Initializing = 29
    TLMC_StatusItemId_InstrumentError = 30
    TLMC_StatusItemId_Interlock = 31
    TLMC_StatusItemId_IonBusVoltage = 32
    TLMC_StatusItemId_IonInstructionError = 33
    TLMC_StatusItemId_IonCommutationError = 34
    TLMC_StatusItemId_IonOvercurrent = 35
    TLMC_StatusItemId_IonOvertemperature = 36
    TLMC_StatusItemId_IonReceiveTimeout = 37
    TLMC_StatusItemId_IonInterlockOpen = 38
    TLMC_StatusItemId_IonPhaseInitializationFailed = 39
    TLMC_StatusItemId_JoggingClockwise = 40
    TLMC_StatusItemId_JoggingCounterclockwise = 41
    TLMC_StatusItemId_MotorCurrent = 42
    TLMC_StatusItemId_MotorOvercurrent = 43
    TLMC_StatusItemId_MovingClockwise = 44
    TLMC_StatusItemId_MovingCounterclockwise = 45
    TLMC_StatusItemId_OutputVoltage = 46
    TLMC_StatusItemId_Overcurrent = 47
    TLMC_StatusItemId_Overload = 48
    TLMC_StatusItemId_Overtemperature = 49
    TLMC_StatusItemId_PhaseInitializationFailure = 50
    TLMC_StatusItemId_Position = 51
    TLMC_StatusItemId_PositionError = 52
    TLMC_StatusItemId_PowerOk = 53
    TLMC_StatusItemId_Settled = 54
    TLMC_StatusItemId_Tracking = 55
    TLMC_StatusItemId_UnrecognisedError = 56
    TLMC_StatusItemId_Velocity = 57
    TLMC_StatusItemId_VelocityLimitExceeded = 58
    TLMC_StatusItemId_Zeroed = 59
    TLMC_StatusItemId_Zeroing = 60
    TLMC_StatusItemId_PositionUnderTravel = 61
    TLMC_StatusItemId_PositionOverTravel = 62
    TLMC_StatusItemId_ZeroingFailure = 63
    TLMC_StatusItemId_AbnormalStageMovement = 64
    TLMC_StatusItemId_PulseAcquired = 65
    TLMC_StatusItemId_PulseAcquiring = 66
    TLMC_StatusItemId_WrongStageDetected = 67
    TLMC_StatusItemId_CirclePositionA = 68
    TLMC_StatusItemId_CirclePositionB = 69
    TLMC_StatusItemId_CircleDiameter = 70
    TLMC_StatusItemId_AbsoluteReading = 71
    TLMC_StatusItemId_RelativeReading = 72
    TLMC_StatusItemId_Range = 73
    TLMC_StatusItemId_UnderOverRead = 74
    TLMC_StatusItemId_Gain = 75
    TLMC_StatusItemId_PhaseCompensationA = 76
    TLMC_StatusItemId_PhaseCompensationB = 77
    TLMC_StatusItemId_TrackingWithSignal = 78
    TLMC_StatusItemId_TrackingOnlyChannelA = 79
    TLMC_StatusItemId_TrackingOnlyChannelB = 80
    TLMC_StatusItemId_AutoRange = 81
    TLMC_StatusItemId_UnderRead = 82
    TLMC_StatusItemId_OverRead = 83
    TLMC_StatusItemId_ChannelAConnected = 84
    TLMC_StatusItemId_ChannelBConnected = 85
    TLMC_StatusItemId_ChannelAEnabled = 86
    TLMC_StatusItemId_ChannelBEnabled = 87
    TLMC_StatusItemId_ChannelAControlMode = 88
    TLMC_StatusItemId_ChannelBControlMode = 89
    TLMC_StatusItemId_NanoTrakMode = 90
    TLMC_StatusItemId_FeedbackSaturated = 91


class TLMC_StatusItemValue(IntEnum):
    TLMC_ValueType_int = 0
    TLMC_ValueType_bool = 1
    TLMC_ValueType_string = 2
    TLMC_ValueType_float = 3


class TLMC_StepperStatusBit(IntEnum):
    TLMC_StepperStatusBit_ClockwiseHardLimit = 0x00000001
    TLMC_StepperStatusBit_CounterclockwiseHardLimit = 0x00000002
    TLMC_StepperStatusBit_MovingClockwise = 0x00000010
    TLMC_StepperStatusBit_MovingCounterclockwise = 0x00000020
    TLMC_StepperStatusBit_JoggingClockwise = 0x00000040
    TLMC_StepperStatusBit_JoggingCounterclockwise = 0x00000080
    TLMC_StepperStatusBit_Homing = 0x00000200
    TLMC_StepperStatusBit_Homed = 0x00000400
    TLMC_StepperStatusBit_DigitalInput1 = 0x00100000
    TLMC_StepperStatusBit_DigitalInput2 = 0x00200000
    TLMC_StepperStatusBit_Enabled = 0x80000000


class TLMC_StepperLoopParams_LoopMode(IntEnum):
    TLMC_StepperLoopParams_LoopMode_Open = 0x0001
    TLMC_StepperLoopParams_LoopMode_Closed = 0x0002


class TLMC_StopMode(IntEnum):
    TLMC_StopMode_Immediate = 1
    TLMC_StopMode_Profiled = 2


class TLMC_TriggerModesForDcBrushless(IntEnum):
    TLMC_TriggerModesForDcBrushless_InputActiveIsLogicHigh = 0x01
    TLMC_TriggerModesForDcBrushless_InputTriggersRelativeMove = 0x02
    TLMC_TriggerModesForDcBrushless_InputTriggersAbsoluteMove = 0x04
    TLMC_TriggerModesForDcBrushless_InputTriggersHomeMove = 0x08
    TLMC_TriggerModesForDcBrushless_OutputActiveIsLogicHigh = 0x10
    TLMC_TriggerModesForDcBrushless_OutputActiveDuringMotion = 0x20
    TLMC_TriggerModesForDcBrushless_OutputActiveWhenMotionComplete = 0x40
    TLMC_TriggerModesForDcBrushless_OutputActiveAtMaxVelocity = 0x80


class TLMC_TriggerModesForStepper(IntEnum):
    TLMC_TriggerModesForStepper_None = 0x00
    TLMC_TriggerModesForStepper_InputTriggerEnabled = 0x01
    TLMC_TriggerModesForStepper_OutputTriggerEnabled = 0x02
    TLMC_TriggerModesForStepper_OutputTriggerFollowsInputTrigger = 0x04
    TLMC_TriggerModesForStepper_OutputActiveUntilMoveEnd = 0x08
    TLMC_TriggerModesForStepper_InputTriggersRelativeMove = 0x10
    TLMC_TriggerModesForStepper_InputTriggersAbsoluteMove = 0x20
    TLMC_TriggerModesForStepper_InputTriggersHomeMove = 0x40
    TLMC_TriggerModesForStepper_OutputTriggerSoftwareInitiated = 0x80


class TLMC_Unit(IntEnum):
    TLMC_Unit_Unspecified = 0
    TLMC_Unit_Millimetres = 1
    TLMC_Unit_Degrees = 2
    TLMC_Unit_Radians = 3
    TLMC_Unit_Cycles = 4
    TLMC_Unit_Micrometres = 5
    TLMC_Unit_Volts = 6
    TLMC_Unit_EncoderCounts = 7
    TLMC_Unit_EncoderCountsPerCycle = 8
    TLMC_Unit_EncoderCountsPerCyclePerCycle = 9
    TLMC_Unit_Minutes = 10
    TLMC_Unit_Microseconds = 11
    TLMC_Unit_MillimetresPerSecondPerSecondPerSecond = 12
    TLMC_Unit_Percentage = 13
    TLMC_Unit_VoltsPerMillisecond = 14
    TLMC_Unit_Milliseconds = 15
    TLMC_Unit_Hertz = 16
    TLMC_Unit_Newtons = 17
    TLMC_Unit_Nanoseconds = 18
    TLMC_Unit_Millivolts = 19
    TLMC_Unit_Steps = 20
    TLMC_Unit_Milliamps = 21
    TLMC_Unit_NanoTrak = 22
    TLMC_Unit_QFactor = 23


class TLMC_UniversalStatusBit(IntFlag):
    TLMC_UniversalStatusBit_ClockwiseHardLimit = 0x00000001
    TLMC_UniversalStatusBit_CounterclockwiseHardLimit = 0x00000002
    TLMC_UniversalStatusBit_ClockwiseSoftLimit = 0x00000004
    TLMC_UniversalStatusBit_CounterclockwiseSoftLimit = 0x00000008
    TLMC_UniversalStatusBit_MovingClockwise = 0x00000010
    TLMC_UniversalStatusBit_MovingCounterclockwise = 0x00000020
    TLMC_UniversalStatusBit_JoggingClockwise = 0x00000040
    TLMC_UniversalStatusBit_JoggingCounterclockwise = 0x00000080
    TLMC_UniversalStatusBit_Connected = 0x00000100
    TLMC_UniversalStatusBit_Homing = 0x00000200
    TLMC_UniversalStatusBit_Homed = 0x00000400
    TLMC_UniversalStatusBit_Initializing = 0x00000800
    TLMC_UniversalStatusBit_Tracking = 0x00001000
    TLMC_UniversalStatusBit_Settled = 0x00002000
    TLMC_UniversalStatusBit_PositionError = 0x00004000
    TLMC_UniversalStatusBit_InstrumentError = 0x00008000
    TLMC_UniversalStatusBit_Interlock = 0x00010000
    TLMC_UniversalStatusBit_Overtemperature = 0x00020000
    TLMC_UniversalStatusBit_BusVoltageFault = 0x00040000
    TLMC_UniversalStatusBit_CommutationError = 0x00080000
    TLMC_UniversalStatusBit_DigitalInput1 = 0x00100000
    TLMC_UniversalStatusBit_DigitalInput2 = 0x00200000
    TLMC_UniversalStatusBit_DigitalInput3 = 0x00400000
    TLMC_UniversalStatusBit_DigitalInput4 = 0x00800000
    TLMC_UniversalStatusBit_Overload = 0x01000000
    TLMC_UniversalStatusBit_EncoderFault = 0x02000000
    TLMC_UniversalStatusBit_Overcurrent = 0x04000000
    TLMC_UniversalStatusBit_BusCurrentFault = 0x08000000
    TLMC_UniversalStatusBit_PowerOk = 0x10000000
    TLMC_UniversalStatusBit_Active = 0x20000000
    TLMC_UniversalStatusBit_Error = 0x40000000
    TLMC_UniversalStatusBit_Enabled = 0x80000000


class TLMC_ValueType(IntEnum):
    TLMC_ValueType_int64 = 0
    TLMC_ValueType_bool = 1
    TLMC_ValueType_string = 2
    TLMC_ValueType_float = 3

class TLMC_Wait(IntEnum):
    TLMC_NoWait = 0
    TLMC_InfiniteWait = -1
    TLMC_Unused = 0