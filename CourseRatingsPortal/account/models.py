from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique = True)
    url = models.URLField(blank = True)
    year = models.PositiveSmallIntegerField(default=1)

    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_modified = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ['user__last_name']

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
