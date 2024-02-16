from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)




class UsersManager(BaseUserManager):

    def create_user(self, username,email, password=None, **kwargs):
        if not password:
            raise ValueError('Superusers must have password.')
        
        if not username :
            raise ValueError('Members must have an username.')
        
        if not email :
            raise ValueError('Members must have an email_id.')
        
        user_obj = self.model(username=username,email=self.normalize_email(email),**kwargs)
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self,username, email, password=None, **kwargs):
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superadmin', True)
        return self.create_user(username, email, password=password, **kwargs)



# Create your models here.
class memberdetails(AbstractBaseUser):
    username=models.CharField(max_length=5,null=True,blank=True,unique=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='image/',null=True,blank=True)
    status=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at=models.DateTimeField(auto_now=True,db_index=True)
   
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    objects = UsersManager() 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, prem, obj=None):
        return self.is_superadmin
    
    def has_module_perms(self, app_lable):
        return self.is_superadmin
    
