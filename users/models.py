from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


class Manager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('email is required')
        user = self.model(
            email=self.normalize_email(email=email),
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        user = self.create_user(
            email=email,
            password=password,
            date_of_birth=date_of_birth)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(
        verbose_name='Email address',
        max_length=200,
        unique=True)
    password = models.CharField(max_length=200)
    username = None
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm: str, obj: None) -> bool:
        return self.is_admin

    def has_module_perms(self, app_label: str) -> bool:
        return True

    @property
    def is_staff(self):
        return self.is_admin
