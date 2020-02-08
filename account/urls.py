from django.urls import path, re_path
from allauth.account.views import login
from . import views
from account import views as user_views


urlpatterns = [
    path('signup/', user_views.SignupView.as_view(template_name="account/signup.html"), name='signup'),
    path('login/', user_views.SignupView.as_view(template_name="account/login.html"), name='login'),
]
