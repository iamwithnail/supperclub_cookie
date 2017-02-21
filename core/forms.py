from django import forms

from .models import Event, Comment

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    location_title = forms.CharField()
    location_code = forms.CharField()
    title = forms.CharField()
    picture_url = forms.URLField()

    class Meta:
        model = Event
        exclude = ('event_url','picture_url')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('', )
