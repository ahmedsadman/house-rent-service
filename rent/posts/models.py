# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class District(models.Model):
    district_name = models.CharField(max_length=50)

    def __str__(self):
        return self.district_name


class Area(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=50)

    def __str__(self):
        return self.area_name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    house_size = models.IntegerField()
    address = models.CharField(max_length=255)
    description = models.TextField()
    family_allowed = models.BooleanField()
    office_allowed = models.BooleanField()
    bachelors_allowed = models.BooleanField()
    creation_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s - %s - %s" % (self.pk, self.author.username, self.creation_date)