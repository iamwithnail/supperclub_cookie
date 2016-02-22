from django.shortcuts import render, redirect
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
    for comment in comments:
        profile = Profile.objects.get(user=comment.user)
        temp_comment = {"text": comment.comment,
                         "user": comment.user,
                         "picture": profile.picture,
                        "timestamp": comment.timestamp,
        }
        final_comments.append(temp_comment)
    print final_comments


    #add list of next five events - use the initial events query Event + next 5 ordered by
    #date, then split out into current (single object) and future (list of events)

    print event
    return render(request, 'core/event.html', {"event": event, "comments": final_comments, "future_events": future_events})

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
        form = CommentForm(request.POST)

        print request.POST
        import datetime
        print "DEBUG FORM", form
        comment = form.save(commit=False)
        comment.user = request.user
        comment.timestamp = datetime.datetime.now()
        print comment.user, comment.timestamp, comment.comment
        comment.save()
        print "DEBUG", comment
        return redirect('events/{{comment.event.event_url}}')
    else:
        print "DEBUG else"
        form = CommentForm()

    return render(request, 'core/event.html', {"form": form})


