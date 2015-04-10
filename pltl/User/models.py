from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from User.userManager import CustUserManager

class User(AbstractBaseUser,PermissionsMixin):
    fname = models.CharField(max_length=20, blank = False)
    lname = models.CharField(max_length=20, blank = False)
    email = models.EmailField(max_length=50, db_index = True, blank = False,primary_key=True)
    course_id = models.CharField(max_length=20, default='DEFAULT VALUE')
    
    USERNAME_FIELD = 'email'
    objects = CustUserManager()
    
    #Attributes for admin
    is_admin = models.BooleanField(default = False, null = False)
    is_active = models.BooleanField(default = True, null = False)
    is_staff = models.BooleanField(default=False, null = False)

    def save(self, *args, **kwargs):
    	error = False
    	try:
    		User.clean_fields(self)
    	except ValidationError as e:
    		#print 'ValidationError: %s' %(e)
    		error = True
    	if error == False:
    		super(User,self).save(*args, **kwargs)

    def get_short_name():
        return self.fname


# Create your models here.
