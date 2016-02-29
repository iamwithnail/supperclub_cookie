from django import template

register = template.Library()

@register.inclusion_tag('core/comments.html', takes_context=True)
def show_comments(context):
    from core.models import Comment, Profile, Event
    from datetime import datetime
    comments = Comment.objects.filter(event__pk=context['event'].id).prefetch_related('user')
    from core.forms import CommentForm
    data = {"event": context['event'].id, "user": context['request'].user, "timestamp": datetime.now()}
    form = CommentForm(initial=data)
    form.user = context['request'].user
    form.event = context['event'].id
    print "DEBUG FORM"
    print form.event, form.user, form
    #prepoulate the form here - user = request.user, timestamp = now()
    #event = event_pk
    print "DEBUG COMMENETS TAG"
    for comment in comments:
        print comment.comment, comment.user, comment.timestamp

    final_comments = []
    for comment in comments:
        profile = Profile.objects.get(user=comment.user)
        temp_comment = {"comment": comment.comment,
                         "user": comment.user,
                         "picture": profile.picture,
                        "timestamp": comment.timestamp,
        }
        final_comments.append(temp_comment)
    return {"comments": final_comments, "form": form}

