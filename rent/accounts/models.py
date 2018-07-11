# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=13)
    address = models.CharField(max_length=100)

    # use the ratings relation here, and add a generic field
    # like {% ratings user.userprofile %}