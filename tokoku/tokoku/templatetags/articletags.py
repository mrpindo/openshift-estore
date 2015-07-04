
from tokoku.models import Article
from django import template
#from shop import cart

 
register = template.Library()
 
@register.inclusion_tag('article/latest4_article_title.html', takes_context=True)
def latest4_article_title(context):
    latest4_article_title = Article.objects.order_by('-id')[:4]
    return {'latest4_article_title': latest4_article_title}


@register.inclusion_tag('article/latest4_article_teaser.html', takes_context=True)
def latest4_article_teaser(context):
    latest4_article_teaser = Article.objects.order_by('-id')[:4]
    return {'latest4_article_teaser': latest4_article_teaser}

@register.inclusion_tag('article/random4_article_teaser.html', takes_context=True)
def random4_article_teaser(context):
    random4_article_teaser = Article.objects.order_by('?')[:4]
    return {'random4_article_teaser': random4_article_teaser}


#@register.inclusion_tag('shop/etalase_list_new.html', takes_context=True)
#def shop_etalase2(context):
#    etalase_list2 = Product.objects.filter(is_active=1).order_by('?')[:8]
#    return {'MEDIA_URL': context['MEDIA_URL'], 'etalase_list2': etalase_list2}

#@register.inclusion_tag("shop/cart_box.html")
#def cart_box(request):
#    cart_item_count = cart.cart_distinct_item_count(request)
#    cart_subtotal = cart.cart_subtotal(request)		
#    return {'cart_item_count': cart_item_count, 'cart_subtotal': cart_subtotal }

