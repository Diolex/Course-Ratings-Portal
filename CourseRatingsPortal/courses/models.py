from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class University(models.Model):
    university_name = models.CharField(max_length = 150)

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.university_name
    class Meta:
        ordering=['university_name']
        verbose_name_plural = "Universities"

class Department(models.Model):
    dep_name = models.CharField(max_length=150)

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.dep_name
    class Meta:
        ordering=['dep_name']

class Professor(models.Model):
    name = models.CharField(max_length = 50)

    university = models.ForeignKey(University)
    rating_value = models.FloatField(default=0)
    easiness_value = models.FloatField(default=0)
    department = models.ManyToManyField(Department)#, related_name='prof_dept')

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)
    def __str__(self):
        return self.name+" : "+self.university.university_name
    class Meta:
        ordering=['name']

class Course(models.Model):
    course_id = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)

    university = models.ForeignKey(University)
    department = models.ForeignKey(Department,null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.course_id+" : "+self.course_name

    class Meta:
        ordering=['course_id','course_name']

class Section(models.Model):
    course = models.ForeignKey(Course)
    section_id = models.CharField(max_length=5)
    registration_code = models.CharField(max_length=15)
    professor = models.ManyToManyField(Professor)
    location = models.CharField(max_length=50)
    location2 = models.CharField(max_length=50)

    class_type = models.CharField(max_length=25)
    class_type2 = models.CharField(max_length=25)
    time = models.CharField(max_length=50)
    time2 = models.CharField(max_length=50)
    days = models.CharField(max_length=5)
    days2 = models.CharField(max_length=5)

    date_range = models.CharField(max_length=50)
    date_range2 = models.CharField(max_length=50)
    schedule_type = models.CharField(max_length=50)
    schedule_type2 = models.CharField(max_length=50)

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default = timezone.now, blank=True)

    def __str__(self):
        return self.course.course_id+" : "+self.course.course_name+" : "+self.section_id

    class Meta:
        ordering=['course__course_id','course__course_name','section_id']

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

