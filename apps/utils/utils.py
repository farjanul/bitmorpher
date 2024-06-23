import string
import random


def generate_authentication_token():
    """
    Generate a random 16-character authentication token.

    Returns:
        str: A random string consisting of letters (both uppercase and lowercase) and digits.
    """
    characters = string.ascii_letters + string.digits
    token = ''.join(random.choices(characters, k=16))
    return token
