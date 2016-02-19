from django.contrib import admin

from django.contrib import admin
from .models import Event, EventVote, SuggestedEventDate, Profile, Comment

admin.site.register(Event)
admin.site.register(EventVote)
admin.site.register(SuggestedEventDate)
admin.site.register(Profile)
admin.site.register(Comment)
# Register your models here.

