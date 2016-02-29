from __future__ import unicode_literals

from django.db import models
from config.settings.common import AUTH_USER_MODEL as User
from django.utils.text import slugify
# Create your models here.

class Event(models.Model):

    date = models.DateField()
    location_title = models.TextField()
    location_code = models.TextField(blank=True, null=True)
    title = models.TextField()
    picture_url = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    confirmed = models.BooleanField()
    booked = models.BooleanField()
    event_url = models.SlugField(unique=True)

    def __str__(self):
        return self.title + " " + str(self.date)


class SuggestedEventDate(models.Model):
    event = models.ForeignKey(Event)
    date = models.DateField()

    def __str__(self):
        return self.event.title

class EventVote(models.Model):
    suggested_date = models.ForeignKey(SuggestedEventDate)
    user = models.ForeignKey(User)
    vote = models.BooleanField()

    def __str__(self):
        return self.suggested_date.event.title + " " + self.user.first_name + " " + str(self.vote)


class Profile(models.Model):
    picture_url = models.URLField(name='picture', blank=True, null=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.first_name


class Comment(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    comment = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.user.first_name + " " + self.comment

""" event_dates = EventDate.objects.filter(event.pk=pk).fetch_related(EventVote) """


"""Event > EventDate(s)
            >> EventVote(s)  >> User """

""" Need to be able to add an event
    Add a user (admin)
    Email users of event (backend)
    Email reminder(s)
    Vote on event date(s)
    See votes on event date(s). """
