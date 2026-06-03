from thorlabs_xa.implementations.device_feature_groups.kdc101_feature_group import Kdc101FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.kpc101_feature_group import Kpc101FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.kst201_feature_group import Kst201FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.lnnx_feature_group import LnnxFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.linear_translation_stage_feature_group import LinearTranslationStageFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.lnnx_logical_channel_feature_group import LnnxLogicalChannelFeatureGroup

from thorlabs_xa.products.kdc101 import Kdc101
from thorlabs_xa.products.kpc101 import Kpc101
from thorlabs_xa.products.kst201 import Kst201
from thorlabs_xa.products.lnnx import Lnnx
from thorlabs_xa.products.linear_translation_stage import LinearTranslationStage
from thorlabs_xa.products.lnnx_logical_channel import LnnxLogicalChannel

from thorlabs_xa.native_sdks.native_functions import NativeFunctions

from thorlabs_xa.shared.device import Device
from thorlabs_xa.shared.enums import TLMC_DeviceType
from thorlabs_xa.shared.params import TLMC_DeviceInfo

class DeviceFactory:

    def __init__(self, native_functions: NativeFunctions):

        self.native_functions = native_functions

    def create(self, device_handle: int, device_info: TLMC_DeviceInfo) -> Device:

        # Note: It is expected that this will produce a pylance error until all device types are implemented
        match device_info.device_type:
            case TLMC_DeviceType.TLMC_DeviceType_LnnxBaseUnit:
                feature_group = LnnxFeatureGroup(device_handle, self.native_functions)
                return Lnnx(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_LnnxLogicalChannel:
                feature_group = LnnxLogicalChannelFeatureGroup(device_handle, self.native_functions)
                return LnnxLogicalChannel(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Kdc101:
                feature_group = Kdc101FeatureGroup(device_handle, self.native_functions)
                return Kdc101(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Kpc101:
                feature_group = Kpc101FeatureGroup(device_handle, self.native_functions)
                return Kpc101(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Kst201:
                feature_group = Kst201FeatureGroup(device_handle, self.native_functions)
                return Kst201(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_LinearTranslationStage:
                feature_group = LinearTranslationStageFeatureGroup(device_handle, self.native_functions)
                return LinearTranslationStage(device_handle, device_info, feature_group, self.native_functions)
        raise ValueError("Device type not currently supported")