from django.shortcuts import render, redirect
from supperclub2.users.models import User
from .models import Event
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def main(request):
    return render(request, )

def random(request):
    return render(request, 'core/core/basetest.html')

from django.views.generic import ListView

"""
def all_events(request):
    from .models import Event
    events = Event.objects.all()
    return render(request, 'core/event_list.html', {"events": events})
"""

class EventsListView(LoginRequiredMixin, ListView):
    template_name = 'core/event_listhtml'
    model = Event

def event(request, event_slug):
    from .models import Event, Comment, Profile
    event = Event.objects.get(event_url=event_slug)
    future_events = Event.objects.filter(date__gt=event.date)
    print "FUTURE", future_events
    comments = Comment.objects.select_related('user').filter(event=event)
    final_comments = []


    #add list of next five events - use the initial events query Event + next 5 ordered by
    #date, then split out into current (single object) and future (list of events)

    print event
    return render(request, 'core/event.html', {"event": event, "future_events": future_events})

def add_event(request):
    from forms import EventForm
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('events', event.event_url)
    else:
        form = EventForm()
    return render(request, 'core/add_event.html', {"form": form})

def new_comment(request):
    from forms import CommentForm
    print request.POST
    print request.path_info
    if request.method == "POST":
        import datetime
        form = CommentForm(request.POST)
        print "DEBUG FORM", form
        comment = form.save(commit=False)
        comment.user = request.user
        comment.timestamp = datetime.datetime.now()
        print comment.user, comment.timestamp, comment.comment
        comment.save()
        event = Event.objects.get(id=request.POST['event'])
        return redirect('events/' + event.event_url)
    else:
        print "DEBUG else"
        form = CommentForm()

    return render(request, 'core/event.html', {"form": form})

def manage_reviews(reviews_dict):
    #pass

def manage_photos(photos_dict):
    #pass


def get_place_details(google_place_id='ChIJO4rSTqADdkgRWXF0GwEEESg'):
    #default to peckham plex for now
    import requests
    key ="AIzaSyDJLGzlgU8zlLqjPttZqvnp2-H01bBxUH8"
    BASE_URL = 'https://maps.googleapis.com/maps/api/place/details/json?placeid='
    request_url = BASE_URL+google_place_id+'&key='+key
    results = requests.get(request_url)['result']
    #supplies website, utc_offset, name, reference, photos, geometry, adr_adress
    #vicinity, reviews, formatted_phone_number,


