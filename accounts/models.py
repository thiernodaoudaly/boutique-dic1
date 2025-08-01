from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Model for superuser

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None, birthday=None):
        if not email:
            raise ValueError('User must have an email addresse')
        
        if not username:
            raise ValueError('User must have an username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            birthday = birthday
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password, birthday):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            birthday=birthday
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique =True)
    email = models.EmailField(max_length=100, unique=True)
    #phone_number = models.CharField(max_length=50, default= "77 ...")
    #profile_pic = models.ImageField(blank=True)
    birthday = models.DateField(default = date(2000,1,1))
    #Required field

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name'] #'username',
     
    objects =  MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm, obj= None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    

