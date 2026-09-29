from typing import List, Protocol

from thorlabs_xa.shared.subchannel import Subchannel

class GetSubchannel(Protocol):
    
    def get_all_subchannels(self) -> List[Subchannel]: ...
    
    def get_subchannel(self, subchannel_number: int) -> Subchannel: ...