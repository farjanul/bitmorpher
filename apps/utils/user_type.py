from enum import Enum


class UserType(Enum):
    """
    Enumeration for user types.
    """
    MANAGER = 'manager'
    CUSTOMER = 'customer'

    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]
