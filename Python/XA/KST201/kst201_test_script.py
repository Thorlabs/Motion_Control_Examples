import time
import platform

from thorlabs_xa.products.kst201 import Kst201
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.enums import (
    TLMC_EnableState,
    TLMC_OperatingMode,
    TLMC_MoveMode,
    TLMC_SettingStringFormat,
    TLMC_StopMode
)
from thorlabs_xa.shared.params import (
    TLMC_DeviceInfo,
)
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.xa_error_factory import XADeviceException


KST201_PART_NUMBER = "KST201"
DEFAULT_TIMEOUT = 5000

SIMULATION_CONFIG = {
    "PartNumber": KST201_PART_NUMBER,
    "SerialNumber": "26000001",
    "ActuatorType": "FW103",
}


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo:
    system_manager.create_simulation(SIMULATION_CONFIG)

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = SIMULATION_CONFIG["PartNumber"]
    device_info.device = SIMULATION_CONFIG["SerialNumber"]
    device_info.transport = ""

    return device_info


def main() -> None:
    device: Kst201 | None = None
    system_manager = SystemManager.instance()

    # Startup
    if platform.system() == "Linux":
        system_manager.startup("deviceDiscovery.connections=/dev/ttyUSB0")
    else:
        system_manager.startup()

    devices = system_manager.get_device_list()
    device_info: TLMC_DeviceInfo | None = None

    # Discover devices
    if not devices:
        print("No devices found — using simulation.")
        device_info = create_simulation(system_manager)
    else:
        print("Devices found:")
        for d in devices:
            print(f"{d.device_type_description}:{d.device} ({d.part_number})")
            if d.part_number == KST201_PART_NUMBER:
                device_info = d

        if not device_info:
            print("No KST201 found — using simulation.")
            device_info = create_simulation(system_manager)

    try:
        # Open device
        device = system_manager.open_device_as(
            device_info.device,
            device_info.transport,
            TLMC_OperatingMode.TLMC_OperatingMode_Default,
            Kst201
        )

        # Enable
        DiagnosticsHelper.console("Enabling KST201...")
        device.set_enable_state(TLMC_EnableState.TLMC_Enabled)

        if device.get_enable_state(DEFAULT_TIMEOUT) == TLMC_EnableState.TLMC_Enabled:
            DiagnosticsHelper.console_green("Device enabled.")
        else:
            DiagnosticsHelper.console_error("Failed to enable.")

        # Identify
        DiagnosticsHelper.console("Identifying device...")
        device.identify()

        # Hardware info
        hw = device.get_hardware_info(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console_object(hw)

        # --- HOME ---
        DiagnosticsHelper.console("Homing...")
        device.home(DEFAULT_TIMEOUT)

        # --- ABSOLUTE MOVE ---
        DiagnosticsHelper.console("Testing absolute move...")

        device.move(
            TLMC_MoveMode.TLMC_MoveMode_Absolute,
            10000,
            DEFAULT_TIMEOUT
        )

        time.sleep(2)

        position = device.get_position_counter(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Position after move: {position}")

        # --- RELATIVE MOVE ---
        DiagnosticsHelper.console("Testing relative move...")

        device.move(
            TLMC_MoveMode.TLMC_MoveMode_Relative,
            -2000,
            DEFAULT_TIMEOUT
        )

        time.sleep(2)

        position = device.get_position_counter(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Position after relative move: {position}")

        # --- STOP TEST ---
        DiagnosticsHelper.console("Testing stop...")
        device.stop(TLMC_StopMode.TLMC_StopMode_Immediate, DEFAULT_TIMEOUT)

        # --- STATUS ---
        DiagnosticsHelper.console("Fetching status...")
        device.request_status(DEFAULT_TIMEOUT)

        status = device.get_stepper_status(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console_object(status)

        # --- SETTINGS ---
        DiagnosticsHelper.console("Fetching settings JSON...")
        json_settings = device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True)
        print(json_settings)

    except XADeviceException as e:
        print("Error occurred:", e.error_code)

    finally:
        if device:
            DiagnosticsHelper.console("Shutting down device...")
            device.disconnect()
            device.close()

        DiagnosticsHelper.console("Shutting down system...")
        system_manager.shutdown()

        DiagnosticsHelper.console("Completed.")


if __name__ == "__main__":
    main()