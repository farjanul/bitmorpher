from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import CustomUserModel


class CustomAuthMiddleware(BaseAuthentication):
    """
    Custom authentication middleware for token-based authentication.
    """

    def authenticate(self, request):
        """
        Authenticate the user based on the 'Authorization' header.
        """
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            try:
                user = CustomUserModel.objects.get(authentication_token=token)
                return (user, None)
            except CustomUserModel.DoesNotExist:
                raise AuthenticationFailed({'error': 'Invalid authentication token'})
        else:
            raise AuthenticationFailed({'error': 'Authentication token required'})
