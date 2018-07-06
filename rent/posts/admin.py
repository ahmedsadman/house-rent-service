# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from posts.models import Post, District, Area

# Register your models here.
admin.site.register(Post)
admin.site.register(District)
admin.site.register(Area)