from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class University(models.Model):
    university_name = models.CharField(max_length = 150)

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering=['university_name']
        verbose_name_plural = "Universities"

class Department(models.Model):
    dep_name = models.CharField(max_length=150)

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering=['dep_name']

class Professor(models.Model):
    name = models.CharField(max_length = 50)

    university = models.ForeignKey(University)
    rating_value = models.FloatField(default=0)
    easiness_value = models.FloatField(default=0)
    department = models.ManyToManyField(Department)

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering=['name']

class Course(models.Model):
    course_id = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    registration_code = models.PositiveIntegerField()

    course_name = models.CharField(max_length=100)
    university = models.ForeignKey(University)
    department = models.ForeignKey(Department,null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering=['course_name']

class Section(models.Model):
    course = models.ForeignKey(Course)
    section_id = models.IntField(default=0, unique=True)
    professor = models.ForeignKey(Professor)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default = timezone.now, blank=True)

    class Meta:
        ordering=['section_id']

class Rating(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True)
    professor = models.ForeignKey(Professor, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    rating_text = models.CharField(max_length = 500)
    rating_quality = models.FloatField(default=0)
    rating_easiness = models.FloatField(default=0)
    counted = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering=['date_modified']

