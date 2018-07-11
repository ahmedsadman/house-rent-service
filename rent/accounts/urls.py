from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from . import forms

app_name = 'accounts'

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(
        template_name='accounts/login.html', authentication_form=forms.CustomAuthForm), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup'),
    url(r'dashboard/$', views.user_dashboard, name='dashboard'),
]