import environ

from django.core.management import BaseCommand
from django.contrib.auth import get_user_model

from apps.utils.user_type import UserType
from apps.utils.utils import generate_authentication_token

UserModel = get_user_model()
env = environ.Env()


class Command(BaseCommand):
    """
    Command for creating a super admin using default admin credentials
    """
    def handle(self, *args, **options):
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
        else:
            print('Default user already exist')
