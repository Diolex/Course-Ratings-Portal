from django.contrib import admin
from courses.models import Dates, University, Department, Course, Professor, User, Rating, Search
# Register your models here.
admin.site.register(Dates)
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Search)
