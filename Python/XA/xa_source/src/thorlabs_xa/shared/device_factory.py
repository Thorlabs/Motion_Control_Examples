from thorlabs_xa.implementations.device_feature_groups.bbd30x_feature_group import Bbd30xFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bbd30x_logical_channel_feature_group import Bbd30xLogicalChannelFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bpc30x_feature_group import Bpc30xFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bpc30x_logical_channel_feature_group import Bpc30xLogicalChannelFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bpc301_feature_group import Bpc301FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bsc201_feature_group import Bsc201FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bsc201v4_feature_group import Bsc201v4FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bsc20x_feature_group import Bsc20xFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bsc20x_logical_channel_feature_group import Bsc20xLogicalChannelFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.bsc20xv4_logical_channel_feature_group import Bsc20xv4LogicalChannelFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.kbd101_feature_group import Kbd101FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.kdc101_feature_group import Kdc101FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.kim001_feature_group import Kim001FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.kpc101_feature_group import Kpc101FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.kst101_feature_group import Kst101FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.kst201_feature_group import Kst201FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.linear_translation_stage_feature_group import LinearTranslationStageFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.pdxc2_feature_group import Pdxc2FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.pdxc3_feature_group import Pdxc3FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.tbd001_feature_group import Tbd001FeatureGroup
from thorlabs_xa.implementations.device_feature_groups.umcx_feature_group import UmcxFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.umcx_brushless_logical_channel_feature_group import UmcxBrushlessLogicalChannelFeatureGroup
from thorlabs_xa.implementations.device_feature_groups.umcx_stepper_logical_channel_feature_group import UmcxStepperLogicalChannelFeatureGroup

from thorlabs_xa.products.bbd30x import Bbd30x
from thorlabs_xa.products.bbd30x_logical_channel import Bbd30xLogicalChannel
from thorlabs_xa.products.bpc301 import Bpc301
from thorlabs_xa.products.bpc30x import Bpc30x
from thorlabs_xa.products.bpc30x_logical_channel import Bpc30xLogicalChannel
from thorlabs_xa.products.bsc201 import Bsc201
from thorlabs_xa.products.bsc201v4 import Bsc201v4
from thorlabs_xa.products.bsc20x import Bsc20x
from thorlabs_xa.products.bsc20x_logical_channel import Bsc20xLogicalChannel
from thorlabs_xa.products.bsc20xv4_logical_channel import Bsc20xv4LogicalChannel
from thorlabs_xa.products.kbd101 import Kbd101
from thorlabs_xa.products.kdc101 import Kdc101
from thorlabs_xa.products.kim001 import Kim001
from thorlabs_xa.products.kpc101 import Kpc101
from thorlabs_xa.products.kst101 import Kst101
from thorlabs_xa.products.kst201 import Kst201
from thorlabs_xa.products.linear_translation_stage import LinearTranslationStage
from thorlabs_xa.products.pdxc2 import Pdxc2
from thorlabs_xa.products.pdxc3 import Pdxc3
from thorlabs_xa.products.tbd001 import Tbd001
from thorlabs_xa.products.umcx import Umcx
from thorlabs_xa.products.umcx_brushless_logical_channel import UmcxBrushlessLogicalChannel
from thorlabs_xa.products.umcx_stepper_logical_channel import UmcxStepperLogicalChannel

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
            case TLMC_DeviceType.TLMC_DeviceType_Bbd30xBaseUnit:
                feature_group = Bbd30xFeatureGroup(device_handle, self.native_functions)
                return Bbd30x(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bbd30xLogicalChannel:
                feature_group = Bbd30xLogicalChannelFeatureGroup(device_handle, self.native_functions)
                return Bbd30xLogicalChannel(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bpc301:
                feature_group = Bpc301FeatureGroup(device_handle, self.native_functions)
                return Bpc301(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bpc30xBaseUnit:
                feature_group = Bpc30xFeatureGroup(device_handle, self.native_functions)
                return Bpc30x(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bpc30xLogicalChannel:
                feature_group = Bpc30xLogicalChannelFeatureGroup(device_handle, self.native_functions)
                return Bpc30xLogicalChannel(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bsc20xBaseUnit:
                feature_group = Bsc20xFeatureGroup(device_handle, self.native_functions)
                return Bsc20x(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bsc20xLogicalChannel:
                feature_group = Bsc20xLogicalChannelFeatureGroup(device_handle, self.native_functions)
                return Bsc20xLogicalChannel(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bsc201:
                feature_group = Bsc201FeatureGroup(device_handle, self.native_functions)
                return Bsc201(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bsc201v4:
                feature_group = Bsc201v4FeatureGroup(device_handle, self.native_functions)
                return Bsc201v4(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Bsc20xv4LogicalChannel:
                feature_group = Bsc20xv4LogicalChannelFeatureGroup(device_handle, self.native_functions)
                return Bsc20xv4LogicalChannel(device_handle, device_info, feature_group, self.native_functions)            
            case TLMC_DeviceType.TLMC_DeviceType_Kbd101:
                feature_group = Kbd101FeatureGroup(device_handle, self.native_functions)
                return Kbd101(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Kdc101:
                feature_group = Kdc101FeatureGroup(device_handle, self.native_functions)
                return Kdc101(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Kpc101:
                feature_group = Kpc101FeatureGroup(device_handle, self.native_functions)
                return Kpc101(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Kim001:
                feature_group = Kim001FeatureGroup(device_handle, self.native_functions)
                return Kim001(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Kst101:
                feature_group = Kst101FeatureGroup(device_handle, self.native_functions)
                return Kst101(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Kst201:
                feature_group = Kst201FeatureGroup(device_handle, self.native_functions)
                return Kst201(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Lts:
                feature_group = LinearTranslationStageFeatureGroup(device_handle, self.native_functions)
                return LinearTranslationStage(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Pdxc2:
                feature_group = Pdxc2FeatureGroup(device_handle, self.native_functions)
                return Pdxc2(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Pdxc3:
                feature_group = Pdxc3FeatureGroup(device_handle, self.native_functions)
                return Pdxc3(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_Tbd001:
                feature_group = Tbd001FeatureGroup(device_handle, self.native_functions)
                return Tbd001(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_UmcxBaseUnit:
                feature_group = UmcxFeatureGroup(device_handle, self.native_functions)
                return Umcx(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_UmcxBrushlessLogicalChannel:
                feature_group = UmcxBrushlessLogicalChannelFeatureGroup(device_handle, self.native_functions)
                return UmcxBrushlessLogicalChannel(device_handle, device_info, feature_group, self.native_functions)
            case TLMC_DeviceType.TLMC_DeviceType_UmcxStepperLogicalChannel:
                feature_group = UmcxStepperLogicalChannelFeatureGroup(device_handle, self.native_functions)
                return UmcxStepperLogicalChannel(device_handle, device_info, feature_group, self.native_functions)
                
        raise ValueError("Device type not currently supported")