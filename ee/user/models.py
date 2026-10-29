from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, user_type, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        return self.create_user(email, 'a', password, **extra_fields)

class User(AbstractBaseUser): 
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=1, choices=(('s', 'Student'), ('t', 'Teacher'), ('a', 'Admin')), default='s')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.email