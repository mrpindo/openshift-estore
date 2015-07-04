from django import forms
from tokoku.models import *

class ContactForm(forms.Form):
    name = forms.CharField()
    senderemail = forms.EmailField(label='e-mail address')
    message_description = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False, label='cc to me')

    def __init__(self, *args, **kwargs):
      super(ContactForm, self).__init__(*args, **kwargs)
      self.fields['message_description'].widget.attrs = {'style': 'width:400px'}


class addArticleForm(forms.ModelForm):
    class Meta:
      model = Article
      #fields = ('title','content','user',)
      fields = ('title','content',)
      #widgets = {
      #    'user': forms.HiddenInput(),
      #}
    def __init__(self, *args, **kwargs):
        super(addArticleForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['cols'] = 80
