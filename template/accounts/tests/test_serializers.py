"""Test cases for account serializers."""

from accounts.models import User
from project.decorators import serialize


def test_serialize_user():
    """Test serialization for a User object."""
    bob = User(username='bob', first_name='Bob', last_name='Marley')
    assert serialize(bob) == {
        'name': 'Bob'
    }
