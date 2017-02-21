# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User





def profile(request, username):
    from django.core.exceptions import ObjectDoesNotExist

    from core.models import Profile
    print request.user
    print username
    import cloudinary
    import cloudinary.uploader
    cloudinary.config(
        cloud_name="dvkkjwzjq",
        api_key="486615593347826",
        api_secret="6uWQ8vTHTEkKh1l7rGo0D1wA-j8"
    )

    if request.method == 'POST':
        try:
            profile = Profile.objects.get(user=request.user)
        except(ObjectDoesNotExist):
            profile = Profile()
            profile.user = request.user
        print request
        print "FILES", request.FILES
        profile_picture = request.FILES['profile_photo']
        print "Profile picture", type(profile_picture)
        uploaded_image = cloudinary.uploader.upload(profile_picture)
        print "PAST THE UPLOAD", uploaded_image
        filename=uploaded_image["secure_url"]
        print filename
        profile.picture = filename
        print profile.picture
        profile.save()
    if request.method == 'GET':
        try:
            profile = Profile.objects.get(user=request.user)
        except(ObjectDoesNotExist):
            return render(request, 'users/profile.html', {"user": request.user, "profile": ""})
    else:
        pass
    return render(request, 'users/profile.html', {"user": request.user, "profile": profile})



class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
