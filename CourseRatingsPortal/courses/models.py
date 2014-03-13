from django.db import models
from datetime import datetime

# Create your models here.
class Dates(models.Model):
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)

class University(models.Model):
    university_name = models.CharField(max_length = 150)

    dates = models.ForeignKey(Dates)

    class Meta:
        ordering=['university_name']

class Department(models.Model):
    dep_name = models.CharField(max_length=150)

    dates = models.ForeignKey(Dates)

    class Meta:
        ordering=['dep_name']


class Course(models.Model):
    course_id = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    registration_code = models.PositiveIntegerField()

    course_name = models.CharField(max_length=100)
    university = models.ForeignKey(University)
    department = models.ForeignKey(Department)

    dates = models.ForeignKey(Dates)

    class Meta:
        ordering=['course_name']

class Professor(models.Model):
    first_name = models.CharField(max_length = 20)
    middle_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)

    university = models.ForeignKey(University)
    rating_value = models.FloatField(default=0)
    easiness_value = models.FloatField(default=0)
    department = models.ManyToManyField(Department)

    dates = models.ForeignKey(Dates)

    class Meta:
        ordering=['last_name','first_name','middle_name']

class User(models.Model):
    name = models.CharField(max_length = 40)
    university = models.ForeignKey(University)

    dates = models.ForeignKey(Dates)

    class Meta:
        ordering=['name','university']

class Rating(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True)
    professor = models.ForeignKey(Professor, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    rating_text = models.CharField(max_length = 1000)
    rating_quality = models.FloatField(default=0)
    rating_easiness = models.FloatField(default=0)

    dates = models.ForeignKey(Dates)
