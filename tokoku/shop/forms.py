from django import forms
from shop.models import *
import re


class ProductAdminForm(forms.ModelForm):
    class Meta:
      model = Product
      fields = ('imgfile', 'imgthumb', 'name', 'slug',)

    def clean_price(self):
      if self.cleaned_data['price'] <= 0:
        raise forms.ValidationError('Price must be greater than zero.')
      return self.cleaned_data['price']

class updateItemCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity', 'maxlength':'5'}), error_messages={'invalid':'Please enter a valid quantity.'}, min_value=1)

    #product_slug = forms.CharField(widget=forms.HiddenInput())

    # override the default __init__ so we can set the request
    #def __init__(self, request=None, *args, **kwargs):
    #  self.request = request
    #  super(updateItemCartForm, self).__init__(*args, **kwargs)

    # custom validation to check for cookies
    def clean(self):
      if self.request:
        if not self.request.session.test_cookie_worked():
          raise forms.ValidationError("Cookies must be enabled.")
      return self.cleaned_data



class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity', 'maxlength':'5'}), error_messages={'invalid':'Please enter a valid quantity.'}, min_value=1)
    product_slug = forms.CharField(widget=forms.HiddenInput())

    # override the default __init__ so we can set the request
    def __init__(self, request=None, *args, **kwargs):
      self.request = request
      super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    # custom validation to check for cookies
    def clean(self):
      if self.request:
        if not self.request.session.test_cookie_worked():
          raise forms.ValidationError("Cookies must be enabled.")
      return self.cleaned_data


#New entry for checkout
def strip_non_numbers(data):
    """ gets rid of all non-number characters """
    non_numbers = re.compile('\D')
    return non_numbers.sub('', data)


class OrderForm(forms.ModelForm):
    """ checkout form class to collect user billing and shipping information for placing an order """
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # override default attributes
        for field in self.fields:
            self.fields[field].widget.attrs['size'] = '30'
            
        self.fields['shipping_state'].widget.attrs['size'] = '3'
        self.fields['shipping_zip'].widget.attrs['size'] = '6'

        #self.fields['billing_state'].widget.attrs['size'] = '3'

                        
    class Meta:
        model = Order
        exclude = ('status','ip_address','user','transaction_id','billing_name','billing_address_1',
'billing_address_2','billing_city','billing_state','billing_country','billing_zip','payment_log',)
        #widgets = {
        #    'billing_state': forms.HiddenInput(),
        #}
           
        
    #def clean_phone(self):
    #    phone = self.cleaned_data['phone']
    #    stripped_phone = strip_non_numbers(phone)
    #    if len(stripped_phone) < 10:
    #        raise forms.ValidationError('Enter a valid phone number with area code.(e.g. 555-555-5555)')
    #    return self.cleaned_data['phone']


class CheckoutForm(forms.ModelForm):
    #same_billing_shipping = forms.BooleanField(required=False, initial=True,
    #    label=("My billing details are the same as my shipping details"))
    same_billing_shipping = forms.BooleanField(required=False, initial=True,
        label=("Detil pembayaran sama dengan detil pengiriman"))

    """ checkout form class to collect user billing and shipping information for placing an order """
    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        # override default attributes
        for field in self.fields:
            self.fields[field].widget.attrs['size'] = '30'
            
        self.fields['shipping_state'].widget.attrs['size'] = '3'
        self.fields['shipping_state'].widget.attrs['size'] = '3'
        self.fields['shipping_zip'].widget.attrs['size'] = '6'
        
        self.fields['billing_state'].widget.attrs['size'] = '3'
        self.fields['billing_state'].widget.attrs['size'] = '3'
        self.fields['billing_zip'].widget.attrs['size'] = '6'

                
    class Meta:
        model = Order
        exclude = ('status','ip_address','user','transaction_id',)
           
        
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone) < 10:
            raise forms.ValidationError('Enter a valid phone number with area code.(e.g. 555-555-5555)')
        return self.cleaned_data['phone']


from django.forms.widgets import RadioSelect

class addProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = '__all__'	#Works!
        fields = ('imgfile', 'name', 'brand', 'sku', 'price', 'quantity', 'description', 'categories', 'clientImgAttrs',)
        widgets = {
            'clientImgAttrs': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
      super(addProductForm, self).__init__(*args, **kwargs)
      self.fields['description'].widget.attrs = {'style': 'width:100%'}



class updateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('imgfile', 'name', 'brand', 'sku', 'price', 'quantity', 'description', 'categories', 'clientImgAttrs',)
        widgets = {
            'clientImgAttrs': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
      super(updateProductForm, self).__init__(*args, **kwargs)
      self.fields['description'].widget.attrs = {'style': 'width:100%'}


class updateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('status', 'email', 'transaction_id',)


#PayPal Rest SDK Payment
class PayPalRestForm(forms.Form):
    name = forms.CharField()
    senderemail = forms.EmailField(label='e-mail address')
    message_description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
      super(PayPalRestForm, self).__init__(*args, **kwargs)

#===from https://djangosnippets.org/snippets/907/
from datetime import date, datetime
from calendar import monthrange

class CreditCardField(forms.IntegerField):
    #@staticmethod	#What is it for?
		
    def get_cc_type(number):
        return		#temporary
        """
        Gets credit card type given number. Based on values from Wikipedia page
        "Credit card number".
        http://en.wikipedia.org/w/index.php?title=Credit_card_number
        """
        number = str(number)
        #group checking by ascending length of number
        if len(number) == 13:
            if number[0] == "4":
                return "Visa"
        elif len(number) == 14:
            if number[:2] == "36":
                return "MasterCard"
        elif len(number) == 15:
            if number[:2] in ("34", "37"):
                return "American Express"
        elif len(number) == 16:
            if number[:4] == "6011":
                return "Discover"
            if number[:2] in ("51", "52", "53", "54", "55"):
                return "MasterCard"
            if number[0] == "4":
                return "Visa"
        return "Unknown"

    def clean(self, value):
        return super(CreditCardField, self).clean(value)		#Temporary
        """Check if given CC number is valid and one of the
           card types we accept"""
        if value and (len(value) < 13 or len(value) > 16):
            raise forms.ValidationError("Please enter in a valid "+\
                "credit card number.")
        elif self.get_cc_type(value) not in ("Visa", "MasterCard",
                                             "American Express"):
            raise forms.ValidationError("Please enter in a Visa, "+\
                "Master Card, or American Express credit card number.")
        return super(CreditCardField, self).clean(value)


class CCExpWidget(forms.MultiWidget):
    """ Widget containing two select boxes for selecting the month and year"""
    def decompress(self, value):
        return [value.month, value.year] if value else [None, None]

    def format_output(self, rendered_widgets):
        html = u' / '.join(rendered_widgets)
        return u'<span style="white-space: nowrap">%s</span>' % html


class CCExpField(forms.MultiValueField):
    EXP_MONTH = [(x, x) for x in range(1, 13)]
    EXP_YEAR = [(x, x) for x in range(date.today().year,
                                       date.today().year + 15)]
    default_error_messages = {
        'invalid_month': u'Enter a valid month.',
        'invalid_year': u'Enter a valid year.',
    }

    def __init__(self, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        fields = (
            forms.ChoiceField(choices=self.EXP_MONTH,
                error_messages={'invalid': errors['invalid_month']}),
            forms.ChoiceField(choices=self.EXP_YEAR,
                error_messages={'invalid': errors['invalid_year']}),
        )
        super(CCExpField, self).__init__(fields, *args, **kwargs)
        self.widget = CCExpWidget(widgets =
            [fields[0].widget, fields[1].widget])

    def clean(self, value):
        exp = super(CCExpField, self).clean(value)
        if date.today() > exp:
            raise forms.ValidationError(
            "The expiration date you entered is in the past.")
        return exp

    def compress(self, data_list):
        if data_list:
            if data_list[1] in forms.fields.EMPTY_VALUES:
                error = self.error_messages['invalid_year']
                raise forms.ValidationError(error)
            if data_list[0] in forms.fields.EMPTY_VALUES:
                error = self.error_messages['invalid_month']
                raise forms.ValidationError(error)
            year = int(data_list[1])
            month = int(data_list[0])
            # find last day of the month
            day = monthrange(year, month)[1]
            return date(year, month, day)
        return None


class PaymentForm(forms.Form):
    #number = CreditCardField(required = True, label = "Card Number", initial='4417119669820331')
    number = CreditCardField(required = True, label = "Card Number", initial='4417119669820331', widget = forms.TextInput(attrs={'readonly':'readonly'}))

    holderfname = forms.CharField(required = True, label = "Card Holder First Name",
        max_length = 60)
    holderlname = forms.CharField(required = True, label = "Card Holder Last Name",
        max_length = 60)

    expiration = CCExpField(required = True, label = "Expiration")
    ccv_number = forms.IntegerField(required = True, label = "CCV Number",
        max_value = 9999, widget = forms.TextInput(attrs={'size': '4'}))

    #amount = forms.DecimalField(required = True, decimal_places=2, label = "Amount due",
    #    max_value = 100, widget = forms.TextInput(attrs={'size': '6'}), initial='0.00')

    def __init__(self, *args, **kwargs):
        self.payment_data = kwargs.pop('payment_data', None)
        super(PaymentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned = super(PaymentForm, self).clean()
        if not self.errors:
            result = self.process_payment()
            if result and result[0] == 'Card declined':
                raise forms.ValidationError('Your credit card was declined.')
            elif result and result[0] == 'Processing error':
                raise forms.ValidationError(
                    'We encountered the following error while processing '+\
                    'your credit card: '+result[1])
        return cleaned

    def process_payment(self):
        if self.payment_data:
            # don't process payment if payment_data wasn't set
            datadict = self.cleaned_data
            datadict.update(self.payment_data)

    #        from virtualmerchant import VirtualMerchant
    #        vmerchant = VirtualMerchant(datadict)

    #        return vmerchant.process_virtualmerchant_payment()
            return
