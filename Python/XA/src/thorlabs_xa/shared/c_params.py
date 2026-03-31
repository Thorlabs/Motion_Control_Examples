from ctypes import Structure, Union, c_bool, c_char, c_double, c_int16, c_int32, c_int8, c_longlong, c_uint16, c_uint32, c_uint8, c_ulonglong

class C_TLMC_AdcInputs(Structure):
    _pack_ = 1
    _fields_ = [("adcInput1", c_uint16),
                ("adcInput2", c_uint16)
                ]


class C_TLMC_ApiVersion(Structure):
    _pack_ = 1
    _fields_ = [("major", c_uint16),
                ("minor", c_uint16),
                ("patch", c_uint16),
                ("build", c_uint32),
                ("prereleaseLabel", c_char * 32),
                ("displayString", c_char * 64)
                ]


class C_TLMC_AnalogMonitorConfigurationParams(Structure):
    _pack_ = 1
    _fields_ = [("motorChannel", c_uint16),
                ("systemVariable", c_uint16),
                ("scale", c_int32),
                ("offset", c_int32)
                ]


class C_TLMC_AnalogMonitorConfigurationParamsChangedNotificationData(Structure):
    _pack_ = 1
    _fields_ = [("monitorNumber", c_uint16)
                ]


class C_TLMC_AuxIoPortModeChangedNotificationData(Structure):
    _pack_ = 1
    _fields_ = [("portNumber", c_uint16)
                ]

class C_TLMC_ButtonParams(Structure):
    _pack_ = 1
    _fields_ = [("buttonMode", c_uint16),
                ("position1", c_int32),
                ("position2", c_int32),
                ("timeout1Milliseconds", c_uint16),
                ("timeout2Milliseconds", c_uint16)]

class C_TLMC_ConnectedProductInfo(Structure):
    _pack_ = 1
    _fields_ = [("productName", c_char * 64),
                ("partNumber", c_char * 16),
                ("axisType", c_uint16),
                ("movementType", c_uint16),
                ("unitType", c_uint16),
                ("distanceScaleFactor", c_double),
                ("velocityScaleFactor", c_double),
                ("accelerationScaleFactor", c_double),
                ("minPosition", c_double),
                ("maxPosition", c_double),
                ("maxVelocity", c_double),
                ("maxAcceleration", c_double)
                ]


class C_TLMC_CurrentLoopParams(Structure):
    _pack_ = 1
    _fields_ = [("phase", c_uint16),
                ("proportional", c_uint16),
                ("integral", c_uint16),
                ("integralLimit", c_uint16),
                ("integralDeadBand", c_uint16),
                ("feedForward", c_uint16),
                ]


class C_TLMC_CurrentLoopParamsChangedNotificationData(Structure):
    _pack_ = 1
    _fields_ = [("scenario", c_uint16)]


class C_TLMC_DcPidParams(Structure):
    _pack_ = 1
    _fields_ = [("proportional", c_uint32),
                ("integral", c_uint32),
                ("derivative", c_uint32),
                ("integralLimit", c_uint32),
                ("filterControl", c_uint16)
                ]


class C_TLMC_DeviceInfo(Structure):
    _pack_ = 1
    _fields_ = [("deviceFamily", c_uint8),
                ("deviceType", c_uint32),
                ("partNumber", c_char * 8),
                ("device", c_char * 64),
                ("transport", c_char * 128),
                ("parentDevice", c_char * 64),
                ("deviceTypeDescription", c_char * 256)
                ]


class C_TLMC_FirmwareVersion(Structure):
    _pack_ = 1
    _fields_ = [("minorVersion", c_uint8),
                ("interimVersion", c_uint8),
                ("majorVersion", c_uint8),
                ("reserved", c_uint8)
                ]


class C_TLMC_GeneralMoveParams(Structure):
    _pack_ = 1
    _fields_ = [("backlashDistance", c_int32)
                ]


class C_TLMC_HardwareInfo(Structure):
    _pack_ = 1
    _fields_ = [("serialNumber", c_uint32),
                ("partNumber", c_char * 8),
                ("type", c_uint16),
                ("firmwareVersion", C_TLMC_FirmwareVersion),
                ("notes", c_char * 48),
                ("deviceDependantData", c_char * 12),
                ("hardwareVersion", c_uint16),
                ("modificationState", c_uint16),
                ("numChannels", c_uint16)
                ]


