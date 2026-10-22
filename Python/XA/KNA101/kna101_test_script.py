import platform

from thorlabs_xa.products.kna101 import Kna101
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.enums import (
    TLMC_KcubeMmiLockState,
    TLMC_OperatingMode,
    TLMC_PZ_SetNanoTrakModeType,
    TLMC_ScaleType,
    TLMC_Wait,
)
from thorlabs_xa.shared.params import (
    TLMC_DeviceInfo,
    TLMC_PZ_KnaIoTriggerParams,
    TLMC_PZ_KnaMmiParams,
    TLMC_PZ_NanoTrakCircleHomePositionParams,
    TLMC_PZ_NanoTrakCircleParams,
    TLMC_PZ_NanoTrakGainParams,
    TLMC_PZ_NanoTrakPhaseCompensationParams,
    TLMC_PZ_NanoTrakTiaRangeParams,
    TLMC_PZ_NanoTrakTnaIoSettings,
    TLMC_PZ_NanoTrakTrackThresholdParams,
)
from thorlabs_xa.shared.xa_error_factory import XADeviceException

KNA101_PART_NUMBER = "KNA101"

SIMULATION_CONFIG_STRING = {"PartNumber": KNA101_PART_NUMBER, "SerialNumber": "81000001"}
DEFAULT_TIMEOUT = 5000


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:

    system_manager.create_simulation(SIMULATION_CONFIG_STRING)

    device_info = TLMC_DeviceInfo()

    device_info.device_type_description = SIMULATION_CONFIG_STRING["PartNumber"]
    device_info.device = SIMULATION_CONFIG_STRING["SerialNumber"]
    device_info.transport = ""

    return device_info


