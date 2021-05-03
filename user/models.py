from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils.translation import ugettext_lazy as _


class UserAccountManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        print(is_staff, is_superuser)
        return self._create_user(email, password, **extra_fields)


    # def create_user(self, email, handle, password, **extra_fields):
    #     if not email:
    #         raise ValueError("Email is compulsory")

    #     email = self.normalize_email(email)
    #     user = self.model(email=email, handle=handle)

    #     user.set_password(password)
    #     user.save()
    #     return user

    # def create_superuser(self, email, handle, password, **extra_fields):
    #     extra_fields.setdefault("is_superuser", True)
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_active", True)
    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError(_("Superuser must have is_staff=True."))
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError(_("Superuser must have is_superuser=True."))

    #     email = self.normalize_email(email)
    #     user = self.model(email=email, handle=handle)

    #     user.set_password(password)
    #     user.save()
        # return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    name = models.CharField(
        max_length=255,
    )
    handle = models.CharField(
        max_length=255,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "handle",
    ]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
