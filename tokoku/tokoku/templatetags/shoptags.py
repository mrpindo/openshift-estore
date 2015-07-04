
from shop.models import Product
from django import template
from shop import cart

 
register = template.Library()
 
@register.inclusion_tag('shop/etalase_list.html', takes_context=True)
def shop_etalase(context):
    #etalase_list = Product.objects.order_by('?')[:10]
    etalase_list = Product.objects.filter(is_active=1).order_by('?')[:8]
    return {'MEDIA_URL': context['MEDIA_URL'], 'etalase_list': etalase_list}

#@register.inclusion_tag('shop/etalase_list_new.html', takes_context=True)
#def shop_etalase2(context):
#    etalase_list2 = Product.objects.filter(is_active=1).order_by('?')[:8]
#    return {'MEDIA_URL': context['MEDIA_URL'], 'etalase_list2': etalase_list2}

@register.inclusion_tag("shop/cart_box.html")
def cart_box(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    cart_subtotal = cart.cart_subtotal(request)		
    return {'cart_item_count': cart_item_count, 'cart_subtotal': cart_subtotal }


@register.inclusion_tag('shop/random4_product_name.html', takes_context=True)
def random4_product_name(context):
    random4_product_name = Product.objects.filter(is_active=1).order_by('?')[:4]
    return {'random4_product_name': random4_product_name}


@register.inclusion_tag('shop/bestselling4_product_name.html', takes_context=True)
def bestselling4_product_name(context):
    from django.db.models import Count
    bestselling4_product_name = Product.objects.filter(is_active=1).annotate(num_prod=Count('orderitem')).order_by('-num_prod')[:4]
    return {'bestselling4_product_name': bestselling4_product_name}

