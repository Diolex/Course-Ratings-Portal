from django.contrib import admin
from courses.models import University, Department, Course, Section, Professor, Rating
# Register your models here.
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Professor)
admin.site.register(Rating)
