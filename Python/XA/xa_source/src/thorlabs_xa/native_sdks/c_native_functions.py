import copy
from ctypes import c_bool, c_char_p, c_int16, c_int8, c_uint, c_uint32, byref, c_double, c_ulong, c_int64, c_int32, c_uint16, c_uint8, create_string_buffer
import ctypes
from importlib.resources import as_file, files
import os
from pathlib import Path
import platform
import json
import sys
from typing import Any, List, Mapping, Optional

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.enums import TLMC_AnalogMonitorNumber, TLMC_AuxIoPortMode, TLMC_AuxIoPortNumber, TLMC_BowIndex, TLMC_CalibrationState, TLMC_CurrentLoopScenario, TLMC_DigitalInput, TLMC_DigitalOutput, TLMC_EnableState, TLMC_EndOfMoveMessagesMode, TLMC_IoPortNumber, TLMC_IoPositionTriggerEnableState, TLMC_KcubeMmiLockState, TLMC_MoveDirection, TLMC_MoveMode, TLMC_OperatingMode, TLMC_PZ_PositionControlMode, TLMC_PZ_SetNanoTrakModeType, TLMC_PZ_StatusBit, TLMC_ParameterGroupId, TLMC_PositionLoopScenario, TLMC_RackBayNumber, TLMC_RackBayOccupiedState, TLMC_ResultCode, TLMC_ScaleType, TLMC_SettingStringFormat, TLMC_StatusItemId, TLMC_StopMode, TLMC_Unit, TLMC_UniversalStatusBit, TLMC_Wait
from thorlabs_xa.shared.c_params import C_TLMC_AdcInputs, C_TLMC_AnalogMonitorConfigurationParams, C_TLMC_ApiVersion, C_TLMC_ButtonParams, C_TLMC_ConnectedProductInfo, C_TLMC_CurrentLoopParams, C_TLMC_DcPidParams, C_TLMC_DeviceInfo, C_TLMC_FirmwareVersion, C_TLMC_GeneralMoveParams, C_TLMC_HardwareInfo, C_TLMC_HomeParams, C_TLMC_IoConfigurationParams, C_TLMC_IoTriggerParams, C_TLMC_JogParams, C_TLMC_JoystickParams, C_TLMC_JoystickSettingsParams, C_TLMC_KcubeIoTriggerParams, C_TLMC_KcubeMmiParams, C_TLMC_KcubePositionTriggerParams, C_TLMC_LcdDisplayParams, C_TLMC_LcdMoveParams, C_TLMC_LimitSwitchParams, C_TLMC_MonitorOutputParams, C_TLMC_MotorOutputParams, C_TLMC_MoveAbsoluteParams, C_TLMC_MoveRelativeParams, C_TLMC_PZ_KpcIoSettingsParams, C_TLMC_PZ_KpcIoTriggerParams, C_TLMC_PZ_KpcMmiParams, C_TLMC_PZ_LnnxControlLoopParams, C_TLMC_PZ_LnnxNotchFilterParams, C_TLMC_PZ_MaxOutputVoltageParams, C_TLMC_PZ_NanoTrakCircleDiameterLookupTableData, C_TLMC_PZ_NanoTrakCircleHomePositionParams, C_TLMC_PZ_NanoTrakCircleParams, C_TLMC_PZ_NanoTrakGainParams, C_TLMC_PZ_NanoTrakMode, C_TLMC_PZ_NanoTrakPhaseCompensationParams, C_TLMC_PZ_NanoTrakRangeParams, C_TLMC_PZ_NanoTrakStatus, C_TLMC_PZ_NanoTrakTnaIoSettings, C_TLMC_PZ_NanoTrakTrackThresholdParams, C_TLMC_PZ_OutputVoltageControlSourceParams, C_TLMC_PZ_OutputWaveformParams, C_TLMC_PZ_PositionLoopParams, C_TLMC_PZ_SlewRateParams, C_TLMC_PZ_StageInfoParams, C_TLMC_PZ_Status, C_TLMC_PositionLoopParams, C_TLMC_PotentiometerParams, C_TLMC_PowerParams, C_TLMC_ProfileModeParams, C_TLMC_RichResponse, C_TLMC_Setting, C_TLMC_StageAxisParams, C_TLMC_StatusItem, C_TLMC_StepperLoopParams, C_TLMC_StepperStatus, C_TLMC_TrackSettleParams, C_TLMC_TriggerParamsForDcBrushless, C_TLMC_TriggerParamsForStepper, C_TLMC_UniversalStatus, C_TLMC_VelocityParams
from thorlabs_xa.shared.params import TLMC_AdcInputs, TLMC_AnalogMonitorConfigurationParams, TLMC_ApiVersion, TLMC_ButtonParams, TLMC_ConnectedProductInfo, TLMC_CurrentLoopParams, TLMC_DeviceInfo, TLMC_FirmwareVersion, TLMC_GeneralMoveParams, TLMC_HardwareInfo, TLMC_HomeParams, TLMC_DcPidParams, TLMC_IoConfigurationParams, TLMC_IoTriggerParams, TLMC_JogParams, TLMC_JoystickParams, TLMC_JoystickSettingsParams, TLMC_KcubeIoTriggerParams, TLMC_KcubeMmiParams, TLMC_KcubePositionTriggerParams, TLMC_LcdDisplayParams, TLMC_LcdMoveParams, TLMC_LimitSwitchParams, TLMC_MonitorOutputParams, TLMC_MotorOutputParams, TLMC_MoveAbsoluteParams, TLMC_MoveRelativeParams, TLMC_PZ_KpcIoSettingsParams, TLMC_PZ_KpcIoTriggerParams, TLMC_PZ_KpcMmiParams, TLMC_PZ_LnnxControlLoopParams, TLMC_PZ_LnnxNotchFilterParams, TLMC_PZ_MaxOutputVoltageParams, TLMC_PZ_NanoTrakCircleDiameterLookupTableData, TLMC_PZ_NanoTrakCircleHomePositionParams, TLMC_PZ_NanoTrakEEPROMParams, TLMC_PZ_NanoTrakGainParams, TLMC_PZ_NanoTrakMode, TLMC_PZ_NanoTrakPhaseCompensationParams, TLMC_PZ_NanoTrakRangeParams, TLMC_PZ_NanoTrakStatus, TLMC_PZ_NanoTrakTnaIoSettings, TLMC_PZ_NanoTrakTrackThresholdParams, TLMC_PZ_OutputVoltageControlSourceParams, TLMC_PZ_OutputWaveformParams, TLMC_PZ_PositionLoopParams, TLMC_PZ_SlewRateParams, TLMC_PZ_StageInfoParams, TLMC_PZ_Status, TLMC_PositionLoopParams, TLMC_PotentiometerParams, TLMC_PowerParams, TLMC_ProfileModeParams, TLMC_RichResponse, TLMC_Setting, TLMC_StageAxisParams, TLMC_StatusItem, TLMC_StepperLoopParams, TLMC_StepperStatus, TLMC_TrackSettleParams, TLMC_TriggerParamsForDcBrushless, TLMC_TriggerParamsForStepper, TLMC_UniversalStatus, TLMC_Value, TLMC_VelocityParams, TLMC_PZ_NanoTrakCircleParams, TLMC_PZ_OutputWaveformLoopTableSample

