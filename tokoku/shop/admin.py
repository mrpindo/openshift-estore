from django.contrib import admin
from django.db.models import ImageField
from shop.models import Product, Category, Order, OrderItem
from shop.forms import ProductAdminForm



class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    # sets values for how the admin site lists your products
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']

    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    #exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('name',)}

# registers your product model with the admin site
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    #exclude = ('created_at', 'updated_at',)

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)

###########


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__','created_at','status','transaction_id','user')
    list_filter = ('status','created_at')
    search_fields = ('email','shipping_name','billing_name','id','transaction_id')
    inlines = [OrderItemInline,]
    fieldsets = (
      ('Basics', {'fields': ('status','email','phone')}),
      ('Shipping', {'fields':('shipping_name','shipping_address_1',
      'shipping_address_2','shipping_city','shipping_state',
      'shipping_zip','shipping_country')}),
      ('Billing', {'fields':('billing_name','billing_address_1',
      'billing_address_2','billing_city','billing_state',
      'billing_zip','billing_country')})
      )
admin.site.register(Order, OrderAdmin)



