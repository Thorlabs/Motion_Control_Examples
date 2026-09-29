from typing import Protocol, runtime_checkable

@runtime_checkable
class EncoderCounter(Protocol):

    def get_encoder_counter(self, max_wait_in_milliseconds: int) -> int: ...

    def set_encoder_counter(self, new_encoder_counter: int) -> None: ...