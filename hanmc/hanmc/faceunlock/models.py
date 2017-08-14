from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    def __unicode__(self):  # __str__ on Python 3
        return self.account
    account = models.CharField(max_length=20, primary_key=True)
    nickname = models.CharField(max_length=30)
    password_md5 = models.CharField(max_length=50)
    email = models.EmailField()
    has_faceset = models.BooleanField(default=False)
    modify_time = models.DateTimeField(auto_now=True)