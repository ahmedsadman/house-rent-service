# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from . import forms
from posts.models import Post, District, Area
from django.utils import timezone


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_detail.html'
    form_class = forms.PostForm
    model = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.creation_date = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PostDetailView(DetailView):
    model = Post


# handle ajax request to update locations based on district
def get_location_data(request):
    print("execute successful")
    if request.is_ajax():
        html_response = ""
        obj = Area.objects.filter(district__district_name = request.POST.get('user_choice'))

        for i in obj:
            html_response += '<option value="%s">%s</option>' % (i.pk, i.area_name)
        return HttpResponse(html_response)
        