# -*- coding: utf-8 -*-
from django import forms
from .models import User
import random
import hashlib

class RegisterForm(forms.Form):
    class Meta:
        model = User
        
    random_nickname = u'用户' + str(random.randint(100000,999999))
    nickname = forms.CharField(initial=random_nickname)
    account = forms.CharField(max_length=20)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Again', widget=forms.PasswordInput)
    email = forms.EmailField()
        
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        account = cleaned_data.get('account')
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if User.objects.filter(pk=account).count() is not 0:
            raise forms.ValidationError('This account is already exist.')
        if password1 and password2:
            if not password1 == password2:
                raise forms.ValidationError('The two passwords entered are different.')
            else:
                del cleaned_data['password1']
                del cleaned_data['password2']
                cleaned_data['password_md5'] = hashlib.md5(password1).hexdigest()
        return cleaned_data
    
class LoginByPwdForm(forms.Form):
    class Meta:
        model = User
        
    account = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super(LoginByPwdForm, self).clean()
        account = cleaned_data.get("account")
        password = cleaned_data.get("password")
        if User.objects.filter(pk=account).count() is not 1:
            raise forms.ValidationError('Bad account.')
        if password:
            password_md5 = hashlib.md5(password).hexdigest()
            if password_md5 == User.objects.get(pk=account).password_md5:
                del cleaned_data['password']
                cleaned_data['password_md5'] = password_md5
            else:
                raise forms.ValidationError('Bad password.')
        return cleaned_data