from thorlabs_xa.products.lnnx import Lnnx
from thorlabs_xa.shared.enums import TLMC_OperatingMode
from thorlabs_xa.shared.system_manager import SystemManager
from thorlabs_xa.shared.xa_error_factory import XADeviceException

MB_SERIAL = "123000001"
CH1_SERIAL = "124000001"
CH2_SERIAL = "124000002"
CH3_SERIAL = "124000003"

DEFAULT_TRANSPORT = ""

system_manager = SystemManager.instance()

device: Lnnx | None = None

try:
    system_manager.startup()

    device = system_manager.open_device_as(MB_SERIAL, DEFAULT_TRANSPORT, TLMC_OperatingMode.TLMC_OperatingMode_Default, Lnnx)

except XADeviceException as e:
    print("Encountered error, code: ", e.error_code)

finally:

    if device is not None:
        try:
            device.close()
        except Exception:
            pass

    system_manager.shutdown()