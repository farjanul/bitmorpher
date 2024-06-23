from rest_framework.permissions import BasePermission
from apps.utils.user_type import UserType


class IsManager(BasePermission):
    """
    Custom permission to only allow access to manager-type users.
    """

    def has_permission(self, request, view):
        """
        Check if the user is authenticated and is of type 'manager'.

        Returns:
            bool: True if the user is authenticated and is a manager, False otherwise.
        """
        return request.user.is_authenticated and request.user.user_type == UserType.MANAGER.value


class IsCustomer(BasePermission):
    """
    Custom permission to only allow access to customer-type users.
    """

    def has_permission(self, request, view):
        """
        Check if the user is authenticated and is of type 'customer'.

        Returns:
            bool: True if the user is authenticated and is a customer, False otherwise.
        """
        return request.user.is_authenticated and request.user.user_type == UserType.CUSTOMER.value
