from django.test import TestCase
from app import models

# Create your tests here.
class TestStudent(TestCase):
    def test_create_student(self):
        joe = models.create_student("Joe Trott", "")
