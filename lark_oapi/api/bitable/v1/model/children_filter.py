# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .condition import Condition


class ChildrenFilter(object):
    _types = {
        "conjunction": str,
        "conditions": List[Condition],
    }

    def __init__(self, d=None):
        self.conjunction: Optional[str] = None
        self.conditions: Optional[List[Condition]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChildrenFilterBuilder":
        return ChildrenFilterBuilder()


class ChildrenFilterBuilder(object):
    def __init__(self) -> None:
        self._children_filter = ChildrenFilter()

    def conjunction(self, conjunction: str) -> "ChildrenFilterBuilder":
        self._children_filter.conjunction = conjunction
        return self

    def conditions(self, conditions: List[Condition]) -> "ChildrenFilterBuilder":
        self._children_filter.conditions = conditions
        return self

    def build(self) -> "ChildrenFilter":
        return self._children_filter
