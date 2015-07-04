from django.db import models
from django import forms
#from django.contrib.auth.models import User
import decimal
from myauth.models import MyUser
from django.utils.text import slugify
import json

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text="Unique value for product page URL, created from name.")
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ['-created_at']
      verbose_name_plural = 'Categories'

    def __str__(self):
      return self.name

    @models.permalink
    def get_absolute_url(self):
      return ('catalog_category', (), { 'category_slug': self.slug })





class Product(models.Model):
    imgfile = models.ImageField("Image File", upload_to="products/main")
    imgthumb = models.ImageField("Image Thumbnail", upload_to="products/thumbnails",blank=True,null=True)
    #imgthumb = models.CharField("Image Thumbnail", max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    clientImgAttrs = models.CharField(max_length=255)

    class Meta:
      ordering = ['-created_at']

    def __str__(self):
      return self.name

    @models.permalink
    def get_absolute_url(self):
      return ('catalog_product', (), { 'product_slug': self.slug })


    def sale_price(self):
      if self.old_price > self.price:
        return self.price
      else:
        return None

    __original_imgfile = None
    __original_name = None
    
    def __init__(self, *args, **kwargs):
      super(Product, self).__init__(*args, **kwargs)
      self.__original_imgfile = self.imgfile
      self.__original_name = self.name



###new!
    def create_thumbnail(self):
        if not self.imgfile:
          return

        from PIL import ImageOps 
        from PIL import Image
        from django.core.files.uploadedfile import SimpleUploadedFile
        import io
        import os

        DJANGO_TYPE = self.imgfile.file.content_type
        if DJANGO_TYPE == 'image/jpeg':
          PIL_TYPE = 'jpeg'
          FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
          PIL_TYPE = 'png'
          FILE_EXTENSION = 'png'

        self.imgthumb.save('%s_thumbnail.%s'%(os.path.splitext(self.imgfile.name)[0],FILE_EXTENSION), self.imgfile, save=False)

        jsonlist = json.loads(self.clientImgAttrs)
        size =  int(jsonlist['imgw']) * int(jsonlist['imgh'])	#Works!
        img_w = int(jsonlist['imgw'])
        img_h = int(jsonlist['imgh'])
        crop_w = int(jsonlist['w'])
        crop_h = int(jsonlist['h'])
        cropbox = (int(jsonlist['x1']), int(jsonlist['y1']), int(jsonlist['x2']), int(jsonlist['y2']))
        

        thumbdir, thumbname = os.path.split(self.imgthumb.path)

        #Resize thumbdb to img_w and img_h		#Works Good
        imgrc = Image.open(io.BytesIO(self.imgthumb.read()))
        if imgrc.mode != 'RGB':
            imgrc = imgrc.convert('RGB')

        imgrc = imgrc.resize((img_w,img_h), Image.ANTIALIAS)
        #imgrc.save(thumbdir +'/'+ thumbname, 'JPEG', quality=75)

        #Now crop thumbdb to appropriate user area of choice	
        imgcrop = imgrc.crop(cropbox)
        #imgcrop.save(thumbdir +'/'+ thumbname, 'JPEG', quality=75)

        #Last step, resize to 140, 160
        imgfin = imgcrop.resize((140, 160), Image.ANTIALIAS)
        imgfin.save(thumbdir +'/'+ thumbname, 'JPEG', quality=75)

    def save(self):
        if self.name != self.__original_name:
           self.slug = slugify(self.name)

	# create a thumbnail, Works!
        if self.imgfile != self.__original_imgfile:
           self.create_thumbnail()

        #self.create_thumbnail()
        super(Product, self).save()

###/new

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey('Product', unique=False)
    imgthumb = models.CharField("Image Thumbnail", max_length=100, blank=True, null=True)


    class Meta:
      db_table = 'shop_cartitem'
      ordering = ['date_added']

    @property
    def total(self):
      return self.quantity * self.product.price

    @property
    def name(self):
      return self.product.name

    @property
    def slug(self):
      return self.product.slug

    @property
    def price(self):
      return self.product.price

    def get_absolute_url(self):
      return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
      self.quantity = self.quantity + int(quantity)
      self.save()



