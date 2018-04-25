from django.urls import reverse
from django.db import models
from django.contrib.auth.models import (
     BaseUserManager, AbstractBaseUser
)
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
 

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
 
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    cover_photo     = models.ImageField(upload_to = 'static/media')
    profile_picture =  models.ImageField(upload_to = 'static/media')
    last_name       =  models.CharField(max_length=100)
    first_name      =  models.CharField(max_length=100)
    middle_name              =   models.CharField(max_length=200)

    sex             =   models.CharField(max_length=6, choices=GENDER, blank=True, default=True)
    date_of_birth   =   models.DateField()
    age             =   models.CharField(max_length=20)

    objects         = MyUserManager()
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.last_name,self.first_name)

    def get_absolute_url(self):
        return u'/some_url/%d' % self.id 
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