class C_TLMC_HomeParams(Structure):
    _pack_ = 1
    _fields_ = [("direction", c_uint16),
                ("limitSwitch", c_uint16),
                ("velocity", c_uint32),
                ("offsetDistance", c_int32)
                ]


class C_TLMC_IoConfigurationParams(Structure):
    _pack_ = 1
    _fields_ = [("mode", c_uint16),
                ("triggerOutSource", c_uint16)
                ]


class TLMC_IoConfigurationParamsChangedNotificationData(Structure):
    _pack_ = 1
    _fields_ = [("portNumber", c_uint16)]


class C_TLMC_IoTriggerParams(Structure):
    _pack_ = 1
    _fields_ = [("triggerInMode", c_uint16),
                ("triggerInPolarity", c_uint16),
                ("triggerInSource", c_uint16),
                ("triggerOutMode", c_uint16),
                ("triggerOutPolarity", c_uint16),
                ("triggerOutForwardStartPosition", c_int32),
                ("triggerOutForwardInterval", c_int32),
                ("triggerOutForwardNumberOfPulses", c_int32),
                ("triggerOutReverseStartPosition", c_int32),
                ("triggerOutReverseInterval", c_int32),
                ("triggerOutReverseNumberOfPulses", c_int32),
                ("triggerOutPulseWidth", c_uint32),
                ("triggerOutNumberOfCycles", c_uint32),
                ("reserved", c_int8 * 8)
                ]


class C_TLMC_JogParams(Structure):
    _pack_ = 1
    _fields_ = [("mode", c_uint16),
                ("stepSize", c_int32),
                ("minVelocity", c_uint32),
                ("acceleration", c_uint32),
                ("maxVelocity", c_uint32),
                ("stopMode", c_uint16),
                ]


class C_TLMC_JoystickParams(Structure):
    _pack_ = 1
    _fields_ = [("lowGearMaxVelocity", c_uint32),
                ("highGearMaxVelocity", c_uint32),
                ("lowGearAcceleration", c_uint32),
                ("highGearAcceleration", c_uint32),
                ("directionSense", c_uint16)
                ]


class C_TLMC_KcubeIoTriggerParams(Structure):
    _pack_ = 1
    _fields_ = [("trigger1Mode", c_uint16),
                ("trigger1Polarity", c_uint16),
                ("trigger2Mode", c_uint16),
                ("trigger2Polarity", c_uint16),
                ("reserved", c_uint8 * 12)
                ]


class C_TLMC_KcubeMmiParams(Structure):
    _pack_ = 1
    _fields_ = [("joystickMode", c_uint16),
                ("joystickMaxVelocity", c_uint32),
                ("joystickAcceleration", c_uint32),
                ("joystickDirectionSense", c_uint16),
                ("presetPosition1", c_int32),
                ("presetPosition2", c_int32),
                ("displayBrightness", c_uint16),
                ("displayTimeout", c_uint16),
                ("displayDimLevel", c_uint16),
                ("presetPosition3", c_int32),
                ("joystickSensativity", c_uint16),
                ("reserved", c_uint8 * 2)
                ]


class C_TLMC_PZ_KpcIoSettingsParams(Structure):
    _pack_ = 1
    _fields_ = [("voltageLimit", c_uint16),
                ("analogInputSource", c_uint16),
                ("filterCutOffFrequency", c_uint16),
                ("voltageRange", c_uint16),
                ("forceSense", c_uint16),
                ("strainGaugeOption", c_uint16)
                ]


class C_TLMC_PZ_KpcMmiParams(Structure):
    _pack_ = 1
    _fields_ = [("joystickMode", c_uint16),
                ("joystickGear", c_uint16),
                ("joystickVoltageStepSize", c_uint16),
                ("joystickPositionStepSize", c_uint16),
                ("joystickDirectionSense", c_uint16),
                ("presetVoltage1", c_uint16),
                ("presetVoltage2", c_uint16),
                ("presetPosition1", c_uint16),
                ("presetPosition2", c_uint16),
                ("displayBrightness", c_uint16),
                ("displayTimeout", c_uint16),
                ("displayDimLevel", c_uint16),
                ("reserved", c_uint8 * 8)
                ]


