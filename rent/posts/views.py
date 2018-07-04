# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from . import forms
from posts.models import Post
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