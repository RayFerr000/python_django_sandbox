from django.db import models
from Course.models import Course

# Create your models here.
class Assignment(models.Model):
    assignment_id = models.IntegerField(default=0)
    course_id = models.ForeignKey(Course)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateTimeField('Due Date')
    total_grade = models.IntegerField(default=0)

   
    
