from django.conf.urls import patterns, include, url
from tokoku.views import * 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from tokoku import SSLMiddleware
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^homeold/$', 'tokoku.views.homeold', name='homeold'),
    url(r'^klinik5/$', klinik5, name='klinik5'),
    url(r'^Rumah2Lantai/$', Rumah2Lantai, name='Rumah2Lantai'),
    url(r'^horseinline/$', horseinline, name='horseinline'),
    url(r'^klinikinline/$', klinikinline, name='klinikinline'),
    url(r'^article/add/$', permission_required('perm')(articleCreate.as_view()), name='article-add'),   
    url(r'^article/detail/(?P<slug>[-\w]+)/$', articleDetail.as_view(), name='article-detail'),   
    url(r'^article/(?P<slug>[-\w]+)/delete/$', permission_required('perm')(articleDelete.as_view()), name='article-delete'),   
    url(r'^article/(?P<slug>[-\w]+)/update/$', permission_required('perm')(articleUpdate.as_view()), name='article-update'),
    url(r'^article/list/$', articleList.as_view(), name='article-list'),      

    url(r'^$', 'tokoku.views.home', name='home'),
    url(r'^about/$', about, name='about'),
    #url(r'^faq/$', faq, {'SSL':True}, name='faq'),	
    url(r'^faq/$', faq, name='faq'),
    url(r'^search/$', search, name='search'),
    # url(r'^tokoku/', include('tokoku.foo.urls')),
    url(r'^shop_map/$', 'tokoku.views.shop_map', name='shop_map'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #The following line, to restrict view using staff_member_required, work flawlessly!
    #url(r'^contact/$', staff_member_required(ContactView.as_view()), name='contact_us'),
    url(r'^contact/$', ContactView.as_view(), name='contact_us'),
    url(r'^contact/thanks/$', contact_thanks, name='contact_thanks'),
    #next two lines, to be deleted
    #url(r'^contact/$', contact, name='contact_us'),
    #url(r'^contact/thanks/$', contact_thanks, name='contact_thanks'),



)

urlpatterns += patterns('',
    url(r'^accounts/', include('myauth.urls')),
)

urlpatterns += patterns('',
    (r'^shop/', include('shop.urls')),
)

urlpatterns += patterns('',
    url(r'^geo/', include('geo.urls')),
)


