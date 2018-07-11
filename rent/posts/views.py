# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from . import forms
from posts.models import Post, District, Area, Images
from django.utils import timezone
from django.forms.models import modelformset_factory
from django import forms as django_forms
import posts.api as api
from django.contrib import messages
from django.contrib.auth.models import User


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
        obj = Area.objects.filter(
            district__district_name=request.POST.get('user_choice'))

        for i in obj:
            html_response += '<option value="%s">%s</option>' % (
                i.pk, i.area_name)
        return HttpResponse(html_response)


@login_required
def create_post(request):
    ImageFormSet = modelformset_factory(Images, form=forms.ImageForm, extra=3)

    if request.method == 'POST':
        postForm = forms.PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            user = get_object_or_404(User, username=request.user.username)
            req = api.Caas('password', user.userprofile.phone_no, 'APP_000001')
            

            if not req.direct_debit('25601', '50'):
                messages.error(request, 'An error occured while trying to debit from the user account')
                return render(request, 'posts/post_form.html', context={'form': postForm, 'formset': formset})

            post_form = postForm.save(commit=False)
            post_form.author = request.user
            post_form.creation_date = timezone.now()
            post_form.save()

            # handling images
            if len(request.FILES) > 0:
                for i in range(len(request.FILES)):
                    image = formset.cleaned_data[i]['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            return render(request, 'posts/post_detail.html', context={'post': post_form})
        else:
            print(postForm.errors, formset.errors)

    else:
        postForm = forms.PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        return render(request, 'posts/post_form.html', context={'form': postForm, 'formset': formset})
