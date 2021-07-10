from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

"""custom user model"""
"""helper function for creating user or super user"""


class UserManager(BaseUserManager):
    """handler email address instead of the username"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        """can't set password because has be encrypted"""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        """supporting multiple databases"""
        user.save(using=self._db)

        return user


"""create user model new"""


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
