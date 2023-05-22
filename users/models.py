from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


# Create your models here.

class APPUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None,):
        """
        Creates and saves a User with the given email,
        first_name, last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name):
        """
        Creates and saves a superuser with the given email, password,
        first_name and last_name.
        """
        user = self.create_user(email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user


class APPUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(default='', blank=True, null=True, max_length=100)
    last_name = models.CharField(default='', blank=True, null=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    signup_date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(default='', blank=True, null=True, max_length=20 )
    country = models.CharField(default='', blank=False, null=False, max_length=25 )
    city = models.CharField(default='', blank=True, null=True, max_length=25)
    profile_pic= models.CharField(default='', blank=False, null=False, max_length=25 )
    bio= models.CharField(default='', max_length=200, blank=False, null=False)
    username= models.CharField(default='', max_length=30, blank=False, null=False)

  
    objects = APPUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return '''{} {}'''.format(self.first_name, self.last_name)

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-signup_date', '-id')
        verbose_name = ('user')
        verbose_name_plural = ('users')

