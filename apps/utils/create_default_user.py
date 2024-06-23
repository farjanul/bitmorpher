from django.contrib.auth import get_user_model

from apps.utils.user_type import UserType
from apps.utils.utils import generate_authentication_token
from conf import settings

env = settings.env

UserModel = get_user_model()


def create_default_user():
    """
    Create a default superuser if one does not already exist.

    This function checks if a superuser with the specified username exists.
    If not, it creates a new superuser with details provided via environment variables.
    """
    is_exist = UserModel.objects.filter(
        username=env.str('DEFAULT_ADMIN_USERNAME')
    ).first()

    if not is_exist:
        user = UserModel.objects.create_superuser(
            username=env.str('DEFAULT_ADMIN_USERNAME'),
            first_name=env.str('DEFAULT_ADMIN_FIRST_NAME'),
            last_name=env.str('DEFAULT_ADMIN_LAST_NAME'),
            email=env.str('DEFAULT_ADMIN_EMAIL'),
            password=env.str('DEFAULT_ADMIN_PASSWORD'),
            user_type=UserType.MANAGER.value,
            authentication_token=generate_authentication_token()
        )
        print('Default user created successfully')
        print('Authentication token: ', user.authentication_token)