#New Entry for Checkout purpose

class BaseOrderInfo(models.Model):
    """ base class for storing customer order information """
    class Meta:
        abstract = True

        
    #contact info
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    
    #shipping information
    shipping_name = models.CharField(max_length=50)
    shipping_address_1 = models.CharField(max_length=50)
    shipping_address_2 = models.CharField(max_length=50, blank=True)
    shipping_city = models.CharField(max_length=50)
    shipping_state = models.CharField(max_length=2)
    shipping_country = models.CharField(max_length=50)
    shipping_zip = models.CharField(max_length=10)
    
    #billing information
    billing_name = models.CharField(max_length=50, default='dummy')
    billing_address_1 = models.CharField(max_length=50, default='dummy')
    billing_address_2 = models.CharField(max_length=50, blank=True)
    billing_city = models.CharField(max_length=50, default='dummy')
    billing_state = models.CharField(max_length=2, default='NY')
    billing_country = models.CharField(max_length=50, default='dummy')
    billing_zip = models.CharField(max_length=10, default='dummy')

    #additional_instructions
    additional_instructions = models.TextField(("Additional instructions"),
                                               blank=True)


class Order(BaseOrderInfo):
    """ model class for storing a customer order instance """
    # each individual status
    SUBMITTED = 1
    AWAITING_PAYMENT = 2
    PAYMENT_RECEIVED = 3
    PROCESSED = 4
    SHIPPED = 5
    CLOSED = 6
    CANCELLED = 0
    # set of possible order statuses
    ORDER_STATUSES = ((SUBMITTED,'Submitted'),
                      (AWAITING_PAYMENT,'Awaiting Payment'),
                      (PAYMENT_RECEIVED,'Payment Received'),
                      (PROCESSED,'Processed'),
                      (SHIPPED,'Shipped'),
                      (CLOSED,'Closed'),
                      (CANCELLED,'Cancelled'),)
    #order info

    status = models.IntegerField(choices=ORDER_STATUSES, default=AWAITING_PAYMENT)
    #ip_address = models.IPAddressField(default='127.0.0.1')  #deprecated in Dajngo1.8  
    ip_address = models.GenericIPAddressField(default='127.0.0.1')
    user = models.ForeignKey(MyUser, null=True)
    transaction_id = models.CharField(max_length=20)
    payment_log = models.CharField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
      ordering = ['-created_at']
    
    def __str__(self):
        return 'Order #' + str(self.id)
    
    @property
    def total(self):
        total = decimal.Decimal('0.00')
        order_items = OrderItem.objects.filter(order=self)
        for item in order_items:
            total += item.total
        return total

    
    @models.permalink
    def get_absolute_url(self):
        return ('order_details', (), { 'order_id': self.id })

    def details_as_dict(self):
        """
        Returns the billing_detail_* and shipping_detail_* fields
        as two name/value pairs of fields in a dict for each type.
        Used in template contexts for rendering each type as groups
        of names/values.
        """
        context = {}
        for fieldset in ("billing_detail", "shipping_detail"):
            fields = [(f.verbose_name, getattr(self, f.name)) for f in
                self._meta.fields if f.name.startswith(fieldset)]
            context["order_%s_fields" % fieldset] = fields
        return context


    
class OrderItem(models.Model):
    session_id = models.CharField(max_length=50)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    order = models.ForeignKey(Order)
    
    @property
    def total(self):
        return self.quantity * self.price
    
    @property
    def name(self):
        return self.product.name
    
    @property
    def sku(self):
        return self.product.sku
    
    def __str__(self):
        return self.product.name + ' (' + self.product.sku + ')'
    
    def get_absolute_url(self):
        return self.product.get_absolute_url()
    

