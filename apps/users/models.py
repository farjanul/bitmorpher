from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.utils.user_type import UserType
from apps.utils.utils import generate_authentication_token


class CustomUserModel(AbstractUser):
    """
    Custom user model that extends the default AbstractUser model.
    """

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices(),
        default=UserType.CUSTOMER.value
    )

    authentication_token = models.CharField(
        max_length=16,
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to generate an authentication token if it is not provided.
        """
        if not self.authentication_token:
            self.authentication_token = generate_authentication_token()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the string representation of the user.
        """
        return self.username
