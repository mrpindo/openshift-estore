from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
#from views import index, login, logout, profile
from myauth.views import *

urlpatterns = patterns('',
    url(r'^$', index, { 'template_name':'myauth/index.html'}, 'accounts_home'),

    url(r'^login/$', 'django.contrib.auth.views.login', 
		{'template_name': 'myauth/login.html'}, 'myauth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', 
		{ 'template_name': 'myauth/logout.html' }, 'myauth_logout'),

    url(r'^profile/$', profile.as_view()),

    #Temporary blocked
    url(r'^password/change/$', 'django.contrib.auth.views.password_change', 
    		{'template_name': 'myauth/password_change_form.html'}, 
    			'password_change'),
    url(r'^password/change_done/$', 'django.contrib.auth.views.password_change_done', 
    		{'template_name': 'myauth/password_change_done.html'}, 
    			'password_change_done'),
 

    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', 
		{'template_name': 'myauth/password_reset_form.html'}, 
			'password_reset'),

    #note: uidb36  for Django <= 1.5
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 		'django.contrib.auth.views.password_reset_confirm', 
		{'template_name': 'myauth/password_reset_confirm.html'}, 
			'password_reset_confirm'),

    url(r'^password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', 
		{'template_name': 'myauth/password_reset_complete.html'}, 
			'password_reset_complete'),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done', 
		{'template_name': 'myauth/password_reset_done.html'}, 
			'password_reset_done'),

)



"""
URLconf for django-signup.
"""

urlpatterns += patterns('',
    url(r'^signup/$', signup, name='myauth_signup'),

    (r'^signup/checkyouremail/$',
	DirectTemplateView.as_view(template_name='myauth/registration_complete.html')),

    (r'^signup/activate/(?P<signup_key>[-\w]+)/$', activate),

    (r'^signup/key_invalid/$',
	DirectTemplateView.as_view(template_name='myauth/key_invalid.html')),

    (r'^signup/success/$',
 	DirectTemplateView.as_view(template_name='myauth/signup_successful.html')),

)

