from django.utils.timezone import now
from apps.utils.models import RequestLogModel


class RequestLogMiddleware:
    """
    Middleware to log details of HTTP requests into the RequestLogModel.
    Logs requests only if the user is authenticated and the path starts with '/API/'.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Process the incoming request and log its details.
        """
        response = self.get_response(request)

        if request.user.is_authenticated and request.path.startswith('/API/'):
            RequestLogModel.objects.create(
                username=request.user.username,
                date_time=now(),
                path=request.path,
                method=request.method
            )
        return response
