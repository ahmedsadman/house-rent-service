# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    house_name = models.CharField(max_length=30)
    house_size = models.IntegerField()
    family_allowed = models.BooleanField()
    office_allowed = models.BooleanField()
    bachelors_allowed = models.BooleanField()
    creation_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.pk})