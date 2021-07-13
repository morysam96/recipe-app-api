from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

"""
client will allow us to make test requests
to our application in our unit tests
reverse will allow us to generate URLs
"""


class AdminSiteTests(TestCase):
    """
    run before every test that we run
    so we can do this using a setup function
    """

    def setUp(self):
        """
        client helper function that allows you
        to log a user in with the django authentication
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='pass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='pass123',
            name='Test user full name'
        )

    # test that the users are listed in our django admin.
    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        # /admin/core/user/id
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

# terminal:docker-compose run app sh -c "python manage.py test && flake8"
