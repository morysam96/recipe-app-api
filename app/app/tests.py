from django.test import TestCase
from .calc import add

class CalcTest(TestCase):
    # first word function should was "test"
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11)


#terminal:docker-compose run app sh -c "python manage.py test"