from django.contrib import admin
from geo.models import Geoname

class GeonameAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    search_fields = ('name', 'latitude', 'longitude')
    ordering = ('name',)


admin.site.register(Geoname, GeonameAdmin)

