from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import forms
from posts.models import Post
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from posts.api import Subscribe
import logging

logger = logging.getLogger(__name__)

# class HomePage(TemplateView):
#     template_name = 'index.html'


def index(request):
    if request.method == 'POST':
        search_form = forms.SearchForm(data=request.POST)

        if search_form.is_valid():
            district_name = search_form.cleaned_data['district']
            area_name = search_form.cleaned_data['area']
            family = search_form.cleaned_data['family_allowed']
            office = search_form.cleaned_data['office_allowed']
            bachelor = search_form.cleaned_data['bachelors_allowed']
            allowed_types = {
                'family_allowed': family,
                'office_allowed': office,
                'bachelors_allowed': bachelor
            }

            # filtering
            results = Post.objects.filter(district=district_name)

            # show specific area ads if selected, otherwise all
            if area_name:
                results = results.filter(area=area_name)

            # show the ads based on selected critera, if none selected, show all
            if family:
                results = results.filter(family_allowed=family)
            if office:
                results = results.filter(office_allowed=office)
            if bachelor:
                results = results.filter(bachelors_allowed=bachelor)

            return render(request, 'search_results.html', context={'results': results})
        else:
            print(search_form.errors)

    else:
        search_form = forms.SearchForm()

    return render(request, 'index.html', context={'search_form': search_form})


# this view func handles the sms sent by users
# the decorator bypassess csrf check
@csrf_exempt
def process_user_sms(request):
    if request.method == 'POST':
        print("EXECUTING RECEIVE______")
        recv = json.loads(request.body.decode('utf-8'))
        print(recv)
        logger.error(recv)

        username = recv['message'].split()[1]
        userob = get_object_or_404(User, username=username)

        # subscribe the user
        api = Subscribe(recv['sourceAddress'])
        # if api.opt_in():
        #     userob.userprofile.masked_id = recv['sourceAddress']
        #     userob.userprofile.is_subscribed = True
        api.opt_in()
        userob.userprofile.masked_id = recv['sourceAddress']
        userob.userprofile.is_subscribed = True

        # save the updated user data
        userob.save()
        userob.userprofile.save()
        return HttpResponse("OK")
