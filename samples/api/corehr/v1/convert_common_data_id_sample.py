# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ConvertCommonDataIdRequest = ConvertCommonDataIdRequest.builder() \
        .id_transform_type(1) \
        .id_type("employment_id") \
        .feishu_user_id_type("open_id") \
        .feishu_department_id_type("open_department_id") \
        .request_body(ConvertCommonDataIdRequestBody.builder()
                      .ids([])
                      .build()) \
        .build()

    # 发起请求
    response: ConvertCommonDataIdResponse = client.corehr.v1.common_data_id.convert(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.common_data_id.convert failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ConvertCommonDataIdRequest = ConvertCommonDataIdRequest.builder() \
        .id_transform_type(1) \
        .id_type("employment_id") \
        .feishu_user_id_type("open_id") \
        .feishu_department_id_type("open_department_id") \
        .request_body(ConvertCommonDataIdRequestBody.builder()
                      .ids([])
                      .build()) \
        .build()

    # 发起请求
    response: ConvertCommonDataIdResponse = await client.corehr.v1.common_data_id.aconvert(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.common_data_id.aconvert failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
