from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_id = models.CharField(max_length=20, default = 'DEFAULT VALUE')
    peer_leader = models.CharField(max_length=20)

