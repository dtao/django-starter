"""Serializers for account-related models."""

from accounts.models import User
from project.decorators import serializes


@serializes(User)
def serialize_user(user):
    """Serialize a User object."""
    return {
        'name': user.display_name
    }
