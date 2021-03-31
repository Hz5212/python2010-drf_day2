from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status


def exception_handler(exc, context):
    # 详细的错误信息的定义
    error = "%s %s %s" % (context['view'], context["request"].method, exc)
    print(error)

    # 先让DRF处理异常  根据异常处理的结果判断异常是否已经被处理
    response = drf_exception_handler(exc, context)

    # 如果返回值为None，说明DRF无法处理，自定义处理
    if response is None:
        return Response({"error_message": "程序内部错误，程序猿小哥哥后台处理中~"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 如果response有值，说明异常已经被处理，
    return response
