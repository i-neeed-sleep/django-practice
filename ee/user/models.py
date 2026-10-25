from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser): 
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=1, choices=(('s', 'Student'), ('t', 'Teacher')), default='s')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'user_type']

    objects = UserManager()

    def __str__(self):
        return self.email