from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import (
    Http404,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect

from . import app_settings, signals
from .forms import (
    LoginForm,
    ResetPasswordForm,
    SignupForm,
    )
from allauth.account.views import SignupView, LoginView

class SignupView(SignupView):
    template_name = "account/signup.html"

class LoginView(LoginView):
    template_name = "account/login.html"

def dashboard(request):

    return render(request, 'account/dashboard.html', context={"dashboard": dashboard})