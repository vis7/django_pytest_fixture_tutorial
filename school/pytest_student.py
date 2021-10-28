# from rest_framework import status
import pytest

from rest_framework.test import APIClient

factory = APIClient()

pytestmark = pytest.mark.django_db

# checking that existing data is good
def test_check_existing_data_intact(student):
    vis = student.get('vis')
    assert vis.first_name == 'anything'
    assert vis.last_name == 'cilans'
    assert vis.age == 20

# creating student
def test_create_student():
    payload = {
        "first_name": "dhruvin",
        "last_name": "prajapati",
        "age": 20
    }
    response = factory.post('student/', payload)
    assert response.status_code == 200

def test_foo():
    assert True
