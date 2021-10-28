import pytest
from school.models import Student

@pytest.fixture
def student():
    return {
        "vis": Student.objects.get(pk=1),
        "dhruvin": Student.objects.get(pk=2)
    }
