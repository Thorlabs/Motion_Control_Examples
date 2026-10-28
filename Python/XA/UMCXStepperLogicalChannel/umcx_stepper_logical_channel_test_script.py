import platform

from thorlabs_xa.products.umcx_stepper_logical_channel import UmcxStepperLogicalChannel
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import (
    TLMC_BowIndex,
    TLMC_DigitalOutput,
    TLMC_EnableState,
    TLMC_MoveMode,
    TLMC_OperatingMode,
    TLMC_SettingStringFormat,
    TLMC_StopMode,
)
from thorlabs_xa.shared.params import (
    TLMC_DeviceInfo,
    TLMC_GeneralMoveParams,
    TLMC_MoveAbsoluteParams,
    TLMC_MoveRelativeParams,
    TLMC_VelocityParams,
)
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException

UMCX_PART_NUMBER = "UMC1"
UMCX_SERIAL_NUMBER = "121000002"
UMCX_STEPPER_CHANNEL_SERIAL_NUMBER = "127000003"
DEFAULT_TIMEOUT = 5000

SIMULATION_CONFIG_STRING = {
    "PartNumber": UMCX_PART_NUMBER,
    "SerialNumber": UMCX_SERIAL_NUMBER,
    "Channels": [
        {
            "BayNumber": 1,
            "SerialNumber": UMCX_STEPPER_CHANNEL_SERIAL_NUMBER,
            "ActuatorType": "DDS220",
        }
    ],
}


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:
    system_manager.create_simulation(SIMULATION_CONFIG_STRING)

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = "UMCX Stepper Logical Channel"
    device_info.device = UMCX_STEPPER_CHANNEL_SERIAL_NUMBER
    device_info.transport = UMCX_SERIAL_NUMBER

    return device_info


