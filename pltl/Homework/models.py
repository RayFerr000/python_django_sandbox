from django.db import models
from Assignment.models import Assignment

class Homework(models.Model):
	homework_id = models.CharField(max_length=20, db_index=True, unique=True, blank=False)
	assignment_id = models.ForeignKey(Assignment)
	homework_soln = models.CharField(max_length=200, blank = False)
	submitted_by = models.EmailField(max_length=20, blank = False)
	submitted_timestamp = models.DateTimeField('date submitted')
	grader_grade = {}
	feedback = {}
