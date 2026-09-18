from typing import Protocol, runtime_checkable

from thorlabs_xa.shared.enums import TLMC_ParameterGroupId

@runtime_checkable
class PersistParams(Protocol):

    def persist_params(self, parameter_group_id: TLMC_ParameterGroupId): ...