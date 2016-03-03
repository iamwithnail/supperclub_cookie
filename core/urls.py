"""supperclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
import views
from .models import Event

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^suggested-dates/(?P<event_slug>[^/]+)', views.suggested_event_dates, name="event_dates"),
    url(r'^events/(?P<event_slug>[^/]+)$', views.event, name="events"),
    url(r'^add_event', views.add_event, name='add_event'),
    url(r'^new_comment', views.new_comment, name='new_comment'),
    url(r'^all_events', views.EventsListView.as_view(queryset=Event.objects.all()), name='all_events'),
    url(r'random', views.random, name='random'),
    url(r'^', TemplateView.as_view(template_name='core/index.html')),
    #url(r'^events/', views.event),
]

    #url(r'^fixtures/(?P<league>[^/]+)/(?P<date_in>[^/]+)/$', ('core.views.fixtures')),

    #url(r'^matchbydate/(?P<date_in>[^/]+)/$', ('core.views.view_all_matches_for_date')),