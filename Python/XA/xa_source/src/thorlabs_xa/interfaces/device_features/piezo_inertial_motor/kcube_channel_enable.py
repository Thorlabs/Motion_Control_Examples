from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_PZIM_KcubeChannelEnableMode

@runtime_checkable
class KcubeChannelEnable(Protocol):

    def get_kcube_channel_enable(self, max_wait_in_milliseconds: int) -> TLMC_PZIM_KcubeChannelEnableMode:...

    def set_kcube_channel_enable(self, channelMode : TLMC_PZIM_KcubeChannelEnableMode) -> None:...