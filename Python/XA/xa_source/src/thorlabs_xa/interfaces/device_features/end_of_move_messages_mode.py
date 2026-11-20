from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_EndOfMoveMessagesMode

@runtime_checkable
class EndOfMoveMessagesMode(Protocol):

    def set_end_of_move_messages_mode(self, messages_mode: TLMC_EndOfMoveMessagesMode) -> None: ...