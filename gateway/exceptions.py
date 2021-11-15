from rest_framework.views import exception_handler
from rest_framework.response import Response


def customExceptionHandler(exc,context):

    response = exception_handler(exc,context)

    if response is not None:
        return response
    
    exc_List = str(exc).split('DETAIL:')

    return Response({
        'message':exc_List[-1]
    },
    status='403')