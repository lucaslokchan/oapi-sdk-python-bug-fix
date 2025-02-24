# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SkillInstance(object):
    _types = {
        "skill_instance_id": str,
        "status": str,
        "input": str,
        "output": str,
    }

    def __init__(self, d=None):
        self.skill_instance_id: Optional[str] = None
        self.status: Optional[str] = None
        self.input: Optional[str] = None
        self.output: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SkillInstanceBuilder":
        return SkillInstanceBuilder()


class SkillInstanceBuilder(object):
    def __init__(self) -> None:
        self._skill_instance = SkillInstance()

    def skill_instance_id(self, skill_instance_id: str) -> "SkillInstanceBuilder":
        self._skill_instance.skill_instance_id = skill_instance_id
        return self

    def status(self, status: str) -> "SkillInstanceBuilder":
        self._skill_instance.status = status
        return self

    def input(self, input: str) -> "SkillInstanceBuilder":
        self._skill_instance.input = input
        return self

    def output(self, output: str) -> "SkillInstanceBuilder":
        self._skill_instance.output = output
        return self

    def build(self) -> "SkillInstance":
        return self._skill_instance
