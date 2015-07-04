from django.conf.urls import *
from shop.views import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
#@staff_member_required



urlpatterns = patterns('',
    (r'^$', index, { 'template_name':'shop/index.html'}, 'catalog_home'),
    (r'^category/all/$', show_all_category, {'template_name':'shop/all_category.html'},'catalog_category'),
    (r'^category/(?P<category_slug>[-\w]+)/$', show_category, {'template_name':'shop/category.html'},'catalog_category'),
    (r'^product/(?P<product_slug>[-\w]+)/$', show_product, {'template_name':'shop/product_detail.html'},'catalog_product'),

    (r'^cart/$', show_cart, { 'template_name': 'shop/cart.html' }, 'show_cart'),



    #url(r'^add_product/$', productCreate.as_view(), name='product-add'),
    url(r'^add_product/$', permission_required('perm_list')(productCreate.as_view()), name='product-add'),   
    #url(r'^update_product/(?P<slug>[-\w]+)/$', productUpdate.as_view(), name='product-update'),
    url(r'^update_product/(?P<slug>[-\w]+)/$', permission_required('perm_list')(productUpdate.as_view()), name='product-update'),
    url(r'^list_product/$', productList.as_view(), name='product-list'),
    #url(r'^delete_product/(?P<slug>[-\w]+)/$', productDelete.as_view(), name='product-delete'),
    url(r'^delete_product/(?P<slug>[-\w]+)/$', permission_required('perm_list')(productDelete.as_view()), name='product-delete'),


    url(r'^add_to_cart/(?P<product_slug>[-\w]+)/$', addToCart, { 'template_name':'shop/cart.html'}, 'cartItem-add'),
    #url(r'^delete_cartitem/(?P<pk>\d+)/$', cartItemDelete.as_view(), name='cartitem-delete'),	#not endorsed!
    url(r'^del_cartitem/(?P<slug>[-\w]+)/$', cartItemDel, { 'template_name':'shop/cart.html'}, 'cartItem-del'),


    url(r'^order/(?P<pk>\d+)/receipt/$', orderReceipt, { 'template_name':'shop/order_receipt.html'}, 'order-receipt'),
    url(r'^neworder/$', orderCreate.as_view(), name='order-add'),
    url(r'^order/list/$', permission_required('perm_list')(orderList.as_view()), name='order-list'),
    #url(r'^order/detail/(?P<pk>\d+)/$', permission_required('perm')(orderDetail.as_view()), name='order-detail'),
    url(r'^order/detail/(?P<pk>\d+)/$', orderDetail.as_view(), name='order-detail'), #temporary permission
    url(r'^order/update/(?P<pk>\d+)/$', permission_required('perm_list')(orderUpdate.as_view()), name='order-update'),


    #url(r'^paypalrest/$', paypalrestCreate.as_view(), name='paypalrest-add'),
    url(r'^order/(?P<pk>\d+)/paypalrest/$', paypalrestCreate.as_view(), name='paypalrest-add'),





)

