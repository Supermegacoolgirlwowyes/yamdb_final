from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if username is None:
            username = email.split('@')[0]
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password):
        if not email:
            raise ValueError('Users must have an email address')
        if username is None:
            username = email.split('@')[0]
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_staff = True
        user.role = user.UserRoles.MOD
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError('Users must have an email address')
        if username is None:
            username = email.split('@')[0]
        user = self.create_user(
            email,
            username,
            password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.role = user.UserRoles.ADM
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    class UserRoles(models.TextChoices):
        USR = 'user', ('User')
        MOD = 'moderator', ('Moderator')
        ADM = 'admin', ('Admin')

    username = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Псевдоним'
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        verbose_name='E-mail'
    )
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    bio = models.TextField(max_length=1000, verbose_name='О себе')
    role = models.CharField(
        max_length=50,
        choices=UserRoles.choices,
        default=UserRoles.USR,
        verbose_name='Уровень доступа'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    @property
    def is_moderator(self):
        return self.role == self.UserRoles.MOD

    @property
    def is_admin(self):
        return self.role == self.UserRoles.ADM

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    class Meta:
        ordering = ['username']
