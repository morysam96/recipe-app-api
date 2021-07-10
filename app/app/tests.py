from django.test import TestCase
from .calc import add,subtract

class CalcTest(TestCase):
    # first word function should was "test"
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11)

    #write test before you write the code(unit test with TDD)
    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5,11),6)




#terminal:docker-compose run app sh -c "python manage.py test && flake8"