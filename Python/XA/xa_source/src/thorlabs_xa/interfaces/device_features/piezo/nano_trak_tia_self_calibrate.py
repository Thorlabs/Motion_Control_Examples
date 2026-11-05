from typing import Protocol, runtime_checkable

@runtime_checkable
class NanoTrakTiaSelfCalibrate(Protocol):

    def nano_trak_tia_self_calibrate(self) -> None: ...