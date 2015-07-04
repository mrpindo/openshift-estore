from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from shop.models import *
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# this stuff goes at the top of the file, below other imports
from django.core import urlresolvers
#from shop.checkout import process, send_order_email
from django.core.mail import send_mail
import shop.cart
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from shop.forms import *
from myauth.models import MyUser
from shop import cart
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse, reverse_lazy


def index(request, template_name):
    page_title = 'Welcome Shoppers'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def show_all_category(request, template_name):
    #product_list = Product.objects.all()
    product_list = Product.objects.filter(is_active=1)
    paginator = Paginator(product_list, 12)  

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def show_category(request, category_slug, template_name="shop/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    product_list = c.product_set.all()
    page_title = c.name
    paginator = Paginator(product_list, 12)  

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render_to_response(template_name, locals(),context_instance=RequestContext(request))



# new product view, with POST vs GET detection
def show_product(request, product_slug, template_name="shop/product_detail.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.all()
    page_title = p.name
    # need to evaluate the HTTP method
    if request.method == 'POST':
      # add to cart...create the bound form
      postdata = request.POST.copy()
      form = ProductAddToCartForm(request, postdata)
      #check if posted data is valid
      if form.is_valid():
        #add to cart and redirect to cart page
        shop.cart.add_to_cart(request)
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
          request.session.delete_test_cookie()
          url = urlresolvers.reverse('show_cart')

        # send message	#add by endik
        messages.add_message(request, messages.SUCCESS, p.name +', telah ditambahkan..')

        return HttpResponseRedirect(url)
    else:
      #it's a GET, create the unbound form. Note request as a kwarg
      form = ProductAddToCartForm(request=request, label_suffix=':')

    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set the test cookie on our first GET request
    request.session.set_test_cookie()


    return render_to_response(template_name, locals(),context_instance=RequestContext(request))




####################################################
### Checkout part, follows
### based on (partially):
### 1. Python/Package_Source/Beginning_Django_Ecommerce_source/Chapter_01-15/ecomstore/checkout
### 2. Python/Package_Source/stephenmcd-cartridge-shop  
###
### Send receipt via email to customer
### send invoice via email to customer (pdf?)
###


'''Retired
def show_checkout(request, template_name='shop/checkout.html'):
    """ checkout form page to collect user shipping and billing information """
    if cart.is_empty(request):
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CheckoutForm(postdata)
        if form.is_valid():
            response = process(request)
            order_number = response.get('order_number',0)
            error_message = response.get('message','')
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = urlresolvers.reverse('checkout_receipt')
                return HttpResponseRedirect(receipt_url)
        else:
            error_message = 'Correct the errors below'
    else:
        #need further study ...
        #if request.user.is_authenticated():
            #user_profile = profile.retrieve(request)   #***
            #form = CheckoutForm(instance=user_profile)
        #else:
            form = CheckoutForm()
    page_title = 'Checkout'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
/Retired'''

class productList(ListView):
    model = Product
    fields = ('imgfile', 'name', 'slug', 'brand', 'sku', 'price', 'quantity', 'description', 'categories' ,)
    #context_object_name = "product_list"    #default is object_list	#not working?
    paginate_by = 40  

class productCreate(CreateView):
    model = Product
    form_class = addProductForm

class productUpdate(UpdateView):
    model = Product
    form_class = updateProductForm

class productDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')

#############################################################################################
#programmaticaly add a product with 1 qty to cart, from icon click in etalase (later in all products)
import random

CART_ID_SESSION_KEY = 'cart_id'

# get the current user's cart id, sets new one if blank
def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
      request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
      cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

def addToCart(request, template_name, product_slug):
    product2cartItem = Product.objects.get(slug=product_slug)
    qty2cartItem = 1

    cart_products = CartItem.objects.filter(cart_id=_cart_id(request))
    product_in_cart = False

    for cart_item in cart_products:
      if cart_item.product.id == product2cartItem.id:
        cart_item.augment_quantity(qty2cartItem)
        product_in_cart = True

    if not product_in_cart:                             #beware of indention, could be interpreted wrong!
        # create and save a new cart item
        ci = CartItem()
        ci.product = product2cartItem
        ci.imgthumb = product2cartItem.imgthumb			#New!, it Works!
        ci.quantity = qty2cartItem 
        ci.cart_id = _cart_id(request)
        ci.save()

    messages.add_message(request, messages.SUCCESS, product2cartItem.name +', telah ditambahkan..')
    url = urlresolvers.reverse('show_cart')
    return HttpResponseRedirect(url)


#class cartItemDelete(DeleteView):
#    model = CartItem
#    success_url = reverse_lazy('show_cart')
#    success_message = "telah dihapus.."		#failed!


def cartItemDel(request, template_name, slug):
    prod = Product.objects.get(slug=slug)
    cartid = _cart_id(request)
    ci = CartItem.objects.get(cart_id=cartid, product_id=prod.id)
    ci.delete()

    messages.add_message(request, messages.WARNING, ci.name +', telah dihapus..')
    url = urlresolvers.reverse('show_cart')
    return HttpResponseRedirect(url)


def show_cart(request, template_name="shop/cart.html"):
    if request.method == 'POST':
      postdata = request.POST.copy()
      if postdata['submit'] == 'Remove':
        shop.cart.remove_from_cart(request)
      if postdata['submit'] == 'Update':
        shop.cart.update_cart(request)

    cart_item_count = cart.cart_distinct_item_count(request)
    cart_subtotal = shop.cart.cart_subtotal(request)
    cart_items = shop.cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

#there is issue when user post more than one order at the same session!
def orderReceipt(request, template_name, pk):
    try:
      order = Order.objects.get(id=pk)
      order_items = OrderItem.objects.filter(order_id=pk, session_id=request.session[CART_ID_SESSION_KEY])
      lenoi = len(order_items)
    except:
      order = {}
      order_items = {}
      lenoi = 0

    if lenoi > 0:	
      from django.core.mail import EmailMultiAlternatives
      from django.template import loader, Context
      from django.contrib.sites.models import Site

      site_name = Site.objects.get_current().domain
      receipt_template = "shop/receipt_template.html"
      email_context = Context({ 'order': order, 'order_items': order_items, 'site_name': site_name })
      subject, from_email, to, cc, bcc = '[myshop-drindo] Order Successfully created.', 'myShop Support <no-reply@mycompany.com>', order.email, 'padangcuisine@gmail.com', 'rumahpribadi@gmail.com'
      text_content = "Thank you for shopping with us."
      html = loader.get_template(receipt_template)
      html_content = html.render(email_context)
      msg = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=[to], cc=[cc], bcc=[bcc])
      msg.attach_alternative(html_content, "text/html")
      msg.send()

      ##to attach some.txt file to message body see:
      ##ref:http://stackoverflow.com/questions/14011468/send-a-txt-with-send-mail-django
  

    else:
      cart_url = urlresolvers.reverse('show_cart')
      return HttpResponseRedirect(cart_url)

    session_id = request.session[CART_ID_SESSION_KEY]
    return render_to_response(template_name, {'order_items':order_items, 'order':order , 'session_id':session_id, 'lenoi':lenoi},context_instance=RequestContext(request))


class orderCreate(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order-receipt')

    def dispatch(self, request, *args, **kwargs):	
        # check if cart is empty
        if cart.is_empty(self.request):			#Works!
          cart_url = urlresolvers.reverse('show_cart')
          return HttpResponseRedirect(cart_url)
        else:
            return super(orderCreate, self).dispatch(request, *args, **kwargs)

    #def form_valid(self, form): 		#good for predefine any input field!
        #add additional activities here!
        #form.instance.user = self.request.user
        #form.instance.billing_state = 'XX'		#Works great!
        #form.instance.billing_state = 'XXXXXX'		#Error, exceeding 3 chars. Great!

        #if cart.is_empty(self.request):		#function replaced by def dispatch() line 295!
        #  cart_url = urlresolvers.reverse('show_cart')
        #  return HttpResponseRedirect(cart_url)

        #return super(orderCreate, self).form_valid(form)

        
    #both args=(self.object.id,) and kwargs={'pk': self.object.pk}  works Okay
    #def get_success_url(self): 
    #  return reverse('order-completed',args=(self.object.id,))
    def get_success_url(self):

      #copy each cartitem to orderitem
      cart_items = CartItem.objects.filter(cart_id=self.request.session[CART_ID_SESSION_KEY])
      for ci in cart_items:
        #""" create order item for each cart item """
        oi = OrderItem()
        oi.order_id = self.object.pk
        oi.session_id = ci.cart_id
        oi.quantity = ci.quantity
        oi.price = ci.price  # now using @property
        oi.product = ci.product
        oi.save()

      #*****How about shipping cost? deal with it later!

      #delete items in cart
      cart_items.delete()		#Maybe Temporary disabled
      

      return reverse('order-receipt', kwargs={'pk': self.object.pk})


class orderList(ListView):
    model = Order
    fields = ('id', 'status', 'user', 'transaction_id', 'created_at', 'updated_at',)
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_admin:
          return Order.objects.all()
        else:
          return Order.objects.filter(email=self.request.user)


class orderDetail(DetailView):
    model = Order
    template_name = 'shop/order_detail.html'

    def get_context_data(self, **kwargs):
      context = super(orderDetail, self).get_context_data(**kwargs)
      context['order_items'] = OrderItem.objects.filter(order=self.object.id)
      return context

    #def get_queryset(self):		#temporarily disabled
    #    if self.request.user.is_admin:
    #      return Order.objects.all()
    #    else:
    #      return Order.objects.filter(email=self.request.user)



class orderUpdate(UpdateView):
    model = Order
    form_class = updateOrderForm
    success_url = reverse_lazy('order-list')

    #def render_to_response(self, context):		#Works!
    #    if not self.request.user.is_admin:
    #      home_url = urlresolvers.reverse('home')
    #      return HttpResponseRedirect(home_url)

    #    return super(orderUpdate, self).render_to_response(context)


    def dispatch(self, request, *args, **kwargs):	#Works, much better than render_to_response(Why?)
        # check if user is not admin
        if not self.request.user.is_admin:
          cart_url = urlresolvers.reverse('show_cart')
          return HttpResponseRedirect(cart_url)
        else:
            return super(orderUpdate, self).dispatch(request, *args, **kwargs)

#SuccessMessageMixin works, but in rigid way, maybe useful in other implementation. messages.success(self.request, message) works much much better!
#from django.contrib.messages.views import SuccessMessageMixin
#class paypalrestCreate(SuccessMessageMixin, FormView):
    #success_message = "%(order_email)s, ********Payment created successfully"		#OK

import math
class paypalrestCreate(FormView):
    template_name = 'shop/paypalrest_form.html'
    form_class = PaymentForm

    def get_success_message(self, cleaned_data):
      order = Order.objects.get(id=self.kwargs['pk'])
      return self.success_message % dict(cleaned_data,
                                           order_email=order.email)

    def get_success_url(self):
      url = reverse_lazy('order-detail', kwargs={'pk': self.kwargs['pk']})
      return url

    def get_context_data(self, **kwargs):
      context = super(paypalrestCreate, self).get_context_data(**kwargs)
      order_id = self.kwargs['pk']
      order = Order.objects.get(id=order_id)
      context['order'] = order
      order_items = OrderItem.objects.filter(order=order_id)
      titems = 0
      for item in order_items:
        titems += math.ceil((item.price / 12000)*100)/100		#Converted to USD

      context['titems'] = str("%0.2f" % titems)
      return context


    def dispatch(self, request, *args, **kwargs):	
        order_id = self.kwargs['pk']
        try:		#order_status exists
          order_status = Order.objects.get(id=order_id).status
        except:		#order_status not exists
          url = urlresolvers.reverse('home')
          return HttpResponseRedirect(url)

        # check if order status is awaiting payment, if not redirect to order detail.
        if order_status != 2:	
          url = urlresolvers.reverse('order-detail', kwargs={'pk': order_id})
          return HttpResponseRedirect(url)

        return super(paypalrestCreate, self).dispatch(request, *args, **kwargs)	

    def form_valid(self, form):
        import httplib2
        h = httplib2.Http()
        if 1 == 1:		#toggle, to skip or not -- temporarily applied!
          try:
            response, content = h.request("https://api.sandbox.paypal.com")   #for live, https://api.paypal.com
            if response.status==200:
                print ("PayPal sandbox Site is Up")
          except httplib2.ServerNotFoundError:
            print ("PayPal sandbox Site is Down")
            messages.error(self.request, "Internet Connection ERROR, PayPal sandbox can not be reached!")
            #redirect to the same page, because internet connection error
            return self.render_to_response(self.get_context_data(form=form)) 

        #Paypal integration started
        pmonth = (form.cleaned_data["expiration"]).month
        pyear = (form.cleaned_data["expiration"]).year
        order_id = self.kwargs['pk']
        order_items = OrderItem.objects.filter(order=order_id)

        items = []
        titems = 0
        for item in order_items:
          iprice = math.ceil((item.price / 12000)*100)/100
          items.append({
                "name": item.name,
                "sku": item.sku,
                "price": str("%0.2f" % iprice),		#Converted to USD
                "currency": "USD",
                "quantity": item.quantity 
                }
                )
          titems += math.ceil((item.price / 12000)*100)/100	# total items Converted to USD

        order = Order.objects.get(id=order_id)
        tamount = str("%0.2f" % titems)			#total amount

        print (items)
        print ("Total amount: "+ str(tamount))


        #print ("************* "+ str(pmonth) +" "+ str(pyear))			#Ok
        #print ("************"+ str(form.cleaned_data["amount"]))		#Ok
        #Lesson learned, decimal field must converted to string so it can be serialized by Json
        #Leasson leaned, total amount must match with sum of all items value * quantity! 

        #**start debug; following lines activated for debug only
        #order.status = 3           #3, payment received	#temp
        #order.payment_log = [{ 'payment log' }]		#temp
        #order.save()						#temp
        #messages.success(self.request, '**Thank you, Payment created for order number: '+ str(order.id) +', with amount of : USD'+ str(tamount))
        #return super(paypalrestCreate, self).form_valid(form)	#temp
        #send error message (django error tags; messages.success - messages.warning -
        #					messages.info - messages.error.
        #Bootstrap error tags; danger - success - warning - info. 
        #messages.danger(self.request, 'Danger!')   #while bootstrap have danger tag, django does not have it
        ##messages.error(self.request, 'Error!')    #Bootstrap does not known error tag, tricked to use danger tag instead in template	#Works!
        #messages.info(self.request, 'INFO!')	         			#Works!
        ##return self.render_to_response(self.get_context_data(form=form))       #Callback consist error(s)  #Temp
        #**end debug

        import paypalrestsdk
        import logging

        logging.basicConfig(level=logging.INFO)

        paypalrestsdk.configure({
          "mode": "sandbox", # sandbox or live
          "client_id": "clientId",
          "client_secret": "secret" })

        payment = paypalrestsdk.Payment({
          "intent": "sale",
          "payer": {
            "payment_method": "credit_card",			
            "funding_instruments": [{
              "credit_card": {
                "type": "visa",
                "number": form.cleaned_data["number"],
                "expire_month": pmonth,
                "expire_year": pyear,
                "cvv2": form.cleaned_data["ccv_number"],
                "first_name": form.cleaned_data["holderfname"],
                "last_name": form.cleaned_data["holderlname"] }}]},
          "transactions": [{
            "item_list": {
              "items": items },
            "amount": {
              "total": tamount,			
              "currency": "USD" },
            "description": "This is the payment transaction description." }]})

        if payment.create():
          print ("***OK, Payment created. Order total: USD "+ str(tamount) +" , for User:"+ str(form.cleaned_data["holderfname"]))
          #print (payment)		#Works beautifully!, temporarily disabled
          order.status = 3           		#update order status to 3, payment received
          order.payment_log = [payment]		#save payment callback dict in, order.paymentlog probably?
          order.save()
          messages.success(self.request, '**Thank you, Payment created for order number: '+ str(order.id) +', with amount of : USD'+ str(tamount))
          #send email to client and padangcuisine, later!
        else:		#if there's an error processing on PayPal side
          print(payment.error)
          #send error message
          #messages.error(self.request, "Payment ERROR: "+ str(payment.error))	#Works-Works-Works!
          messages.error(self.request, "Payment ERROR: "+ str([payment.error][0]['details'][0]['issue']))
          #redirect to the same page, because callback contains error(s)
          return self.render_to_response(self.get_context_data(form=form)) 

        return super(paypalrestCreate, self).form_valid(form)	#valid form processed successfully
