from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from tokoku.forms import * 
from django.core import urlresolvers
from django.contrib import messages
from django.conf import settings

from tokoku.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse, reverse_lazy


class articleList(ListView):
    model = Article
    template_name = 'article/article_list.html'
    paginate_by = 10



class articleCreate(CreateView):
    model = Article
    form_class = addArticleForm
    template_name = 'article/article_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(articleCreate, self).form_valid(form)

    # where to put this email restrict part? 
    #'padangcuisine@gmail.com'.split('@')[0]
    #will return padangcuisine

class articleDetail(DetailView):
    model = Article
    template_name = 'article/article_detail.html'



class articleUpdate(UpdateView):
    model = Article
    form_class = addArticleForm
    template_name = 'article/article_form.html'


class articleDelete(DeleteView):
    model = Article
    template_name = 'article/article_confirm_delete.html'
    success_url = reverse_lazy('article-list')


def home(request, template_name="home.html"):
    page_title = 'Home'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def klinik5(request, template_name="3DWorks/klinik5.html"):
    page_title = 'Klinik 5'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def Rumah2Lantai(request, template_name="3DWorks/Rumah2Lantai.html"):
    page_title = 'Rumah 2 Lantai'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def horseinline(request, template_name="3DWorks/horseinline.html"):
    page_title = '3D Horse Inline'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def klinikinline(request, template_name="3DWorks/klinikinline.html"):
    page_title = '3D Klinik Inline'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))


def about(request, template_name="about.html"):
    page_title = 'Mengenai Website Ini'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def faq(request, template_name="faq.html"):
    page_title = 'Pertanyaan yang sering dilontarkan'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def shop_map(request, template_name="shopping_map.html"):
    page_title = 'Shop_map'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))


class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_thanks')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        subject = 'Pesan dari ~ ' + form.cleaned_data['name']
        message_description = form.cleaned_data['message_description']
        sender = form.cleaned_data['senderemail']
        cc_myself = form.cleaned_data['cc_myself']
        recipients = ['padangcuisine@gmail.com']
        if cc_myself:
            recipients.append(sender)
        message = message_description
        send_mail(subject, message, sender, recipients)

        return super(ContactView, self).form_valid(form)

def contact_thanks(request, template_name="contact_thanks.html"):
    page_title = 'Thank you'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))


'''to be deleted, replaced by class based view
#The following two line, to restrict view using @staff_member_required, work flawlessly!
#from django.contrib.admin.views.decorators import staff_member_required
#@staff_member_required
def Xcontact(request, template_name="contact_form.html"):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            subject = 'Pesan dari ~ ' + form.cleaned_data['name']
            message_description = form.cleaned_data['message_description']
            sender = form.cleaned_data['senderemail']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['padangcuisine@gmail.com']
            if cc_myself:
                recipients.append(sender)
            message = message_description
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/contact/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def contact_thanks(request, template_name="contact_thanks.html"):
    page_title = 'Thank you'
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))
'''

### Search facility
from django.shortcuts import render_to_response
from django.template import RequestContext
import re

from django.db.models import Q
#from repository.models import fileUpload
from shop.models import Product

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query




def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        terms = normalize_query(query_string)

        a_list = []
        n_list = []
        a_list.extend(terms)
        for a in a_list:
          n_list.extend(Product.objects.filter(name__icontains=a).values_list('id', flat=True))

        found_entries = Product.objects.filter(id__in=n_list).order_by('-id')

    return render_to_response('search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))

def Xsearch(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        #entry_query = get_query(query_string, ['title', 'body',])
        #entry_query = get_query(query_string, ['slug',])
        entry_query = get_query(query_string, ['name',])
        #entry_query = get_query(query_string, ['name__in',])	#should be name__in  but it doesnt work!
        
        found_entries = Product.objects.filter(entry_query).order_by('-id')


    return render_to_response('search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))