class C_TLMC_PZ_KpcIoTriggerParams(Structure):
    _pack_ = 1
    _fields_ = [("trigger1Mode", c_uint16),
                ("trigger1Polarity", c_uint16),
                ("trigger2Mode", c_uint16),
                ("trigger2Polarity", c_uint16),
                ("strainGaugeLowerLimit", c_int32),
                ("strainGaugeUpperLimit", c_int32),
                ("smoothingSamples", c_uint16),
                ("monitorOutputMode", c_uint16),
                ("monitorFilterCutOffFrequency", c_uint16),
                ("monitorOutputSoftwareValue", c_int16),
                ("reserved", c_uint8 * 6)
                ]


class C_TLMC_KcubePositionTriggerParams(Structure):
    _pack_ = 1
    _fields_ = [("forwardStartPosition", c_int32),
                ("forwardInterval", c_uint32),
                ("forwardNumberOfPulses", c_uint32),
                ("reverseStartPosition", c_int32),
                ("reverseInterval", c_uint32),
                ("reverseNumberOfPulses", c_uint32),
                ("pulseWidth", c_uint32),
                ("numberOfCycles", c_uint32),
                ("reserved", c_uint8 * 12)
                ]


class C_TLMC_LcdDisplayParams(Structure):
    _pack_ = 1
    _fields_ = [("knobSensitivity", c_int16),
                ("displayBrightness", c_uint16),
                ("displayTimeout", c_uint16),
                ("displayDimLevel", c_uint16),
                ("reserved", c_uint8 * 20)
                ]


class C_TLMC_LcdMoveParams(Structure):
    _pack_ = 1
    _fields_ = [("knobMode", c_uint16),
                ("jogStepSize", c_int32),
                ("acceleration", c_int32),
                ("maxVelocity", c_int32),
                ("jogStopMode", c_uint16),
                ("presetPosition", c_int32 * 3),
                ("reserved", c_uint8 * 20)
                ]


class C_TLMC_LimitSwitchParams(Structure):
    _pack_ = 1
    _fields_ = [("clockwiseHardLimitOperatingMode", c_uint16),
                ("counterclockwiseHardLimitOperatingMode", c_uint16),
                ("clockwiseSoftLimit", c_int32),
                ("counterclockwiseSoftLimit", c_int32),
                ("softLimitOperatingMode", c_uint16)
                ]


class C_TLMC_MotorOutputParams(Structure):
    _pack_ = 1
    _fields_ = [("continuousCurrentLimit", c_uint16),
                ("energyLimit", c_uint16),
                ("motorLimit", c_uint16),
                ("motorBias", c_uint16),
                ("reserved", c_int8 * 4)
                ]


class C_TLMC_MoveAbsoluteParams(Structure):
    _pack_ = 1
    _fields_ = [("absolutePosition", c_int32)
                ]


class C_TLMC_MoveRelativeParams(Structure):
    _pack_ = 1
    _fields_ = [("relativeDistance", c_int32)
                ]


class C_TLMC_PotentiometerParams(Structure):
    _pack = 1
    _fields = [("deflection0", c_uint16),
               ("velocity1", c_int32),
               ("deflection1", c_uint16),
               ("velocity2", c_int32),
               ("deflection2", c_uint16),
               ("velocity3", c_int32),
               ("deflection3", c_uint16),
               ("velocity4", c_int32)]

    
class C_TLMC_PositionLoopParams(Structure):
    _pack_ = 1
    _fields_ = [("proportional", c_uint16),
                ("integral", c_uint16),
                ("integralLimit", c_uint32),
                ("derivative", c_uint16),
                ("servoCycles", c_uint16),
                ("scale", c_uint16),
                ("velocityFeedForward", c_uint16),
                ("accelerationFeedForward", c_uint16),
                ("errorLimit", c_uint32)
                ]


class TLMC_PositionLoopParamsChangedNotificationData(Structure):
    _pack_ = 1
    _fields_ = [("scenario", c_uint16)]


class C_TLMC_PowerParams(Structure):
    _pack_ = 1
    _fields_ = [("restFactor", c_uint16),
                ("moveFactor", c_uint16),
                ]


class C_TLMC_ProfileModeParams(Structure):
    _pack_ = 1
    _fields_ = [("mode", c_uint16),
                ("jerk", c_uint32),
                ("reserved", c_int8 * 4)
                ]

class C_TLMC_PZ_NanoTrakCircleDiameterLookupTableData(Structure):
    _pack_ = 1
    _fields_ = [("lookupTableValues", c_uint16 * 16)]

