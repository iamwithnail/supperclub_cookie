from django import template

register = template.Library()

@register.inclusion_tag('core/comments.html')
def show_comments(event_pk):
    from core.models import Comment, Profile
    # from supperclub2.users import
    comments = Comment.objects.filter(event__pk=event_pk).prefetch_related('user')

    print "DEBUG CMMNETS TAG"
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
    return {"comments": final_comments}
