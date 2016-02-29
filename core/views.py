from django.shortcuts import render, redirect
from config.settings.common import AUTH_USER_MODEL as User
from .models import Event

# Create your views here.

def main(request):
    return render(request, 'core/index.html')

def random(request):
    return render(request, 'core/core/basetest.html')

from django.views.generic import ListView

def all_events(request):
    from .models import Event
    events = Event.objects.all()
    return render(request, 'core/event_list.html', {"events": events})


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
        print "DEBUG", comment
        return redirect('events/' + event.event_url)
    else:
        print "DEBUG else"
        form = CommentForm()

    return render(request, 'core/event.html', {"form": form})


def suggested_event_dates(request, event_slug):
    from .models import Event, SuggestedEventDate, EventVote
    event_object = Event.objects.get(event_url=event_slug)
    suggested_dates = SuggestedEventDate.objects.filter(event=event_object).prefetch_related()

    all_users = User.objects.all()
    user_votes = EventVote.objects.filter(suggested_date__in=suggested_dates).\
        prefetch_related().order_by('suggested_date')
    dates_response = {}
    """for suggestion in suggested_dates:
        dates_response[suggestion] = {}
        for u in all_users:
            for v in in user_votes:
                if
                pass

    for user in all_users:
        if user not in user_votes:

       """

    print all_users
    print user_votes
    return render (request,
                   'core/suggested_dates.html',
                   {"suggested_dates": suggested_dates, "event": event_object, "user_votes": user_votes}
                   )
