# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListPermissionMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.type: Optional[str] = None
        self.fields: Optional[str] = None
        self.perm_type: Optional[str] = None
        self.token: Optional[str] = None

    @staticmethod
    def builder() -> "ListPermissionMemberRequestBuilder":
        return ListPermissionMemberRequestBuilder()


class ListPermissionMemberRequestBuilder(object):

    def __init__(self) -> None:
        list_permission_member_request = ListPermissionMemberRequest()
        list_permission_member_request.http_method = HttpMethod.GET
        list_permission_member_request.uri = "/open-apis/drive/v1/permissions/:token/members"
        list_permission_member_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_permission_member_request: ListPermissionMemberRequest = list_permission_member_request

    def type(self, type: str) -> "ListPermissionMemberRequestBuilder":
        self._list_permission_member_request.type = type
        self._list_permission_member_request.add_query("type", type)
        return self

    def fields(self, fields: str) -> "ListPermissionMemberRequestBuilder":
        self._list_permission_member_request.fields = fields
        self._list_permission_member_request.add_query("fields", fields)
        return self

    def perm_type(self, perm_type: str) -> "ListPermissionMemberRequestBuilder":
        self._list_permission_member_request.perm_type = perm_type
        self._list_permission_member_request.add_query("perm_type", perm_type)
        return self

    def token(self, token: str) -> "ListPermissionMemberRequestBuilder":
        self._list_permission_member_request.token = token
        self._list_permission_member_request.paths["token"] = str(token)
        return self

    def build(self) -> ListPermissionMemberRequest:
        return self._list_permission_member_request