from thorlabs_xa.shared.xa_error_factory import XAErrorFactory

from thorlabs_xa.shared.map_native_to_python import MapNativeToPython
from thorlabs_xa.shared.map_python_to_native import MapPythonToNative

class CNativeFunctions(NativeFunctions):

    NATIVELIBRARYFILENAME_WINDOWS = "tlmc_xa_native.dll"
    NATIVELIBRARYFILENAME_LINUX = "libtlmc_xa_native.so"

    xa_lib: ctypes.CDLL | None = None

    def __init__(self) -> None:
        lib_name = self.pick_lib_name()

        resource_pkg = "thorlabs_xa"
        resource = files(resource_pkg).joinpath(lib_name)

        with as_file(resource) as lib_path:
            self.load_with_search_path(lib_path)

    def pick_lib_name(self) -> str:
        system = platform.system()
        if system == "Windows":
            return self.NATIVELIBRARYFILENAME_WINDOWS
        elif system == "Linux":
            return self.NATIVELIBRARYFILENAME_LINUX
        raise OSError(f"Unsupported OS: {system}")

    def load_with_search_path(self, lib_path: Path) -> None:

        if sys.platform.startswith("win"):
            dll_dir = str(lib_path.parent)
            try:
                os.add_dll_directory(dll_dir)
            except (AttributeError, FileNotFoundError):
                os.environ["PATH"] = dll_dir + os.pathsep + os.environ.get("PATH", "")

        try:
            self.xa_lib = ctypes.CDLL(str(lib_path))
        except OSError as e:
            raise OSError(
                f"Failed to load native library at '{lib_path}': {e}\n"
                f"OS: {platform.system()} Arch: {platform.machine()} "
                f"Python: {platform.python_version()} "
            ) from e


    @staticmethod
    def wrap_error_code(return_code: int):

        if (return_code != 0):
            exception = XAErrorFactory.convert_return(TLMC_ResultCode(return_code))

            if exception is not None:
                raise exception

    def activate_calibration(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_ActivateCalibration(c_ulong(handle)))

    def add_user_message_to_log(self, user_message: str) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_AddUserMessageToLog(MapPythonToNative.string(user_message)))

    def close(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Close(c_ulong(handle)))

    def convert_from_device_units_to_physical(self, handle: int, scale_type: TLMC_ScaleType, device_value: int) -> tuple [float, TLMC_Unit]:
        c_physical = c_double(0)
        c_unit = c_int32(0)
         
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_ConvertFromDeviceToPhysical(c_ulong(handle), c_uint16(scale_type), c_int64(device_value), byref(c_physical), byref(c_unit)))
        return c_physical.value, TLMC_Unit(c_unit.value)

    def convert_from_physical_to_device(self, handle: int, scale_type: TLMC_ScaleType, unit: TLMC_Unit, physical_value: float) -> int:
        device_val = c_int64(0)

        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_ConvertFromPhysicalToDevice(c_ulong(handle), c_uint16(scale_type), c_uint16(unit), c_double(physical_value), byref(device_val)))
        return device_val.value

    def create_simulation(self, description: Mapping[str, Any]) -> None:
        contents = json.dumps(description)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_CreateSimulation(MapPythonToNative.string(contents)))

    def deactivate_calibration(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_DeactivateCalibration(c_ulong(handle)))

    def disconnect(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Disconnect(c_ulong(handle)))

    def get_adc_inputs(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_AdcInputs:
        c_params = C_TLMC_AdcInputs()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetAdcInputs(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))

        return MapNativeToPython.adc_inputs(c_params)

    def get_analog_monitor_configuration_params(self, handle: int, monitor_number: TLMC_AnalogMonitorNumber, max_wait_in_milliseconds: int) -> TLMC_AnalogMonitorConfigurationParams:
        c_params = C_TLMC_AnalogMonitorConfigurationParams()        
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetAnalogMonitorConfigurationParams(c_ulong(handle), c_uint16(monitor_number), byref(c_params), c_int64(max_wait_in_milliseconds)))

        return MapNativeToPython.analog_monitor_configuration_params(c_params)

    def get_api_version(self) -> TLMC_ApiVersion:
        c_params = C_TLMC_ApiVersion()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetApiVersion(byref(c_params)))

        return MapNativeToPython.api_version(c_params)

    def get_aux_io_port_mode(self, handle: int, port_number: TLMC_AuxIoPortNumber, max_wait_in_milliseconds: int) -> TLMC_AuxIoPortMode:
        c_port_mode = c_uint16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetAuxIoPortMode(handle, c_uint16(port_number), byref(c_port_mode), c_int64(max_wait_in_milliseconds)))

        return TLMC_AuxIoPortMode(c_port_mode.value)

    def get_aux_io_software_states(self, handle: int, max_wait_in_milliseconds: int) -> int:
        c_software_states = c_uint16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetAuxIoSoftwareStates(c_ulong(handle), byref(c_software_states), c_int64(max_wait_in_milliseconds)))
        return c_software_states.value

    def get_button_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_ButtonParams:
        c_button_params = C_TLMC_ButtonParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetButtonParams(c_ulong(handle), byref(c_button_params), c_int64(max_wait_in_milliseconds)))

        return MapNativeToPython.button_params(c_button_params)
        
    def get_calibration_state(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_CalibrationState:
        c_calibration_state = c_uint8(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetCalibrationState(c_ulong(handle), byref(c_calibration_state), c_int64(max_wait_in_milliseconds)))

        return TLMC_CalibrationState(c_calibration_state)

    def get_bow_index(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_BowIndex:
        c_bow_index = c_uint16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetBowIndex(handle, byref(c_bow_index), c_int64(max_wait_in_milliseconds)))
        return TLMC_BowIndex(c_bow_index.value)

    def get_connected_product(self, handle: int, max_length: int) -> str:
        c_buffer = ctypes.create_string_buffer(max_length)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetConnectedProduct(c_ulong(handle), byref(c_buffer), c_uint(max_length)))

        return MapNativeToPython.string(c_buffer)

    def get_connected_product_info(self, handle: int) -> TLMC_ConnectedProductInfo:
        c_params = C_TLMC_ConnectedProductInfo()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetConnectedProductInfo(c_ulong(handle), byref(c_params)))

        return MapNativeToPython.connected_product_info(c_params)

    def get_connected_products_supported(self, handle: int) -> str:

        result_length = c_uint32(0)

        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetConnectedProductsSupported(
            c_ulong(handle),
            None,
            c_uint(0),
            byref(result_length)))

        buffer_length = result_length.value + 1
        c_buffer = ctypes.create_string_buffer(buffer_length)

        result_length = c_int32(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetConnectedProductsSupported(
            c_ulong(handle),
            byref(c_buffer),
            c_uint(buffer_length),
            byref(result_length)))
        
        return MapNativeToPython.string(c_buffer)

    def get_current_loop_params(self, handle: int, loop_scenario: TLMC_CurrentLoopScenario, max_wait_in_milliseconds: int) -> TLMC_CurrentLoopParams:
        c_params = C_TLMC_CurrentLoopParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetCurrentLoopParams(c_ulong(handle), loop_scenario,
            byref(c_params), c_int64(max_wait_in_milliseconds)))

        return MapNativeToPython.current_loop_params(c_params)

    def get_dc_pid_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_DcPidParams:
        c_params = C_TLMC_DcPidParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetDcPidParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))

        return MapNativeToPython.dc_pid_params(c_params)

    def get_device_info(self, handle: int) -> TLMC_DeviceInfo:
        c_params = C_TLMC_DeviceInfo()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetDeviceInfo(c_ulong(handle), byref(c_params)))

        return MapNativeToPython.device_info(c_params)

    def get_device_list_item_count(self) -> int:
        c_count = c_uint16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetDeviceListItemCount(byref(c_count)))
        return c_count.value

    def get_device_list_items(self, source_start_index: int, number_of_items: int) -> List[TLMC_DeviceInfo]:
        ArrayType = C_TLMC_DeviceInfo * number_of_items
        items_buf = ArrayType()

        items_copied = c_uint16(0)

        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetDeviceListItems(c_uint16(source_start_index), c_uint16(number_of_items), items_buf, byref(items_copied)))

        count = int(items_copied.value)
        device_infos: list[TLMC_DeviceInfo] = []
        for i in range(count):
            device_infos.append(MapNativeToPython.device_info(copy.copy(items_buf[i])))

        return device_infos

    def get_digital_input_states(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_DigitalInput:
        c_state = c_uint16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetDigitalInputStates(c_ulong(handle), byref(c_state), c_int64(max_wait_in_milliseconds)))
        return TLMC_DigitalInput(c_state.value)
    
    def get_digital_output_states(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_DigitalOutput:
        c_state = c_uint8(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetDigitalOutputStates(c_ulong(handle), byref(c_state), c_int64(max_wait_in_milliseconds)))
        return TLMC_DigitalOutput(c_state.value)

    def get_enable_state(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_EnableState:
        c_enable_state = c_uint8(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetEnableState(c_ulong(handle), byref(c_enable_state), c_int64(max_wait_in_milliseconds)))
        return TLMC_EnableState(c_enable_state.value)

    def get_encoder_counter(self, handle: int, max_wait_in_milliseconds: int) -> int:
        c_encoder_counter = c_int32(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetEncoderCounter(c_ulong(handle), byref(c_encoder_counter), c_int64(max_wait_in_milliseconds)))
        return c_encoder_counter.value

    def get_firmware_version_info(self, handle: int, max_wait_in_milliseconds: int) -> tuple [TLMC_FirmwareVersion, TLMC_FirmwareVersion]:
        c_device_firmware_version = C_TLMC_FirmwareVersion()
        c_required_firmware_version = C_TLMC_FirmwareVersion()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetFirmwareVersionInfo(c_ulong(handle), byref(c_device_firmware_version), byref(c_required_firmware_version), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.firmware_version(c_device_firmware_version), MapNativeToPython.firmware_version(c_required_firmware_version)

    def get_general_move_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_GeneralMoveParams:
        c_params = C_TLMC_GeneralMoveParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetGeneralMoveParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.general_move_params(c_params)

    def get_hardware_info(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_HardwareInfo:
        c_params = C_TLMC_HardwareInfo()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetHardwareInfo(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.hardware_info(c_params)

    def get_home_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_HomeParams:
        c_params = C_TLMC_HomeParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetHomeParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.home_params(c_params)

    def get_io_configuration_number_of_ports_supported(self, handle: int) -> int:
        c_ports = c_uint8(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetIoConfigurationNumberOfPortsSupported(handle, byref(c_ports)))
        return c_ports.value

    def get_io_configuration_params(self, handle: int, port_number: TLMC_IoPortNumber, max_wait_in_milliseconds: int) -> TLMC_IoConfigurationParams:
        c_params = C_TLMC_IoConfigurationParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetIoConfigurationParams(c_ulong(handle), c_uint16(port_number.value), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.io_configuration_params(c_params)

    def get_io_position_trigger_enable_state(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_IoPositionTriggerEnableState:
        c_enable_state = c_uint8(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetIoPositionTriggerEnableState(c_ulong(handle), byref(c_enable_state), c_int64(max_wait_in_milliseconds)))
        return TLMC_IoPositionTriggerEnableState(c_enable_state.value)

    def get_io_trigger_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_IoTriggerParams:
        c_params = C_TLMC_IoTriggerParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetIoTriggerParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.io_trigger_params(c_params)

    def get_jog_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_JogParams:
        c_params = C_TLMC_JogParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetJogParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.jog_params(c_params)

    def get_joystick_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_JoystickParams:
        c_params = C_TLMC_JoystickParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetJoystickParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.joystick_params(c_params)

    def get_joystick_settings_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_JoystickSettingsParams:
        c_params = C_TLMC_JoystickSettingsParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetJoystickSettingsParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.joystick_settings_params(c_params)

    def get_kcube_io_trigger_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_KcubeIoTriggerParams:
        c_params = C_TLMC_KcubeIoTriggerParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetKcubeIoTriggerParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.kcube_io_trigger_params(c_params)

    def get_kcube_mmi_lock_state(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_KcubeMmiLockState:
        c_lock_state = c_uint8(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetKcubeMmiLockState(c_ulong(handle), byref(c_lock_state), c_int64(max_wait_in_milliseconds)))
        return TLMC_KcubeMmiLockState(c_lock_state.value)

    def get_kcube_mmi_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_KcubeMmiParams:
        c_params = C_TLMC_KcubeMmiParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetKcubeMmiParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.kcube_mmi_params(c_params)

    def get_kcube_position_trigger_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_KcubePositionTriggerParams:
        c_params = C_TLMC_KcubePositionTriggerParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetKcubePositionTriggerParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.kcube_position_trigger_params(c_params)

    def get_lcd_display_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_LcdDisplayParams:
        c_params = C_TLMC_LcdDisplayParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetLcdDisplayParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.lcd_display_params(c_params)

    def get_lcd_move_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_LcdMoveParams:
        c_params = C_TLMC_LcdMoveParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetLcdMoveParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.lcd_move_params(c_params)

    def get_limit_switch_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_LimitSwitchParams:
        c_params = C_TLMC_LimitSwitchParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetLimitSwitchParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.limit_switch_params(c_params)
    
    def get_monitor_output_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_MonitorOutputParams:
        c_params = C_TLMC_MonitorOutputParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetMonitorOutputParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.monitor_output_params(c_params)

    def get_motor_output_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_MotorOutputParams:
        c_params = C_TLMC_MotorOutputParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetMotorOutputParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.motor_output_params(c_params)

    def get_move_absolute_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_MoveAbsoluteParams:
        c_params = C_TLMC_MoveAbsoluteParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetMoveAbsoluteParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.move_absolute_params(c_params)

    def get_move_relative_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_MoveRelativeParams:
        c_params = C_TLMC_MoveRelativeParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetMoveRelativeParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.move_relative_params(c_params)

    def get_position_counter(self, handle: int, max_wait_in_milliseconds: int) -> int:
        c_position_counter = c_int32(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetPositionCounter(c_ulong(handle), byref(c_position_counter), c_int64(max_wait_in_milliseconds)))
        return c_position_counter.value

    def get_position_loop_params(self, handle: int, position_loop_scenario: TLMC_PositionLoopScenario, max_wait_in_milliseconds: int) -> TLMC_PositionLoopParams:
        c_params = C_TLMC_PositionLoopParams()
        max_wait_val = c_int64(max_wait_in_milliseconds)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetPositionLoopParams(c_ulong(handle), c_uint16(int(position_loop_scenario)), byref(c_params), max_wait_val))
        return MapNativeToPython.position_loop_params(c_params)
    
    def get_potentiometer_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PotentiometerParams:
        c_params = C_TLMC_PotentiometerParams()
        max_wait_val = c_int64(max_wait_in_milliseconds)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetPotentiometerParams(c_ulong(handle), byref(c_params), max_wait_val))
        return MapNativeToPython.potentiometer_params(c_params)

    def get_power_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PowerParams:
        c_params = C_TLMC_PowerParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetPowerParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.power_params(c_params)

    def get_preferred_physical_unit(self, handle: int, scale_type: TLMC_ScaleType) -> TLMC_Unit:
        c_unit = c_int32(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetPreferredPhysicalUnit(c_ulong(handle), c_uint16(scale_type.value), byref(c_unit)))
        return TLMC_Unit(c_unit.value)
    
    def get_profile_mode_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_ProfileModeParams:
        c_params = C_TLMC_ProfileModeParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetProfileModeParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.profile_mode_params(c_params)

    def get_rack_bay_occupied_state(self, handle: int, bay_number: TLMC_RackBayNumber, max_wait_in_milliseconds: int) -> TLMC_RackBayOccupiedState:
        c_state = c_uint8(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetRackBayOccupiedState(c_ulong(handle), c_uint16(bay_number.value), byref(c_state), c_int64(max_wait_in_milliseconds)))
        return TLMC_RackBayOccupiedState(c_state.value)

    def get_rich_response(self, handle: int) -> TLMC_RichResponse:
        c_params = C_TLMC_RichResponse()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetRichResponse(c_ulong(handle), byref(c_params)))
        return MapNativeToPython.rich_response(c_params)

    def get_setting(self, handle: int, settings_name: str, max_wait_in_milliseconds: int) -> TLMC_Setting:
        c_params = C_TLMC_Setting()
        c_settings_name = create_string_buffer(settings_name.encode("utf-8"))
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetSetting(c_ulong(handle), c_settings_name, byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.setting(c_params)

    def get_setting_count(self, handle: int) -> int:
        c_count = c_uint16()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetSettingCount(c_ulong(handle), byref(c_count)))
        return c_count.value

    def get_settings(self, handle: int, source_start_index: int, number_of_items: int) -> List[TLMC_Setting]:

        if number_of_items <= 0:
            return []

        ArrayType = C_TLMC_Setting * number_of_items
        settings_buf = ArrayType()
        items_copied = c_uint16(0)

        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetSettings(
            c_ulong(handle),
            c_uint16(source_start_index),
            c_uint16(number_of_items),
            settings_buf,
            byref(items_copied)
        ))

        count = min(items_copied.value, number_of_items)

        settings: List[TLMC_Setting] = []

        for i in range(count):
            settings.append(MapNativeToPython.setting(copy.copy(settings_buf[i])))

        return settings

    def get_setting_discrete_values(self, handle: int, setting_name: str) -> str:

        name_bytes = setting_name.encode("utf-8")
        name_c = c_char_p(name_bytes)

        needed = c_uint(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetSettingDiscreteValues(
            c_ulong(handle),
            name_c,
            None,
            c_uint(0),
            byref(needed)
        ))

        size = int(needed.value)
        if size == 0:
            return ""

        buf = create_string_buffer(size + 1)

        wrote = c_uint(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetSettingDiscreteValues(
            c_ulong(handle),
            name_c,
            buf,
            c_uint(size),
            byref(wrote)
        ))

        n = int(wrote.value) if wrote.value != 0 else size

        if n > 0 and buf.raw[n - 1:n] == b"\x00":
            n_for_decode = n - 1
        else:
            n_for_decode = n

        raw = buf.raw[:min(n_for_decode, size)]

        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("utf-8", errors="replace")

        return text

    def get_settings_as_string(self, handle: int, setting_string_format: TLMC_SettingStringFormat, include_read_only_items: bool) -> str:

        needed = c_uint(0)

        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetSettingsAsString(
            c_ulong(handle),
            None,
            c_uint(0),
            byref(needed),
            c_uint8(setting_string_format),
            c_bool(include_read_only_items)
        ))

        size = int(needed.value)
        if size <= 0:
            return ""

        buffer_length = size + 1
        buf = create_string_buffer(buffer_length)

        written = c_uint(0)

        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetSettingsAsString(
            c_ulong(handle),
            byref(buf),
            c_uint(buffer_length),
            byref(written),
            c_uint8(setting_string_format),
            c_bool(include_read_only_items)
        ))

        n = int(written.value) if written.value != 0 else size
        raw = buf.raw[:min(n, size)]

        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("utf-8", errors="replace")

        return text

    def get_status_item(self, handle: int, status_item_id: TLMC_StatusItemId) -> TLMC_StatusItem:
        c_status_item = C_TLMC_StatusItem()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetStatusItem(c_ulong(handle), status_item_id, byref(c_status_item)))
        return MapNativeToPython.status_item(c_status_item)

    def get_status_item_count(self, handle: int) -> int:
        c_count = c_uint16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetStatusItemCount(c_ulong(handle), byref(c_count)))
        return c_count.value

    def get_status_items(self, handle: int, start_index: int, number_of_items: int) -> List[TLMC_StatusItem]:

        if number_of_items <= 0:
            return []

        ArrayType = C_TLMC_StatusItem * number_of_items
        items_buf = ArrayType()
        items_copied = c_uint16(0)

        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetStatusItems(
            c_ulong(handle),
            c_uint16(start_index),
            c_uint16(number_of_items),
            items_buf,
            byref(items_copied)
        ))

        count = min(items_copied.value, number_of_items)
        status_items: List[TLMC_StatusItem] = [MapNativeToPython.status_item(copy.copy(items_buf[i])) for i in range(count)]

        return status_items

    def get_stage_axis_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_StageAxisParams:
        c_params = C_TLMC_StageAxisParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetStageAxisParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.stage_axis_params(c_params)

    def get_stepper_loop_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_StepperLoopParams:
        c_params = C_TLMC_StepperLoopParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetStepperLoopParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.stepper_loop_params(c_params)

    def get_stepper_status(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_StepperStatus:
        c_params = C_TLMC_StepperStatus()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetStepperStatus(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.stepper_status(c_params)

    def get_track_settle_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_TrackSettleParams:
        c_params = C_TLMC_TrackSettleParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetTrackSettleParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))        
        return MapNativeToPython.track_settle_params(c_params)

    def get_trigger_params_for_dc_brushless(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_TriggerParamsForDcBrushless:
        c_params = C_TLMC_TriggerParamsForDcBrushless()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetTriggerParamsForDcBrushless(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.trigger_params_for_dc_brushless(c_params)

    def get_trigger_params_for_stepper(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_TriggerParamsForStepper:
        c_params = C_TLMC_TriggerParamsForStepper()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetTriggerParamsForStepper(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.trigger_params_for_stepper(c_params)

    def get_universal_status(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_UniversalStatus:
        c_params = C_TLMC_UniversalStatus()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetUniversalStatus(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.universal_status(c_params)

    def get_universal_status_bits(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_UniversalStatusBit:
        c_universal_status_bits = c_uint32(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetUniversalStatusBits(
            c_ulong(handle), byref(c_universal_status_bits), c_int64(max_wait_in_milliseconds)))
        return TLMC_UniversalStatusBit(c_universal_status_bits.value)

    def get_velocity_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_VelocityParams:
        c_params = C_TLMC_VelocityParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_GetVelocityParams(c_ulong(handle), byref(
            c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.velocity_params(c_params)

    def home(self, handle: int, max_wait_in_milliseconds: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Home(c_ulong(handle), c_int64(max_wait_in_milliseconds)))

    def identify(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Identify(c_ulong(handle)))

    def load_params(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_LoadParams(c_ulong(handle)))

    def move(self, handle: int, mode: TLMC_MoveMode, param: int, max_wait_in_milliseconds: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Move(
            c_ulong(handle), c_uint8(mode), c_int32(param), c_int64(max_wait_in_milliseconds)))

    def move_absolute(self, handle: int, move_mode: TLMC_MoveMode, position: int, max_wait_in_milliseconds: int) -> None:
        position_val = position

        if move_mode == TLMC_MoveMode.TLMC_MoveMode_AbsoluteToProgrammedPosition:
            position_val = TLMC_Wait.TLMC_Unused
        else:
            move_mode = TLMC_MoveMode.TLMC_MoveMode_Absolute

        self.move(handle, move_mode, position_val, max_wait_in_milliseconds)

    def move_continuous(self, handle: int, direction: TLMC_MoveDirection, max_wait_in_milliseconds: int) -> None:
        if direction == TLMC_MoveDirection.Move_Direction_Reverse:
            move_mode = TLMC_MoveMode.TLMC_MoveMode_ContinuousReverse
        else:
            move_mode = TLMC_MoveMode.TLMC_MoveMode_ContinuousForward
            
        self.move(handle, move_mode, TLMC_Wait.TLMC_Unused, max_wait_in_milliseconds)

    def move_jog(self, handle: int, direction: TLMC_MoveDirection, max_wait_in_milliseconds: int) -> None:

        if direction == TLMC_MoveDirection.Move_Direction_Reverse:
            move_mode = TLMC_MoveMode.TLMC_MoveMode_JogReverse
        else:
            move_mode = TLMC_MoveMode.TLMC_MoveMode_JogForward
        
        self.move(handle, move_mode, TLMC_Wait.TLMC_Unused, max_wait_in_milliseconds)

    def move_relative(self, handle: int, move_mode: TLMC_MoveMode, step_size: int, max_wait_in_milliseconds: int) -> None:
        step_size_val = step_size
        if move_mode == TLMC_MoveMode.TLMC_MoveMode_RelativeByProgrammedDistance:
            step_size_val = TLMC_Wait.TLMC_Unused
        else:
            move_mode = TLMC_MoveMode.TLMC_MoveMode_Relative
        
        self.move(handle, move_mode, step_size_val, max_wait_in_milliseconds)
    
    def open(self, device: str, transport_type: str, operating_mode: TLMC_OperatingMode) -> int:

        device_handle_val = c_ulong(0)

        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Open(
                MapPythonToNative.string(device),
                MapPythonToNative.string(transport_type),
                c_uint32(operating_mode.value),
                byref(device_handle_val)))

        return device_handle_val.value

    def persist_params(self, handle: int, parameter_group_id: TLMC_ParameterGroupId) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PersistParams(c_ulong(handle), parameter_group_id))
    
    def pz_get_kpc_io_settings_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcIoSettingsParams:
        c_params = C_TLMC_PZ_KpcIoSettingsParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetKpcIoSettingsParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_kpc_io_settings_params(c_params)

    def pz_get_kpc_io_trigger_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcIoTriggerParams:
        c_params = C_TLMC_PZ_KpcIoTriggerParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetKpcIoTriggerParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_kpc_io_trigger_params(c_params)

    def pz_get_kpc_mmi_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_KpcMmiParams:
        c_params = C_TLMC_PZ_KpcMmiParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetKpcMmiParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_kpc_mmi_params(c_params)

    def pz_get_lnnx_control_loop_params(self, max_wait_in_milliseconds: int) -> TLMC_PZ_LnnxControlLoopParams:
        c_params = C_TLMC_PZ_LnnxControlLoopParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetLnnxControlLoopParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_lnnx_control_loop_params(c_params)
    
    def pz_get_lnnx_notch_filter_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_LnnxNotchFilterParams:
        c_params = C_TLMC_PZ_LnnxNotchFilterParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetLnnxNotchFilterParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_lnnx_notch_filter_params(c_params)

    def pz_get_max_output_voltage_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_MaxOutputVoltageParams:
        c_params = C_TLMC_PZ_MaxOutputVoltageParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetMaxOutputVoltageParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_max_output_voltage_params(c_params)

    def pz_get_max_travel(self, handle: int, max_wait_in_milliseconds: int) -> int:
        c_max_travel = c_uint16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetMaxTravel(c_ulong(handle), byref(c_max_travel), c_int64(max_wait_in_milliseconds)))
        return c_max_travel.value

    def pz_get_nano_trak_circle_diameter_lookup_table_data(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleDiameterLookupTableData:
        c_params = C_TLMC_PZ_NanoTrakCircleDiameterLookupTableData()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakCircleDiameterLookupTableData(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_circle_diameter_lookup_table_data(c_params)

    def pz_get_nano_trak_circle_home_position(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleHomePositionParams:
        c_params = C_TLMC_PZ_NanoTrakCircleHomePositionParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakCircleHomePosition(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_circle_home_position_params(c_params)

    def pz_get_nano_trak_circle_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakCircleParams:
        c_params = C_TLMC_PZ_NanoTrakCircleParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakCircleParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_circle_params(c_params)

    def pz_get_nano_trak_gain_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakGainParams:
        c_params = C_TLMC_PZ_NanoTrakGainParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakGainParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_gain_params(c_params)

    def pz_get_nano_trak_mode(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakMode:
        c_params = C_TLMC_PZ_NanoTrakMode()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakMode(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_mode(c_params)

    def pz_get_nano_trak_phase_compensation_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakPhaseCompensationParams:
        c_params = C_TLMC_PZ_NanoTrakPhaseCompensationParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakPhaseCompensationParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_phase_compensation_params(c_params)

    def pz_get_nano_trak_range_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakRangeParams:
        c_params = C_TLMC_PZ_NanoTrakRangeParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakRangeParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_range_params(c_params)

    def pz_get_nano_trak_status(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakStatus:
        c_params = C_TLMC_PZ_NanoTrakStatus()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakStatus(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_status(c_params)

    def pz_get_nano_trak_tna_io_settings(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTnaIoSettings:
        c_params = C_TLMC_PZ_NanoTrakTnaIoSettings()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakTnaIoSettings(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_tna_io_settings(c_params)

    def pz_get_nano_trak_track_threshold(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_NanoTrakTrackThresholdParams:
        c_params = C_TLMC_PZ_NanoTrakTrackThresholdParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetNanoTrakTrackThreshold(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_nano_trak_track_threshold(c_params)

    def pz_get_output_voltage(self, handle: int, max_wait_in_milliseconds: int) -> int:
        c_voltage = c_int16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetOutputVoltage(handle, byref(c_voltage), c_int64(max_wait_in_milliseconds)))
        return c_voltage.value

    def pz_get_output_voltage_control_source_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_OutputVoltageControlSourceParams:
        c_params = C_TLMC_PZ_OutputVoltageControlSourceParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetOutputVoltageControlSourceParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_output_voltage_control_source_params(c_params)

    def pz_get_output_waveform_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_OutputWaveformParams:
        c_params = C_TLMC_PZ_OutputWaveformParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetOutputWaveformParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_output_waveform_params(c_params)

    def pz_get_position(self, handle: int, max_wait_in_milliseconds: int) -> int:
        c_position = c_int16(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetPosition(c_ulong(handle), byref(c_position), c_int64(max_wait_in_milliseconds)))
        return c_position.value

    def pz_get_position_control_mode(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionControlMode:
        c_control_mode = c_int8(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetPositionControlMode(c_ulong(handle), byref(c_control_mode), c_int64(max_wait_in_milliseconds)))
        return TLMC_PZ_PositionControlMode(c_control_mode.value)

    def pz_get_position_loop_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_PositionLoopParams:
        c_params = C_TLMC_PZ_PositionLoopParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetPositionLoopParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_position_loop_params(c_params)

    def pz_get_slew_rate_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_SlewRateParams:
        c_params = C_TLMC_PZ_SlewRateParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetSlewRateParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_slew_rate_params(c_params)

    def pz_get_stage_info_params(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_StageInfoParams:
        c_params = C_TLMC_PZ_StageInfoParams()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetStageInfoParams(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_stage_info_params(c_params)

    def pz_get_status(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_Status:
        c_params = C_TLMC_PZ_Status()
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetStatus(c_ulong(handle), byref(c_params), c_int64(max_wait_in_milliseconds)))
        return MapNativeToPython.pz_status(c_params)

    def pz_get_status_bits(self, handle: int, max_wait_in_milliseconds: int) -> TLMC_PZ_StatusBit:
        c_status_bits = c_uint32(0)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_GetStatusBits(c_ulong(handle), byref(c_status_bits), c_int64(max_wait_in_milliseconds)))
        return TLMC_PZ_StatusBit(c_status_bits.value)

    def pz_nano_trak_circle_to_home_position(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_NanoTrakMoveToCircleHomePosition(c_ulong(handle)))
        
    def pz_nano_trak_tia_self_calibrate(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_NanoTrakTiaSelfCalibrate(c_ulong(handle)))

    def pz_set_kpc_io_settings_params(self, handle: int, params: TLMC_PZ_KpcIoSettingsParams) -> None:
        c_params = MapPythonToNative.pz_kpc_io_settings_params(params)        
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetKpcIoSettingsParams(c_ulong(handle), byref(c_params)))

    def pz_set_kpc_io_trigger_params(self, handle: int, params: TLMC_PZ_KpcIoTriggerParams) -> None:
        c_params = MapPythonToNative.pz_kpc_io_trigger_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetKpcIoTriggerParams(c_ulong(handle), byref(c_params)))
    
    def pz_set_kpc_mmi_params(self, handle: int, params: TLMC_PZ_KpcMmiParams) -> None:
        c_params = MapPythonToNative.pz_kpc_mmi_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetKpcMmiParams(c_ulong(handle), byref(c_params)))

    def pz_set_lnnx_control_loop_params(self, handle: int, params: TLMC_PZ_LnnxControlLoopParams) -> None:
        c_params = MapPythonToNative.pz_lnnx_control_loop_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetLnnxControlLoopParams(c_ulong(handle), byref(c_params)))

    def pz_set_lnnx_notch_filter_params(self, handle: int, params: TLMC_PZ_LnnxNotchFilterParams) -> None:
        c_params = MapPythonToNative.pz_lnnx_notch_filter_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetLnnxNotchFilterParams(c_ulong(handle), byref(c_params)))

    def pz_set_max_output_voltage(self, handle: int, max_output_voltage: int) -> None:
        c_voltage = c_uint16(max_output_voltage)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetMaxOutputVoltage(c_ulong(handle), c_voltage))

    def pz_set_max_travel(self, handle: int, max_travel: int) -> None:
        c_max_travel = c_uint16(max_travel)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetMaxTravel(c_ulong(handle), c_max_travel))
    
    def pz_set_nano_trak_circle_diameter(self, handle: int, nano_trak_circle_diameter: int) -> None:
        c_nano_trak_circle_diameter = c_uint16(nano_trak_circle_diameter)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakCircleDiameter(c_ulong(handle), c_nano_trak_circle_diameter))

    def pz_set_nano_trak_circle_diameter_lookup_table_data(self, handle: int, params: TLMC_PZ_NanoTrakCircleDiameterLookupTableData) -> None:
        c_params = MapPythonToNative.pz_nano_trak_circle_diameter_lookup_table_data(params)
        return CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakCircleDiameterLookupTableData(c_ulong(handle), byref(c_params)))

    def pz_set_nano_trak_circle_home_position(self, handle: int, params: TLMC_PZ_NanoTrakCircleHomePositionParams) -> None:
        c_params = MapPythonToNative.pz_nano_trak_circle_home_position_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakCircleHomePosition(c_ulong(handle), byref(c_params)))

    def pz_set_nano_trak_circle_params(self, handle: int, params: TLMC_PZ_NanoTrakCircleParams) -> None:
        c_params = MapPythonToNative.pz_nano_trak_circle_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakCircleParams(c_ulong(handle), byref(c_params)))

    def pz_set_nano_trak_eeprom_params(self, handle: int, params: TLMC_PZ_NanoTrakEEPROMParams) -> None:
        c_params = MapPythonToNative.pz_nano_trak_eeprom_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakEEPROMParams(c_ulong(handle), byref(c_params)))

    def pz_set_nano_trak_gain_params(self, handle: int, params: TLMC_PZ_NanoTrakGainParams) -> None:
        c_params = MapPythonToNative.pz_nano_trak_gain_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakGainParams(c_ulong(handle), byref(c_params)))

    def pz_set_nano_trak_mode(self, handle: int, set_mode: TLMC_PZ_SetNanoTrakModeType) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakMode(c_ulong(handle), c_uint8(int(set_mode))))

    def pz_set_nano_trak_phase_compensation_params(self, handle: int, params: TLMC_PZ_NanoTrakPhaseCompensationParams) -> None:
        c_params = MapPythonToNative.pz_nano_trak_phase_compensation_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakPhaseCompensationParams(c_ulong(handle), byref(c_params)))

    def pz_set_nano_trak_range_params(self, handle: int, params: TLMC_PZ_NanoTrakRangeParams) -> None:
        c_params = MapPythonToNative.pz_nano_trak_range_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakRangeParams(c_ulong(handle), byref(c_params)))

    def pz_set_nano_trak_tna_io_settings(self, handle: int, params: TLMC_PZ_NanoTrakTnaIoSettings) -> None:
        c_params = MapPythonToNative.pz_nano_trak_tna_io_settings(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakTnaIoSettings(c_ulong(handle), byref(c_params)))

    def pz_set_nano_trak_track_threshold(self, handle: int, params: TLMC_PZ_NanoTrakTrackThresholdParams) -> None:
        c_params = MapPythonToNative.pz_nano_trak_track_threshold(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetNanoTrakTrackThreshold(c_ulong(handle), byref(c_params)))

    def pz_set_output_voltage(self, handle: int, new_output_voltage: int) -> None:
        c_voltage = c_int16(new_output_voltage)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetOutputVoltage(c_ulong(handle), c_voltage))

    def pz_set_output_voltage_control_source_params(self, handle: int, params: TLMC_PZ_OutputVoltageControlSourceParams) -> None:
        c_params = MapPythonToNative.pz_output_voltage_control_source_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetOutputVoltageControlSourceParams(c_ulong(handle), byref(c_params)))

    def pz_set_output_waveform_loop_table_sample(self, handle: int, params: TLMC_PZ_OutputWaveformLoopTableSample) -> None:
        c_params = MapPythonToNative.pz_output_waveform_lookup_table_sample(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetOutputWaveformLookupTableSample(c_ulong(handle), byref(c_params)))

    def pz_set_output_waveform_params(self, handle: int, params: TLMC_PZ_OutputWaveformParams) -> None:
        c_params = MapPythonToNative.pz_output_waveform_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetOutputWaveformParams(c_ulong(handle), byref(c_params)))

    def pz_set_position(self, handle: int, new_position: int) -> None:
        c_position = c_int16(new_position)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetPosition(c_ulong(handle), c_position))

    def pz_set_position_control_mode(self, handle: int, control_mode: TLMC_PZ_PositionControlMode, max_wait_in_milliseconds: int) -> None:
        c_control_mode = c_uint8(control_mode)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetPositionControlMode(c_ulong(handle), c_control_mode, c_int64(max_wait_in_milliseconds)))

    def pz_set_position_loop_params(self, handle: int, params: TLMC_PZ_PositionLoopParams) -> None:
        c_params = MapPythonToNative.pz_position_loop_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetPositionLoopParams(c_ulong(handle), byref(c_params)))

    def pz_set_slew_rate_params(self, handle: int, params: TLMC_PZ_SlewRateParams) -> None:
        c_params = MapPythonToNative.pz_slew_rate_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetSlewRateParams(c_ulong(handle), byref(c_params)))

    def pz_set_zero(self, handle: int, max_wait_in_milliseconds: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_SetZero(c_ulong(handle), c_int64(max_wait_in_milliseconds)))

    def pz_start_output_waveform(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_StartOutputWaveform(c_ulong(handle)))

    def pz_stop_output_waveform(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_PZ_StopOutputWaveform(c_ulong(handle)))

    def rack_identify(self, handle: int, channel: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_RackIdentify(c_ulong(handle), c_uint8(channel)))

    def remove_simulation(self, description: str) -> None:
        c_check = MapPythonToNative.string(json.dumps(description))
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_RemoveSimulation(c_check))

    def request_status(self, handle: int,  max_wait_in_milliseconds: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_RequestStatus(c_ulong(handle), c_int64(max_wait_in_milliseconds)))

    def restore_factory_defaults(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_RestoreFactoryDefaults(c_ulong(handle)))

    def send_no_flash_programming(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SendNoFlashProgramming(c_ulong(handle)))

    def send_yes_flash_programming(self, handle: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SendYesFlashProgramming(c_ulong(handle)))

    def set_actuator_type(self, handle: int, actuator_type: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetActuatorType(c_ulong(handle)))

    def set_analog_monitor_configuration_params(self, handle: int, monitor_number: TLMC_AnalogMonitorNumber, params: TLMC_AnalogMonitorConfigurationParams) -> None:
        c_params = MapPythonToNative.analog_monitor_configuration_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetAnalogMonitorConfigurationParams(
            c_ulong(handle), c_uint16(int(monitor_number)), byref(c_params)))

    def set_aux_io_port_mode(self, handle: int, port_number: TLMC_AuxIoPortNumber, port_mode: TLMC_AuxIoPortMode) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.SetAuxIoPortMode(c_ulong(handle), c_uint16(int(port_number)), c_uint16(int(port_mode))))

    def set_aux_io_software_states(self, handle: int, software_states: int) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetAuxIoSoftwareStates(c_ulong(handle), c_uint16(software_states)))

    def set_bow_index(self, handle: int, bow_index: TLMC_BowIndex) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetBowIndex(c_ulong(handle), c_uint16(int(bow_index))))

    def set_button_params(self, handle: int, params: TLMC_ButtonParams) -> None:
        c_params = MapPythonToNative.button_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetButtonParams(c_ulong(handle), byref(c_params)))
     
    def set_connected_product(self, handle: int, product_name: str) -> None:
        c_product_name = MapPythonToNative.string(product_name)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetConnectedProduct(c_ulong(handle), c_product_name))

    def set_connected_product_info(self, handle: int, params: TLMC_ConnectedProductInfo) -> None:
        c_params = MapPythonToNative.connected_product_info(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetConnectedProductInfo(c_ulong(handle), byref(c_params)))

    def set_current_loop_params(self, handle: int, scenario: TLMC_CurrentLoopScenario, params: TLMC_CurrentLoopParams) -> None:
        c_params = MapPythonToNative.current_loop_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetCurrentLoopParams(
            c_ulong(handle), c_uint16(int(scenario)), byref(c_params)))

    def set_dc_pid_params(self, handle: int, params: TLMC_DcPidParams) -> None:
        c_params = MapPythonToNative.dc_pid_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetDcPidParams(c_ulong(handle), byref(c_params)))

    def set_digital_output_states(self, handle: int, output_state: TLMC_DigitalOutput) -> None:
        c_output_state = c_uint8(int(output_state))
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetDigitalOutputStates(c_ulong(handle), c_output_state))

    def set_enable_state(self, handle: int, enable_state: TLMC_EnableState) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetEnableState(c_ulong(handle), enable_state, c_int64(TLMC_Wait.TLMC_InfiniteWait)))

    def set_encoder_counter(self, handle: int, encoder_counter: int) -> None:
        c_encoder_counter = c_int32(encoder_counter)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetEncoderCounter(c_ulong(handle), c_encoder_counter))

    def set_end_of_move_messages_mode(self, handle: int, messages_mode: TLMC_EndOfMoveMessagesMode) -> None:
        c_messages_mode = c_uint8(int(messages_mode))
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetEndOfMoveMessagesMode(c_ulong(handle), c_messages_mode))

    def set_general_move_params(self, handle: int, params: TLMC_GeneralMoveParams) -> None:
        c_params = MapPythonToNative.general_move_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetGeneralMoveParams(c_ulong(handle), byref(c_params)))

    def set_home_params(self, handle: int, params: TLMC_HomeParams) -> None:
        c_params = MapPythonToNative.home_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetHomeParams(handle, byref(c_params)))

    def set_io_configuration_params(self, handle: int, port_number: TLMC_IoPortNumber, params: TLMC_IoConfigurationParams) -> None:
        c_port_number = c_uint16(int(port_number))
        c_params = MapPythonToNative.io_configuration_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetIoConfigurationParams(c_ulong(handle), c_port_number, byref(c_params)))

    def set_io_position_trigger_enable_state(self, handle: int, enable_state: TLMC_IoPositionTriggerEnableState, max_wait_in_milliseconds: int) -> None:
        c_enable_state = c_uint8(int(enable_state))
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetIoPositionTriggerEnableState(c_ulong(handle), c_enable_state, c_int64(max_wait_in_milliseconds)))

    def set_io_trigger_params(self, handle: int, params: TLMC_IoTriggerParams) -> None:
        c_params = MapPythonToNative.io_trigger_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetIoTriggerParams(c_ulong(handle), byref(c_params)))

    def set_jog_params(self, handle: int, params: TLMC_JogParams) -> None:
        c_params = MapPythonToNative.jog_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetJogParams(c_ulong(handle), byref(c_params)))

    def set_joystick_params(self, handle: int, params: TLMC_JoystickParams) -> None:
        c_params = MapPythonToNative.joystick_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetJoystickParams(c_ulong(handle), byref(c_params)))

    def set_joystick_settings_params(self, handle: int, params: TLMC_JoystickSettingsParams) -> None:
        c_params = MapPythonToNative.joystick_settings_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetJoystickSettingsParams(c_ulong(handle), byref(c_params)))

    def set_kcube_io_trigger_params(self, handle: int, params: TLMC_KcubeIoTriggerParams) -> None:
        c_params = MapPythonToNative.kcube_io_trigger_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetKcubeIoTriggerParams(c_ulong(handle), byref(c_params)))

    def set_kcube_mmi_lock_state(self, handle: int, lock_state: TLMC_KcubeMmiLockState) -> None:
        c_lock_state = c_uint8(int(lock_state))
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetKcubeMmiLockState(c_ulong(handle), c_lock_state))

    def set_kcube_mmi_params(self, handle: int, params: TLMC_KcubeMmiParams) -> None:
        c_params = MapPythonToNative.kcube_mmi_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetKcubeMmiParams(c_ulong(handle), byref(c_params)))

    def set_kcube_position_trigger_params(self, handle: int, params: TLMC_KcubePositionTriggerParams) -> None:
        c_params = MapPythonToNative.kcube_position_trigger_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetKcubePositionTriggerParams(c_ulong(handle), byref(c_params)))

    def set_lcd_display_params(self, handle: int, params: TLMC_LcdDisplayParams) -> None:
        c_params = MapPythonToNative.lcd_display_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetLcdDisplayParams(c_ulong(handle), byref(c_params)))

    def set_lcd_move_params(self, handle: int, params: TLMC_LcdMoveParams) -> None:
        c_params = MapPythonToNative.lcd_move_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetLcdMoveParams(c_ulong(handle), byref(c_params)))

    def set_limit_switch_params(self, handle: int, params: TLMC_LimitSwitchParams) -> None:
        c_params = MapPythonToNative.limit_switch_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetLimitSwitchParams(c_ulong(handle), byref(c_params)))

    def set_monitor_output_params(self, handle: int, params: TLMC_MonitorOutputParams) -> None:
        c_params = MapPythonToNative.monitor_output_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetMonitorOutputParams(c_ulong(handle), byref(c_params)))

    def set_motor_output_params(self, handle: int, params: TLMC_MotorOutputParams) -> None:
        c_params = MapPythonToNative.motor_output_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetMotorOutputParams(c_ulong(handle), byref(c_params)))

    def set_move_absolute_params(self, handle: int, params: TLMC_MoveAbsoluteParams) -> None:
        c_params = MapPythonToNative.move_absolute_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetMoveAbsoluteParams(c_ulong(handle), byref(c_params)))

    def set_move_relative_params(self, handle: int, params: TLMC_MoveRelativeParams) -> None:
        c_params = MapPythonToNative.move_relative_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetMoveRelativeParams(c_ulong(handle), byref(c_params)))

    def set_position_counter(self, handle: int, position_counter: int) -> None:
        c_position_counter = c_int32(position_counter)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetPositionCounter(c_ulong(handle), c_position_counter))

    def set_position_loop_params(self, handle: int, scenario: TLMC_PositionLoopScenario, params: TLMC_PositionLoopParams) -> None:
        c_scenario = c_uint16(int(scenario))
        c_params = MapPythonToNative.position_loop_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetPositionLoopParams(c_ulong(handle), c_scenario, byref(c_params)))

    def set_potentiometer_params(self, handle: int, params: TLMC_PotentiometerParams) -> None:
        c_params = MapPythonToNative.potentiometer_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetPotentiometerParams(c_ulong(handle), byref(c_params)))

    def set_power_params(self, handle: int, params: TLMC_PowerParams) -> None:
        c_params = MapPythonToNative.power_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetPowerParams(c_ulong(handle), byref(c_params)))

    def set_profile_mode_params(self, handle: int, params: TLMC_ProfileModeParams) -> None:
        c_params = MapPythonToNative.profile_mode_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetProfileModeParams(c_ulong(handle), byref(c_params)))

    def set_setting(self, handle: int, setting_name: str, value: TLMC_Value) -> None:
        c_setting_name = MapPythonToNative.string(setting_name)
        c_value = MapPythonToNative.value(value)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetSetting(c_ulong(handle), c_setting_name, c_value))

    def set_settings_from_string(self, handle: int, settings: str) -> None:
        c_settings = MapPythonToNative.string(settings)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetSettingsFromString(c_ulong(handle), c_settings))

    def set_stage_axis_params(self, handle: int, params: TLMC_StageAxisParams) -> None:
        c_params = MapPythonToNative.stage_axis_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetStageAxisParams(c_ulong(handle), byref(c_params)))

    def set_status_mode(self, handle: int, operating_mode: TLMC_OperatingMode) -> None:
        c_operating_mode = c_uint32(int(operating_mode))
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetStatusMode(c_ulong(handle), c_operating_mode))

    def set_stepper_loop_params(self, handle: int, params: TLMC_StepperLoopParams) -> None:
        c_params = MapPythonToNative.stepper_loop_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetStepperLoopParams(c_ulong(handle), byref(c_params)))

    def set_track_settle_params(self, handle: int, params: TLMC_TrackSettleParams) -> None:
        c_params = MapPythonToNative.track_settle_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetTrackSettleParams(c_ulong(handle), byref(c_params)))

    def set_trigger_params_for_dc_brushless(self, handle: int, params: TLMC_TriggerParamsForDcBrushless) -> None:
        c_params = MapPythonToNative.trigger_params_for_dc_brushless(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetTriggerParamsForDcBrushless(c_ulong(handle), byref(c_params)))

    def set_trigger_params_for_stepper(self, handle: int, params: TLMC_TriggerParamsForStepper) -> None:
        c_params = MapPythonToNative.trigger_params_for_stepper(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetTriggerParamsForStepper(c_ulong(handle), byref(c_params)))

    def set_velocity_params(self, handle: int, params: TLMC_VelocityParams) -> None:
        c_params = MapPythonToNative.velocity_params(params)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_SetVelocityParams(c_ulong(handle), byref(c_params)))

    def shutdown(self) -> None:
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Shutdown())

    def startup(self, settings_file_name: Optional[str]) -> None:
        if settings_file_name is None:
            CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Startup(None))
            return
        
        c_settings_file_name = MapPythonToNative.string(settings_file_name)
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Startup(c_settings_file_name))

    def stop(self, handle: int, stop_mode: TLMC_StopMode, max_wait_in_milliseconds: int) -> None:
        c_stop_mode = c_uint8(int(stop_mode))
        CNativeFunctions.wrap_error_code(self.xa_lib.TLMC_Stop(handle, c_stop_mode, c_int64(max_wait_in_milliseconds)))
