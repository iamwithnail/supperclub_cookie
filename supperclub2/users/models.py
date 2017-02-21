# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):


    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def save(self, *args, **kwargs):
        from core.models import Profile
        from django.core.exceptions import MultipleObjectsReturned
        try:
            super(AbstractUser, self).save(*args, **kwargs)
            profile, _ = Profile.objects.get_or_create(user=self)
        except MultipleObjectsReturned:
            profile = Profile.objects.filter(user=self)[0]
            #raise error to admin








