"""Test cases for account models."""

from django.test import TestCase

from accounts.models import User


class UserTestCase(TestCase):
    """Test cases related to the User model."""

    def test_display_name(self):
        """Test that User.display_name uses first_name or username."""
        bob = User(username='bob')
        self.assertEqual('bob', bob.display_name)

        bob.first_name = 'Robert'
        self.assertEqual('Robert', bob.display_name)
