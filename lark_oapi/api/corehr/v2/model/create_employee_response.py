# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_employee_response_body import CreateEmployeeResponseBody


class CreateEmployeeResponse(BaseResponse):
    _types = {
        "data": CreateEmployeeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateEmployeeResponseBody] = None
        init(self, d, self._types)
