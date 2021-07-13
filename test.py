from django.test import TestCase
from django.contrib.auth.models import Group, User


# class MyTest(TestCase):
#     fixtures = ['group.json']

#     def test_should_create_group(self):
#         group = Group.objects.get(pk=1)
#         self.assertEqual(group.name, "appusers")

# simple test
def test_foo():
    assert True

# accessing database


def test_should_create_user_with_username(db) -> None:
    user = User.objects.create_user("Haki")
    assert user.username == "Haki"