class C_TLMC_PZ_NanoTrakCircleHomePositionParams(Structure):
    _pack_ = 1
    _fields_ = [("circleHomePositionA", c_uint16),
                ("circleHomePositionB", c_uint16)]

class C_TLMC_PZ_NanoTrakCircleParams(Structure):
    _pack_ = 1
    _fields_ = [("circleDiameterMode", c_uint16),
                ("circleDiameterSoftware", c_uint16),
                ("circleOscillationFrequency", c_uint16),
                ("absolutePowerMinCircleDiameter", c_uint16),
                ("absolutePowerMaxCircleDiameter", c_uint16),
                ("absolutePowerAdjustType", c_uint16)]

class C_TLMC_PZ_NanoTrakEEPROMParams(Structure):
    _pack_ = 1
    _fields_ = [("channelIdentifier", c_uint16),
                ("messageId", c_uint16)]

class C_TLMC_PZ_NanoTrakGainParams(Structure):
    _pack_ = 1
    _fields_ = [("gainControlMode", c_uint16),
                ("gain", c_int16)]

class C_TLMC_PZ_NanoTrakMode(Structure):
    _pack_ = 1
    _fields_ = [("state", c_uint8),
                ("mode", c_uint8)]

class C_TLMC_PZ_NanoTrakPhaseCompensationParams(Structure):
    _pack_ = 1
    _fields_ = [("phaseCompensationMode", c_uint16),
                ("phaseCompensationASoftware", c_int16),
                ("phaseCompensationBSoftware", c_int16)]

class C_TLMC_PZ_NanoTrakRangeParams(Structure):
    _pack_ = 1
    _fields_ = [("rangeMode", c_uint16),
                ("rangeUpLimit", c_int16),
                ("rangeDownLimit", c_int16),
                ("settleSamples", c_int16),
                ("rangeChangeType", c_uint16),
                ("rangeType", c_uint16)]

class C_TLMC_PZ_NanoTrakStatus(Structure):
    _pack_ = 1
    _fields_ = [("circlePositionA", c_uint16),
                ("circlePositionB", c_uint16),
                ("circleDiameter", c_uint16),
                ("absoluteReading", c_uint32),
                ("relativeReading", c_uint32),
                ("range", c_int16),
                ("underOverRead", c_int16),
                ("statusBits", c_uint32),
                ("nanoTrakGain", c_int16),
                ("phaseCompensationA", c_int16),
                ("phaseCompensationB", c_int16)]

class C_TLMC_PZ_NanoTrakTnaIoSettings(Structure):
    _pack_ = 1
    _fields_ = [("outRangeType", c_uint8),
                ("outRouteType", c_uint8),
                ("signalSourceMode", c_uint8),
                ("signalSourceBoostType", c_uint8),
                ("signalOutputMode", c_uint8),
                ("channel1SignalRangeType", c_uint8),
                ("channel2SignalRangeType", c_uint8)]

class C_TLMC_PZ_NanoTrakTrackThresholdParams(Structure):
    _pack_ = 1
    _fields_ = [("trackThreshold", c_uint32)]


class C_TLMC_Notification(Structure):
    _pack = 1
    _fields = [("id", c_int32),
               ("data", c_ulonglong),
               ("dataLength", c_uint32)]


class C_TLMC_PZ_OutputWaveformParams(Structure):
    _pack_ = 1
    _fields_ = [("mode", c_uint16),
                ("numberOfSamplesPerCycle", c_uint16),
                ("numberOfCycles", c_int32),
                ("interSampleDelay", c_int32),
                ("preCycleDelay", c_int32),
                ("postCycleDelay", c_int32),
                ("outputTriggerStartIndex", c_uint16),
                ("outputTriggerWidth", c_int32),
                ("numberOfSamplesBetweenTriggerRepetition", c_uint16)
                ]

class C_TLMC_PZ_OutputWaveformLoopTableSample(Structure):
    _pack_ = 1
    _fields_ = [("index", c_uint16),
                ("voltage", c_int16)
                ]

class C_TLMC_PZ_MaxOutputVoltageParams(Structure):
    _pack_ = 1
    _fields_ = [("maxOutputVoltage", c_uint16),
                ("voltageLimit", c_uint16)
                ]


class C_TLMC_PZ_OutputVoltageControlSourceParams(Structure):
    _pack_ = 1
    _fields_ = [("source", c_uint16)
                ]


class C_TLMC_PZ_PositionLoopParams(Structure):
    _pack_ = 1
    _fields_ = [("proportional", c_uint16),
                ("integral", c_uint16)
                ]


