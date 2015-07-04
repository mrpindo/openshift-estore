from django.db import models
from django import forms
#from django.contrib.auth.models import User
#import decimal
from myauth.models import MyUser
from django.utils.text import slugify
#import json



class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)	#max_length ignored for int in Django 1.8
    slug = models.SlugField(max_length=140)
    content = models.TextField()
    user = models.ForeignKey(MyUser)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ['-created_at']

    def __str__(self):
      return self.title

    @models.permalink
    def get_absolute_url(self):
      return ('article-detail', (), { 'slug': self.slug })

    __original_title = None
    def __init__(self, *args, **kwargs):
      super(Article, self).__init__(*args, **kwargs)
      self.__original_title = self.title

    def save(self):
        if self.title != self.__original_title:
           self.slug = slugify(self.title)
        super(Article, self).save()


