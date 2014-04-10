from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Search(models.Model):
    user = models.ForeignKey(User)
    search_parameters = models.CharField(max_length=150)