class C_TLMC_PZ_Status(Structure):
    _pack_ = 1
    _fields_ = [("outputVoltage", c_int16),
                ("position", c_int16),
                ("statusBits", c_uint32)
                ]


class C_TLMC_PZ_SlewRateParams(Structure):
    _pack_ = 1
    _fields_ = [("openSlewRate", c_uint16),
                ("closedLoopSlewRate", c_uint16)
                ]


class C_TLMC_RichResponse(Structure):
    _pack_ = 1
    _fields_ = [("messageId", c_uint16),
                ("code", c_uint16),
                ("notes", c_char * 64)
                ]


class TLMC_Response(Structure):
    _pack_ = 1
    _fields_ = [("messageId", c_uint16),
                ("code", c_uint16)
                ]


class C_TLMC_Value(Union):
    _pack_ = 1
    _fields_ = [("int64Value", c_longlong),
                ("boolValue", c_bool),
                ("string", c_char * 24)
                ]


class C_TLMC_Setting(Structure):
    _pack_ = 1
    _fields_ = [("valueType", c_uint8),
                ("isValueSet", c_bool),
                ("Value", C_TLMC_Value),
                ("ScaleType", c_uint16),
                ("UnitType", c_uint16),
                ("Name", c_char * 128),
                ("DisplayName", c_char * 128),
                ("isReadOnly", c_bool),
                ("hasDiscreteValues", c_bool),
                ("hasMin", c_bool),
                ("hasMax", c_bool),
                ("minValue", C_TLMC_Value),
                ("maxValue", C_TLMC_Value)
                ]


class C_TLMC_SettingItemChangedNotificationData(Structure):
    _pack_ = 1
    _fields_ = [("settingName", c_char * 128)]


class C_TLMC_StageAxisParams(Structure):
    _pack_ = 1
    _fields_ = [("typeId", c_uint16),
                ("axisId", c_uint16),
                ("partNumber", c_char * 16),
                ("serialNumber", c_uint32),
                ("countsPerUnit", c_uint32),
                ("minPosition", c_int32),
                ("maxPosition", c_int32),
                ("maxAcceleration", c_uint32),
                ("maxDeceleration", c_uint32),
                ("maxVelocity", c_uint32),
                ("gearBoxRatio", c_uint16),
                ("reserved", c_uint8 * 22)
                ]


class C_TLMC_StatusItem(Structure):
    _pack_ = 1
    _fields_ = [("id", c_int32),
                ("valueType", c_uint8),
                ("value", C_TLMC_Value)
                ]


class C_TLMC_StatusItemChangedNotificationData(Structure):
    _pack_ = 1
    _fields_ = [("count", c_uint16),
                ("ids", c_int32)
                ]


class C_TLMC_StepperLoopParams(Structure):
    _pack_ = 1
    _fields_ = [("loopMode", c_uint16),
                ("proportional", c_int32),
                ("integral", c_int32),
                ("differential", c_int32),
                ("outputClip", c_int32),
                ("outputTolerance", c_int32),
                ("microstepsPerEncoderCount", c_uint32),
                ("reserved", c_uint8 * 8)
                ]


class C_TLMC_StepperStatus(Structure):
    _pack_ = 1
    _fields_ = [("position", c_int32),
                ("encoderCount", c_int32),
                ("statusBits", c_int32),
                ]


class C_TLMC_TrackSettleParams(Structure):
    _pack_ = 1
    _fields_ = [("settleTime", c_uint16),
                ("settleWindow", c_uint16),
                ("trackWindow", c_uint16),
                ("reserved", c_uint8 * 4)
                ]


class C_TLMC_TriggerParamsForDcBrushless(Structure):
    _pack_ = 1
    _fields_ = [("modes", c_uint8)]


class C_TLMC_TriggerParamsForStepper(Structure):
    _pack_ = 1
    _fields_ = [("modes", c_uint8)]


class C_TLMC_UniversalStatus(Structure):
    _pack_ = 1
    _fields_ = [("position", c_int32),
                ("velocity", c_int16),
                ("motorCurrent", c_int16),
                ("statusBits", c_uint32)
                ]


class C_TLMC_VelocityParams(Structure):
    _pack_ = 1
    _fields_ = [("minVelocity", c_uint32),
                ("acceleration", c_uint32),
                ("maxVelocity", c_uint32)
                ]