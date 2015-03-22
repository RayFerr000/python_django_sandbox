from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    fname = models.CharField(max_length=20, blank = False)
    lname = models.CharField(max_length=20, blank = False)
    email = models.EmailField(max_length=50, unique = True, db_index = True, blank = False)
    course_id = models.CharField(max_length=20, default='DEFAULT VALUE')
    role = {}
    USERNAME_FIELD = 'email'

# Create your models here.
