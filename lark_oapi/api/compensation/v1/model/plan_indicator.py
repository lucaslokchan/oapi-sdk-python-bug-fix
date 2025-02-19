# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .adjustment_logic import AdjustmentLogic


class PlanIndicator(object):
    _types = {
        "indicator_id": str,
        "plan_indicator_logic": AdjustmentLogic,
    }

    def __init__(self, d=None):
        self.indicator_id: Optional[str] = None
        self.plan_indicator_logic: Optional[AdjustmentLogic] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PlanIndicatorBuilder":
        return PlanIndicatorBuilder()


class PlanIndicatorBuilder(object):
    def __init__(self) -> None:
        self._plan_indicator = PlanIndicator()

    def indicator_id(self, indicator_id: str) -> "PlanIndicatorBuilder":
        self._plan_indicator.indicator_id = indicator_id
        return self

    def plan_indicator_logic(self, plan_indicator_logic: AdjustmentLogic) -> "PlanIndicatorBuilder":
        self._plan_indicator.plan_indicator_logic = plan_indicator_logic
        return self

    def build(self) -> "PlanIndicator":
        return self._plan_indicator
