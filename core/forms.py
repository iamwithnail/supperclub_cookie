from django import forms

from .models import Event, Comments

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('date',
                  'location_title',
                  'location_code',
                  'title',
                  'picture_url',
                  'notes',
                  'additional_notes',
                  'confirmed',
                  'booked',
                  'event_url',)


class CommentForm(forms.ModelForm):

    #don't use the auto gen for this one, need to populate.
    class Meta:
        model = Comments

        fields = ('comment','timestamp', 'event', 'user')

