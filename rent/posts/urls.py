from django.conf.urls import url
from . import views


app_name = 'posts'

urlpatterns = [
    # url(r'^new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^new/$', views.create_post, name='post_new'),
    url(r'^get_location/$', views.get_location_data, name='get_location'),
    url(r'^(?P<pk>\d+)', views.PostDetailView.as_view(), name='post_detail')
]