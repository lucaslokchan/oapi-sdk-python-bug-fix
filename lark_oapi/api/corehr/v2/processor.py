# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type

from lark_oapi.event.processor import IEventProcessor
from .model.p2_corehr_employee_domain_event_v2 import P2CorehrEmployeeDomainEventV2
from .model.p2_corehr_job_change_updated_v2 import P2CorehrJobChangeUpdatedV2
from .model.p2_corehr_offboarding_checklist_updated_v2 import P2CorehrOffboardingChecklistUpdatedV2
from .model.p2_corehr_offboarding_status_updated_v2 import P2CorehrOffboardingStatusUpdatedV2
from .model.p2_corehr_offboarding_updated_v2 import P2CorehrOffboardingUpdatedV2
from .model.p2_corehr_probation_updated_v2 import P2CorehrProbationUpdatedV2
from .model.p2_corehr_process_updated_v2 import P2CorehrProcessUpdatedV2
from .model.p2_corehr_process_approver_updated_v2 import P2CorehrProcessApproverUpdatedV2
from .model.p2_corehr_process_cc_updated_v2 import P2CorehrProcessCcUpdatedV2
from .model.p2_corehr_process_node_updated_v2 import P2CorehrProcessNodeUpdatedV2


class P2CorehrEmployeeDomainEventV2Processor(IEventProcessor[P2CorehrEmployeeDomainEventV2]):
    def __init__(self, f: Callable[[P2CorehrEmployeeDomainEventV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrEmployeeDomainEventV2]:
        return P2CorehrEmployeeDomainEventV2

    def do(self, data: P2CorehrEmployeeDomainEventV2) -> None:
        self.f(data)


class P2CorehrJobChangeUpdatedV2Processor(IEventProcessor[P2CorehrJobChangeUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrJobChangeUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrJobChangeUpdatedV2]:
        return P2CorehrJobChangeUpdatedV2

    def do(self, data: P2CorehrJobChangeUpdatedV2) -> None:
        self.f(data)


class P2CorehrOffboardingChecklistUpdatedV2Processor(IEventProcessor[P2CorehrOffboardingChecklistUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrOffboardingChecklistUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrOffboardingChecklistUpdatedV2]:
        return P2CorehrOffboardingChecklistUpdatedV2

    def do(self, data: P2CorehrOffboardingChecklistUpdatedV2) -> None:
        self.f(data)


class P2CorehrOffboardingStatusUpdatedV2Processor(IEventProcessor[P2CorehrOffboardingStatusUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrOffboardingStatusUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrOffboardingStatusUpdatedV2]:
        return P2CorehrOffboardingStatusUpdatedV2

    def do(self, data: P2CorehrOffboardingStatusUpdatedV2) -> None:
        self.f(data)


class P2CorehrOffboardingUpdatedV2Processor(IEventProcessor[P2CorehrOffboardingUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrOffboardingUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrOffboardingUpdatedV2]:
        return P2CorehrOffboardingUpdatedV2

    def do(self, data: P2CorehrOffboardingUpdatedV2) -> None:
        self.f(data)


class P2CorehrProbationUpdatedV2Processor(IEventProcessor[P2CorehrProbationUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrProbationUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrProbationUpdatedV2]:
        return P2CorehrProbationUpdatedV2

    def do(self, data: P2CorehrProbationUpdatedV2) -> None:
        self.f(data)


class P2CorehrProcessUpdatedV2Processor(IEventProcessor[P2CorehrProcessUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrProcessUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrProcessUpdatedV2]:
        return P2CorehrProcessUpdatedV2

    def do(self, data: P2CorehrProcessUpdatedV2) -> None:
        self.f(data)


class P2CorehrProcessApproverUpdatedV2Processor(IEventProcessor[P2CorehrProcessApproverUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrProcessApproverUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrProcessApproverUpdatedV2]:
        return P2CorehrProcessApproverUpdatedV2

    def do(self, data: P2CorehrProcessApproverUpdatedV2) -> None:
        self.f(data)


class P2CorehrProcessCcUpdatedV2Processor(IEventProcessor[P2CorehrProcessCcUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrProcessCcUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrProcessCcUpdatedV2]:
        return P2CorehrProcessCcUpdatedV2

    def do(self, data: P2CorehrProcessCcUpdatedV2) -> None:
        self.f(data)


class P2CorehrProcessNodeUpdatedV2Processor(IEventProcessor[P2CorehrProcessNodeUpdatedV2]):
    def __init__(self, f: Callable[[P2CorehrProcessNodeUpdatedV2], None]):
        self.f = f

    def type(self) -> Type[P2CorehrProcessNodeUpdatedV2]:
        return P2CorehrProcessNodeUpdatedV2

    def do(self, data: P2CorehrProcessNodeUpdatedV2) -> None:
        self.f(data)
