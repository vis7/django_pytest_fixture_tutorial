from django.test import TestCase
from django.contrib.auth.models import Group, User

# # simple test
def test_foo():
    assert True

# accessing database
def test_should_create_user_with_username(db):
    user = User.objects.create_user("Haki")
    assert user.username == "vis"
