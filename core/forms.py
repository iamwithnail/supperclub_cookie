from django import forms

from .models import Event, Comment

class EventForm(forms.ModelForm):
    name = forms.CharField()
    date = forms.DateField(widget=forms.SelectDateWidget)
    location_title = forms.CharField()
    location_code = forms.CharField()
    title = forms.CharField()
    picture_url = forms.URLField()
    notes = forms.CharField()
    additional_notes = forms.CharField()
    confirmed = forms.BooleanField()
    booked = forms.BooleanField()

    class Meta:
        model = Event
        exclude = ('event_url',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('', )
