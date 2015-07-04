from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from geo.models import Geoname
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


urlpatterns = patterns('',
    url(r'^$', ListView.as_view( 
               model=Geoname, 
               template_name = 'geoname_list.html',
               paginate_by=50 )),
#               paginate_by=50,
#               context_object_name="geox_list", ))  #this works, default to geoname_list
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
                           model=Geoname,
                           template_name='geo/geoname_detail.html')),


)
