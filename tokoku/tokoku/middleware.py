#https://github.com/Matt-Stevens/Django-SSL-Redirect
#http://stackoverflow.com/questions/8436666/how-to-make-python-on-heroku-https-only
from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class SSLRedirectMiddleware:

    def process_request(self, request):
        if not any([settings.DEBUG, request.is_secure(), request.META.get("HTTP_X_FORWARDED_PROTO", "") == 'https']):
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace("http://", "https://")
            return HttpResponsePermanentRedirect(secure_url)
