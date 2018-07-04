# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView, ListView
from django.contrib import messages
from accounts.models import UserProfile
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


class SignUp(CreateView):
    form_class = forms.CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        c = {'form': form}
        user = form.save(commit=False)

        # cleaned data
        phone_number = form.cleaned_data['phone_no']
        address = form.cleaned_data['address']
        password = form.cleaned_data['password']
        password2 = form.cleaned_data['password2']

        # confirm password
        if password and password2 and password != password2:
            messages.error(self.request, "Passwords do not Match",
                           extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user.set_password(password)
        user.save()

        # create user-profile model with extra info
        UserProfile.objects.create(
            user=user, phone_no=phone_number, address=address)

        return super().form_valid(form)


# handles the user dashboard
@login_required
def user_dashboard(request):
    objects = Post.objects.filter(
        author=request.user).order_by('-creation_date')
    return render(request, 'accounts/dashboard.html', {'post_list': objects})
