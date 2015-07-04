def ga_key(request):
    from django.conf import settings
    return {'ga_key': settings.GOOGLE_ANALYTICS_KEY}