def main() -> None:
    device: UmcxStepperLogicalChannel | None = None

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
            print(f"{listed_device_info.device_type_description}:{listed_device_info.device} found at {listed_device_info.transport} ({listed_device_info.part_number})")

            is_known_serial = listed_device_info.device == UMCX_STEPPER_CHANNEL_SERIAL_NUMBER
            is_stepper_description = "stepper" in listed_device_info.device_type_description.lower()

            if is_known_serial or is_stepper_description:
                device_info = listed_device_info

        if not device_info:
            print("No UMCX stepper logical channel devices found, continuing with simulation!")
            device_info = create_simulation(system_manager)

    try:
        device = system_manager.open_device_as(
            device_info.device,
            device_info.transport,
            TLMC_OperatingMode.TLMC_OperatingMode_Default,
            UmcxStepperLogicalChannel,
        )

        DiagnosticsHelper.console("Enabling UMCX stepper logical channel...")
        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        enable_state = device.get_enable_state(DEFAULT_TIMEOUT)
        if enable_state == TLMC_EnableState.TLMC_Enabled:
            DiagnosticsHelper.console_green("UMCX stepper logical channel enabled.")
        else:
            DiagnosticsHelper.console_error("UMCX stepper logical channel not enabled as expected.")

        DiagnosticsHelper.console("Identifying device...")
        device.identify()

        DiagnosticsHelper.console("Getting hardware info...")
        DiagnosticsHelper.console_object(device.get_hardware_info(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console("Testing round trip of digital output states...")
        digital_output = TLMC_DigitalOutput.TLMC_DigitalOutput_1
        device.set_digital_output_states(digital_output)

        digital_output_returned = device.get_digital_output_states(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Sent: {digital_output}")
        DiagnosticsHelper.console(f"Received: {digital_output_returned}")

        if digital_output == digital_output_returned:
            DiagnosticsHelper.console_green("Digital output states round trip test passed.")
        else:
            DiagnosticsHelper.console_error("Digital output states round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of bow index...")
        bow_index = TLMC_BowIndex.TLMC_BowIndex_SCurve2
        device.set_bow_index(bow_index)

        bow_index_returned = device.get_bow_index(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Sent: {bow_index}")
        DiagnosticsHelper.console(f"Received: {bow_index_returned}")

        if bow_index == bow_index_returned:
            DiagnosticsHelper.console_green("Bow index round trip test passed.")
        else:
            DiagnosticsHelper.console_error("Bow index round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of encoder counter...")
        encoder_counter = 1234
        device.set_encoder_counter(encoder_counter)

        encoder_counter_returned = device.get_encoder_counter(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Sent: {encoder_counter}")
        DiagnosticsHelper.console(f"Received: {encoder_counter_returned}")

        if encoder_counter == encoder_counter_returned:
            DiagnosticsHelper.console_green("Encoder counter round trip test passed.")
        else:
            DiagnosticsHelper.console_error("Encoder counter round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of general move params...")
        general_move_params = TLMC_GeneralMoveParams()
        general_move_params.backlash_distance = 80

        device.set_general_move_params(general_move_params)
        general_move_params_returned = device.get_general_move_params(DEFAULT_TIMEOUT)

        sent_general_move_params = DiagnosticsHelper.object_as_string(general_move_params)
        received_general_move_params = DiagnosticsHelper.object_as_string(general_move_params_returned)

        DiagnosticsHelper.console(f"Sent: {sent_general_move_params}")
        DiagnosticsHelper.console(f"Received: {received_general_move_params}")

        if sent_general_move_params == received_general_move_params:
            DiagnosticsHelper.console_green("General move params round trip test passed.")
        else:
            DiagnosticsHelper.console_error("General move params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of velocity params...")
        velocity_params = TLMC_VelocityParams()
        velocity_params.acceleration = 180
        velocity_params.max_velocity = 280
        velocity_params.min_velocity = 0

        device.set_velocity_params(velocity_params)
        velocity_params_returned = device.get_velocity_params(DEFAULT_TIMEOUT)

        sent_velocity_params = DiagnosticsHelper.object_as_string(velocity_params)
        received_velocity_params = DiagnosticsHelper.object_as_string(velocity_params_returned)

        DiagnosticsHelper.console(f"Sent: {sent_velocity_params}")
        DiagnosticsHelper.console(f"Received: {received_velocity_params}")

        if sent_velocity_params == received_velocity_params:
            DiagnosticsHelper.console_green("Velocity params round trip test passed.")
        else:
            DiagnosticsHelper.console_error("Velocity params round trip test failed.")

        DiagnosticsHelper.console("Testing round trip of move absolute params...")
        move_absolute_params = TLMC_MoveAbsoluteParams()
        move_absolute_params.absolute_position = 400

        device.set_move_absolute_params(move_absolute_params)
        move_absolute_params_returned = device.get_move_absolute_params(DEFAULT_TIMEOUT)

        sent_move_absolute_params = DiagnosticsHelper.object_as_string(move_absolute_params)
        received_move_absolute_params = DiagnosticsHelper.object_as_string(move_absolute_params_returned)

        DiagnosticsHelper.console(f"Sent: {sent_move_absolute_params}")
        DiagnosticsHelper.console(f"Received: {received_move_absolute_params}")

        if sent_move_absolute_params == received_move_absolute_params:
            DiagnosticsHelper.console_green("Move absolute params round trip test passed.")
        else:
            DiagnosticsHelper.console_error("Move absolute params round trip test failed.")

        device.move(TLMC_MoveMode.TLMC_MoveMode_AbsoluteToProgrammedPosition, 0, DEFAULT_TIMEOUT)

        DiagnosticsHelper.console("Testing round trip of move relative params...")
        move_relative_params = TLMC_MoveRelativeParams()
        move_relative_params.relative_distance = 200

        device.set_move_relative_params(move_relative_params)
        move_relative_params_returned = device.get_move_relative_params(DEFAULT_TIMEOUT)

        sent_move_relative_params = DiagnosticsHelper.object_as_string(move_relative_params)
        received_move_relative_params = DiagnosticsHelper.object_as_string(move_relative_params_returned)

        DiagnosticsHelper.console(f"Sent: {sent_move_relative_params}")
        DiagnosticsHelper.console(f"Received: {received_move_relative_params}")

        if sent_move_relative_params == received_move_relative_params:
            DiagnosticsHelper.console_green("Move relative params round trip test passed.")
        else:
            DiagnosticsHelper.console_error("Move relative params round trip test failed.")

        device.move(TLMC_MoveMode.TLMC_MoveMode_RelativeByProgrammedDistance, 0, DEFAULT_TIMEOUT)

        position_counter = device.get_position_counter(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Position counter: {position_counter}")

        DiagnosticsHelper.console("Requesting status and reading UMC status...")
        device.request_status(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console_object(device.get_umc_status(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console("Reading stepper loop params...")
        DiagnosticsHelper.console_object(device.get_stepper_loop_params(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console("Getting universal status bits...")
        DiagnosticsHelper.console_object(device.get_universal_status_bits(DEFAULT_TIMEOUT))

        DiagnosticsHelper.console("Getting settings JSON...")
        json_settings = device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True)
        DiagnosticsHelper.console(json_settings)

        DiagnosticsHelper.console("Stopping device...")
        device.stop(TLMC_StopMode.TLMC_StopMode_Immediate, DEFAULT_TIMEOUT)

    except XADeviceException as e:
        print("Encountered error, code:", e.error_code)

    finally:
        if device:
            DiagnosticsHelper.console("Shutting down UMCX stepper logical channel...")
            device.close()

        DiagnosticsHelper.console("Shutting down system...")
        system_manager.shutdown()

    DiagnosticsHelper.console("Completed.")


if __name__ == "__main__":
    main()