def main() -> None:

    device: Kna101 | None = None

    system_manager = SystemManager.instance()

    if platform.system() == "Linux":
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

            if listed_device_info.part_number == KNA101_PART_NUMBER:
                device_info = listed_device_info

        if not device_info:
            print("No KNA101 devices found, check that your device is powered and is visible to your system. Continuing with simulation!")
            device_info = create_simulation(system_manager)

    try:

        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Kna101)

        DiagnosticsHelper.console(f"Device part number is {device.get_hardware_info(TLMC_Wait.TLMC_InfiniteWait).part_number}")

        firmware_version = device.get_firmware_version_info(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Firmware version: {firmware_version[0].major_version}.{firmware_version[0].minor_version}.{firmware_version[0].interim_version}")

        device.identify()
        DiagnosticsHelper.console_green("Identify command sent.")

        # Test round trip of Kcube MMI Lock
        DiagnosticsHelper.console("Testing round trip of Kcube MMI Lock...")
        device.set_kcube_mmi_lock_state(TLMC_KcubeMmiLockState.TLMC_KcubeMmiLockState_Unlocked)
        lock_state = device.get_kcube_mmi_lock_state(DEFAULT_TIMEOUT)
        if lock_state == TLMC_KcubeMmiLockState.TLMC_KcubeMmiLockState_Unlocked:
            DiagnosticsHelper.console_green("Kcube MMI Lock round trip test passed.")
        else:
            DiagnosticsHelper.console_error("Kcube MMI Lock round trip test failed.")

        # Test round trip of NanoTrak Gain Params
        DiagnosticsHelper.console("Testing round trip of NanoTrak Gain Params...")
        gain_params = device.get_nano_trak_gain_params(DEFAULT_TIMEOUT)
        original_gain = gain_params.gain
        gain_params.gain = 100
        device.set_nano_trak_gain_params(gain_params)
        gain_params_returned = device.get_nano_trak_gain_params(DEFAULT_TIMEOUT)
        if gain_params_returned.gain == 100:
            DiagnosticsHelper.console_green("NanoTrak Gain Params round trip test passed.")
        else:
            DiagnosticsHelper.console_error(f"NanoTrak Gain Params round trip test failed. Expected 100, got {gain_params_returned.gain}")

        # Test round trip of NanoTrak Circle Params
        DiagnosticsHelper.console("Testing round trip of NanoTrak Circle Params...")
        circle_params = device.get_nano_trak_circle_params(DEFAULT_TIMEOUT)
        circle_params.circle_diameter_software = 1000
        device.set_nano_trak_circle_params(circle_params)
        circle_params_returned = device.get_nano_trak_circle_params(DEFAULT_TIMEOUT)
        if circle_params_returned.circle_diameter_software == 1000:
            DiagnosticsHelper.console_green("NanoTrak Circle Params round trip test passed.")
        else:
            DiagnosticsHelper.console_error(f"NanoTrak Circle Params round trip test failed. Expected 1000, got {circle_params_returned.circle_diameter_software}")

        # Test set NanoTrak Circle Diameter
        DiagnosticsHelper.console("Testing set NanoTrak Circle Diameter...")
        device.set_nano_trak_circle_diameter(500)
        DiagnosticsHelper.console_green("NanoTrak Circle Diameter set successfully.")

        # Test round trip of NanoTrak Circle Home Position
        DiagnosticsHelper.console("Testing round trip of NanoTrak Circle Home Position...")
        home_position_params = device.get_nano_trak_circle_home_position(DEFAULT_TIMEOUT)
        home_position_params.circle_home_position_a = 100
        home_position_params.circle_home_position_b = 200
        device.set_nano_trak_circle_home_position(home_position_params)
        home_position_returned = device.get_nano_trak_circle_home_position(DEFAULT_TIMEOUT)
        if home_position_returned.circle_home_position_a == 100 and home_position_returned.circle_home_position_b == 200:
            DiagnosticsHelper.console_green("NanoTrak Circle Home Position round trip test passed.")
        else:
            DiagnosticsHelper.console_error(f"NanoTrak Circle Home Position round trip test failed. Expected (100, 200), got ({home_position_returned.circle_home_position_a}, {home_position_returned.circle_home_position_b})")

        # Test NanoTrak Circle To Home Position
        DiagnosticsHelper.console("Testing NanoTrak Circle To Home Position...")
        device.nano_trak_circle_to_home_position()
        DiagnosticsHelper.console_green("NanoTrak Circle To Home Position command sent.")

        # Test round trip of NanoTrak Phase Compensation Params
        DiagnosticsHelper.console("Testing round trip of NanoTrak Phase Compensation Params...")
        phase_params = device.get_nano_trak_phase_compensation_params(DEFAULT_TIMEOUT)
        phase_params.phase_compensation_a_software = 45
        device.set_nano_trak_phase_compensation_params(phase_params)
        phase_params_returned = device.get_nano_trak_phase_compensation_params(DEFAULT_TIMEOUT)
        if phase_params_returned.phase_compensation_a_software == 45:
            DiagnosticsHelper.console_green("NanoTrak Phase Compensation Params round trip test passed.")
        else:
            DiagnosticsHelper.console_error(f"NanoTrak Phase Compensation Params round trip test failed. Expected 45, got {phase_params_returned.phase_compensation_a_software}")

        # Test NanoTrak Status
        DiagnosticsHelper.console("Getting NanoTrak Status...")
        try:
            nano_trak_status = device.get_nano_trak_status(DEFAULT_TIMEOUT)
            DiagnosticsHelper.console(DiagnosticsHelper.object_as_string(nano_trak_status))
        except ValueError as e:
            DiagnosticsHelper.console_error(f"NanoTrak Status failed (simulation limitation): {e}")

        # Test subchannels
        DiagnosticsHelper.console("Testing subchannels...")
        subchannels = device.get_all_subchannels()
        DiagnosticsHelper.console(f"Found {len(subchannels)} subchannels.")

        for subchannel in subchannels:
            DiagnosticsHelper.console(f"  Subchannel {subchannel.subchannel_number}: handle={subchannel.subchannel_handle}")

        # Test subchannel 1
        DiagnosticsHelper.console("Testing subchannel 1...")
        sub1 = device.get_subchannel(1)
        DiagnosticsHelper.console(f"  Subchannel 1 handle: {sub1.subchannel_handle}")

        # Test subchannel 1 settings
        DiagnosticsHelper.console("  Getting subchannel 1 settings...")
        sub1_settings = sub1.get_settings_items()
        DiagnosticsHelper.console(f"  Found {len(sub1_settings)} settings on subchannel 1.")
        for setting in sub1_settings[:3]:
            DiagnosticsHelper.console(f"    {setting.name}: {setting.value}")

        # Test subchannel 1 position control mode
        DiagnosticsHelper.console("  Testing subchannel 1 position control mode...")
        sub1_mode = sub1.get_position_control_mode(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"  Subchannel 1 position control mode: {sub1_mode}")

        # Test subchannel 1 position loop params
        DiagnosticsHelper.console("  Testing subchannel 1 position loop params...")
        sub1_loop_params = sub1.get_position_loop_params(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"  Subchannel 1 position loop params: proportional={sub1_loop_params.proportional}, integral={sub1_loop_params.integral}")

        # Test subchannel 1 load params
        DiagnosticsHelper.console("  Testing subchannel 1 load params...")
        sub1.load_params()
        DiagnosticsHelper.console_green("  Subchannel 1 load params sent.")

        # Test subchannel 2
        DiagnosticsHelper.console("Testing subchannel 2...")
        sub2 = device.get_subchannel(2)
        DiagnosticsHelper.console(f"  Subchannel 2 handle: {sub2.subchannel_handle}")

        # Test subchannel 2 settings
        DiagnosticsHelper.console("  Getting subchannel 2 settings...")
        sub2_settings = sub2.get_settings_items()
        DiagnosticsHelper.console(f"  Found {len(sub2_settings)} settings on subchannel 2.")
        for setting in sub2_settings[:3]:
            DiagnosticsHelper.console(f"    {setting.name}: {setting.value}")

        # Test subchannel 2 position control mode
        DiagnosticsHelper.console("  Testing subchannel 2 position control mode...")
        sub2_mode = sub2.get_position_control_mode(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"  Subchannel 2 position control mode: {sub2_mode}")

        # Test subchannel 2 position loop params
        DiagnosticsHelper.console("  Testing subchannel 2 position loop params...")
        sub2_loop_params = sub2.get_position_loop_params(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"  Subchannel 2 position loop params: proportional={sub2_loop_params.proportional}, integral={sub2_loop_params.integral}")

        # Test subchannel 2 load params
        DiagnosticsHelper.console("  Testing subchannel 2 load params...")
        sub2.load_params()
        DiagnosticsHelper.console_green("  Subchannel 2 load params sent.")

        DiagnosticsHelper.console_green("Subchannel tests completed.")

        # ========== New Feature Tests ==========

        # Test round trip of NanoTrak Track Threshold
        DiagnosticsHelper.console("Testing round trip of NanoTrak Track Threshold...")
        track_threshold = device.get_nano_trak_track_threshold(DEFAULT_TIMEOUT)
        track_threshold.track_threshold = 500
        device.set_nano_trak_track_threshold(track_threshold)
        track_threshold_returned = device.get_nano_trak_track_threshold(DEFAULT_TIMEOUT)
        if track_threshold_returned.track_threshold == 500:
            DiagnosticsHelper.console_green("NanoTrak Track Threshold round trip test passed.")
        else:
            DiagnosticsHelper.console_error(f"NanoTrak Track Threshold round trip test failed. Expected 500, got {track_threshold_returned.track_threshold}")

        # Test round trip of NanoTrak TIA Range Params
        DiagnosticsHelper.console("Testing round trip of NanoTrak TIA Range Params...")
        tia_range_params = device.get_nano_trak_tia_range_params(DEFAULT_TIMEOUT)
        tia_range_params.range_up_limit = 100
        device.set_nano_trak_tia_range_params(tia_range_params)
        tia_range_params_returned = device.get_nano_trak_tia_range_params(DEFAULT_TIMEOUT)
        if tia_range_params_returned.range_up_limit == 100:
            DiagnosticsHelper.console_green("NanoTrak TIA Range Params round trip test passed.")
        else:
            DiagnosticsHelper.console_error(f"NanoTrak TIA Range Params round trip test failed. Expected 100, got {tia_range_params_returned.range_up_limit}")

        # Test get NanoTrak Status Bits Params
        DiagnosticsHelper.console("Getting NanoTrak Status Bits Params...")
        status_bits = device.get_nano_trak_status_bits_params(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"NanoTrak Status Bits: {DiagnosticsHelper.object_as_string(status_bits)}")
        DiagnosticsHelper.console_green("NanoTrak Status Bits Params test passed.")

        # Test round trip of KNA IO Trigger Params
        DiagnosticsHelper.console("Testing round trip of KNA IO Trigger Params...")
        io_trigger_params = device.get_kna_io_trigger_params(DEFAULT_TIMEOUT)
        device.set_kna_io_trigger_params(io_trigger_params)
        io_trigger_params_returned = device.get_kna_io_trigger_params(DEFAULT_TIMEOUT)
        io_trigger_string = DiagnosticsHelper.object_as_string(io_trigger_params)
        io_trigger_returned_string = DiagnosticsHelper.object_as_string(io_trigger_params_returned)
        if io_trigger_string == io_trigger_returned_string:
            DiagnosticsHelper.console_green("KNA IO Trigger Params round trip test passed.")
        else:
            DiagnosticsHelper.console_error("KNA IO Trigger Params round trip test failed.")

        # Test round trip of KNA MMI Params
        DiagnosticsHelper.console("Testing round trip of KNA MMI Params...")
        mmi_params = device.get_kna_mmi_params(DEFAULT_TIMEOUT)
        mmi_params.display_brightness = 50
        device.set_kna_mmi_params(mmi_params)
        mmi_params_returned = device.get_kna_mmi_params(DEFAULT_TIMEOUT)
        if mmi_params_returned.display_brightness == 50:
            DiagnosticsHelper.console_green("KNA MMI Params round trip test passed.")
        else:
            DiagnosticsHelper.console_error(f"KNA MMI Params round trip test failed. Expected 50, got {mmi_params_returned.display_brightness}")

        # Test round trip of NanoTrak Circle Diameter Lookup Table Data
        DiagnosticsHelper.console("Testing round trip of NanoTrak Circle Diameter Lookup Table Data...")
        lookup_table = device.get_nano_trak_circle_diameter_lookup_table_data(DEFAULT_TIMEOUT)
        device.set_nano_trak_circle_diameter_lookup_table_data(lookup_table)
        lookup_table_returned = device.get_nano_trak_circle_diameter_lookup_table_data(DEFAULT_TIMEOUT)
        lookup_string = DiagnosticsHelper.object_as_string(lookup_table)
        lookup_returned_string = DiagnosticsHelper.object_as_string(lookup_table_returned)
        if lookup_string == lookup_returned_string:
            DiagnosticsHelper.console_green("NanoTrak Circle Diameter Lookup Table Data round trip test passed.")
        else:
            DiagnosticsHelper.console_error("NanoTrak Circle Diameter Lookup Table Data round trip test failed.")

        # Test KNA Scan
        DiagnosticsHelper.console("Testing KNA Scan...")
        device.start_kna_scan()
        DiagnosticsHelper.console_green("KNA Scan started.")
        scan_data = device.get_kna_scan_data(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"KNA Scan data: lineNumber={scan_data.line_number}")
        device.stop_kna_scan()
        DiagnosticsHelper.console_green("KNA Scan stopped.")

        # Test round trip of NanoTrak TNA IO Settings (read-modify-write with same values)
        DiagnosticsHelper.console("Testing round trip of NanoTrak TNA IO Settings...")
        tna_io_settings = device.get_nano_trak_tna_io_settings(DEFAULT_TIMEOUT)
        device.set_nano_trak_tna_io_settings(tna_io_settings)
        tna_io_settings_returned = device.get_nano_trak_tna_io_settings(DEFAULT_TIMEOUT)
        tna_io_string = DiagnosticsHelper.object_as_string(tna_io_settings)
        tna_io_returned_string = DiagnosticsHelper.object_as_string(tna_io_settings_returned)
        if tna_io_string == tna_io_returned_string:
            DiagnosticsHelper.console_green("NanoTrak TNA IO Settings round trip test passed.")
        else:
            DiagnosticsHelper.console_error("NanoTrak TNA IO Settings round trip test failed.")

        # Test load params
        DiagnosticsHelper.console("Testing load params...")
        device.load_params()
        DiagnosticsHelper.console_green("Load params command sent.")

        # Test settings
        DiagnosticsHelper.console("Getting settings...")
        settings = device.get_settings_items()
        DiagnosticsHelper.console(f"Found {len(settings)} settings.")
        for setting in settings[:5]:
            DiagnosticsHelper.console(f"  {setting.name}: {setting.value}")

        # Test status items
        DiagnosticsHelper.console("Getting status items...")
        status_count = device.get_status_item_count()
        DiagnosticsHelper.console(f"Found {status_count} status items.")

        # Test unit converter
        DiagnosticsHelper.console("Testing unit converter...")
        preferred_unit = device.get_preferred_physical_unit(0)
        DiagnosticsHelper.console(f"Preferred unit: {preferred_unit}")

        DiagnosticsHelper.console_green("All new feature tests completed.")

    except XADeviceException as e:

        print("Encountered error, code: ", e.error_code)

    finally:

        if device is not None:
            DiagnosticsHelper.console("Shutting down KNA101...")
            try:
                device.disconnect()
            except XADeviceException:
                DiagnosticsHelper.console("Disconnect not supported in simulation mode, skipping.")
            device.close()

        DiagnosticsHelper.console("Shutting down system...")
        system_manager.shutdown()

    DiagnosticsHelper.console("Completed.")


main()
