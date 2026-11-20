import platform

from thorlabs_xa.products.bbd30x import Bbd30x
from thorlabs_xa.shared.diagnostics_helper import DiagnosticsHelper
from thorlabs_xa.shared.enums import (
    TLMC_AuxIoPortMode,
    TLMC_AuxIoPortNumber,
    TLMC_DigitalOutput,
    TLMC_OperatingMode,
    TLMC_RackBayNumber,
    TLMC_SettingStringFormat,
)
from thorlabs_xa.shared.params import TLMC_DeviceInfo
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException

BBD30X_PART_NUMBER = "BBD303"
DEFAULT_TIMEOUT = 5000

SIMULATION_CONFIG_STRING = {
    "PartNumber": BBD30X_PART_NUMBER,
    "SerialNumber": "103003334",
    "Channels": [
        {"BayNumber": 1, "SerialNumber": "104003335", "ActuatorType": "DDS220"},
        {"BayNumber": 2, "SerialNumber": "104003336", "ActuatorType": "DDS300"},
        {"BayNumber": 3, "SerialNumber": "104003337", "ActuatorType": "DDS600"},
    ],
}


def create_simulation(system_manager: SystemManager) -> TLMC_DeviceInfo | None:
    try:
        system_manager.create_simulation(SIMULATION_CONFIG_STRING)
    except XADeviceException as e:
        print(f"Unable to create simulation for {BBD30X_PART_NUMBER}: {e.error_code}")
        return None

    device_info = TLMC_DeviceInfo()
    device_info.device_type_description = BBD30X_PART_NUMBER
    device_info.device = SIMULATION_CONFIG_STRING["SerialNumber"]
    device_info.transport = ""
    return device_info


def main() -> None:
    device: Bbd30x | None = None
    system_manager = SystemManager.instance()

    if platform.system() == "Linux":
        system_manager.startup("deviceDiscovery.connections=/dev/ttyUSB0")
    else:
        system_manager.startup()

    devices = system_manager.get_device_list()
    device_info: TLMC_DeviceInfo | None = None

    for listed_device_info in devices:
        if listed_device_info.part_number == BBD30X_PART_NUMBER:
            device_info = listed_device_info

    if not device_info:
        device_info = create_simulation(system_manager)

    if not device_info:
        print("No compatible BBD30X device available.")
        system_manager.shutdown()
        return

    try:
        device = system_manager.open_device_as(device_info.device, device_info.transport, TLMC_OperatingMode.TLMC_OperatingMode_Default, Bbd30x)

        DiagnosticsHelper.console(device.get_hardware_info(DEFAULT_TIMEOUT))

        application_firmware, device_firmware = device.get_firmware_version_info(DEFAULT_TIMEOUT)
        DiagnosticsHelper.console(f"Application firmware: {application_firmware}")
        DiagnosticsHelper.console(f"Device firmware: {device_firmware}")

        device.set_digital_output_states(TLMC_DigitalOutput.TLMC_DigitalOutput_1)
        DiagnosticsHelper.console(f"Digital outputs: {device.get_digital_output_states(DEFAULT_TIMEOUT).name}")

        device.set_aux_io_port_mode(
            TLMC_AuxIoPortNumber.TLMC_AuxIoPortNumber_Port1,
            TLMC_AuxIoPortMode.TLMC_AuxIoPortMode_SoftwareControlled,
        )
        DiagnosticsHelper.console(
            f"Aux mode: {device.get_aux_io_port_mode(TLMC_AuxIoPortNumber.TLMC_AuxIoPortNumber_Port1, DEFAULT_TIMEOUT).name}"
        )

        DiagnosticsHelper.console(
            f"Rack bay 1 state: {device.get_rack_bay_occupied_state(TLMC_RackBayNumber.TLMC_RackBayNumber_1, DEFAULT_TIMEOUT).name}"
        )

        DiagnosticsHelper.console(device.get_settings(TLMC_SettingStringFormat.TLMC_SettingStringFormat_Json, True))

    except XADeviceException as e:
        print("Encountered error, code:", e.error_code)
    finally:
        if device:
            device.disconnect()
            device.close()
        system_manager.shutdown()


if __name__ == "__main__":
    main()
