from __future__ import unicode_literals

from django.db import models
from config.settings.common import AUTH_USER_MODEL as User
from django.utils.text import slugify


class Event(models.Model):

    date = models.DateField()
    location_title = models.TextField()
    location_code = models.TextField(blank=True, null=True)
    picture_url = models.URLField(blank=True, null=True, max_length=250)
    event_url = models.SlugField(unique=True, max_length=250)

    def __str__(self):
        return self.event_url + " " + str(self.date)

    def save(self, *args, **kwargs):
        self.event_url = slugify(self.location_title+str(self.date))
        super(Event, self).save(*args, **kwargs)

class Profile(models.Model):
    picture_url = models.URLField(name='picture', blank=True, null=True)
    user = models.OneToOneField(User)
    twitter = models.CharField(blank=True, null=True, max_length=64)
    instagram = models.CharField(blank=True, null=True, max_length=64)
    #TODO: Probably move social fields to their own thing, OR use the AllAuth options.




    def __str__(self):
        return self.user.first_name


class Comment(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    comment = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.user.first_name + " " + self.comment
