# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from django.template import RequestContext
from django.views.generic import TemplateView

from myauth.urls import *

"""
Workaround for migrating direct_to_template function to DirectTemplateView
"""
from django.views.generic import TemplateView

"""
Views for django-signup.
"""

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.models import User
from myauth.models import SignUpProfile, MyUser
from myauth.forms import SignUpForm, ActivateForm
import datetime
from django.contrib.sites.models import get_current_site



def index(request, template_name="myauth/index.html"):
    page_title = 'Accounts page'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def login(request, template_name="myauth/login.html"):
    page_title = 'Login page'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def logout(request, template_name="myauth/logout.html"):
    page_title = 'Logout page'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

class profile(TemplateView):
   template_name = "myauth/profile.html"


class DirectTemplateView(TemplateView):
    extra_context = None
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if self.extra_context is not None:
            for key, value in self.extra_context.items():
                if callable(value):
                    context[key] = value()
                else:
                    context[key] = value
        return context




def _send_activation_email(profile):
    # Render activation email
    message = render_to_string('myauth/activation_email.txt',
	{'signup_key': profile.signup_key,
        'expiration_days': settings.SIGNUP_EXPIRY_DAYS,
        'site': get_current_site})

    subject = render_to_string('myauth/activation_email_subject.txt')
        # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    # Send activation email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [profile.email,],
                fail_silently=False)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # Generate and send activation email
            _send_activation_email(instance)
            return HttpResponseRedirect('/accounts/signup/checkyouremail')
    else:
        form = SignUpForm()
    return render_to_response('myauth/signup_form.html', {'form': form},
		context_instance=RequestContext(request))


def activate(request, signup_key):
    # Try and get a sign up profile that matches activation key
    # Redirect to failure page if no match
    try:
        profile = SignUpProfile.objects.get(signup_key=signup_key)
    except:
        return HttpResponseRedirect('/accounts/signup/key_invalid')

    # Check if profile has expired
    if profile.expiry_date > datetime.datetime.now():    
					#related with USE_TZ in settings.py!
        if request.method == 'POST':
            form = ActivateForm(request.POST)
            if form.is_valid():
                # Create a new User instance
                user = MyUser(email=profile.email)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                # Delete the sign up profile
                profile.delete()
                return HttpResponseRedirect('/accounts/signup/success')
        else:
            form = ActivateForm()
    else:
        # Delete expired sign up profile and show invalid key page
        profile.delete()
        return HttpResponseRedirect('/accounts/signup/key_invalid')
    return render_to_response('myauth/activate_form.html', {'form': form, 'user': profile.email},  
		context_instance=RequestContext(request))



