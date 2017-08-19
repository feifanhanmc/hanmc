# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .models import User
from .forms import LoginByPwdForm, RegisterForm 
from twisted.python.formmethod import Password
from django.views.decorators.csrf import csrf_exempt
import facepp

def index(request):
    context = {}
    try:
        account = request.session.get('account')
        u = User.objects.get(pk=account)
    except:
        pass
    else:
        context['account'] = account
        context['nickname'] = u.nickname
    return render(request, 'faceunlock/index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #获取绑定的数据，并存储到数据库
            cleaned_data = form.cleaned_data
            account = cleaned_data['account']
            nickname = cleaned_data['nickname']
            u = User.objects.create(pk=account)
            u.nickname = nickname
            u.password_md5 = cleaned_data['password_md5']
            u.email = cleaned_data['email']
            u.save()
            #设置session
            request.session['account'] = account
            request.session['nickname'] = nickname

            return HttpResponseRedirect(reverse('faceunlock:index'))
    else:
        form = RegisterForm()
    return render(request, 'faceunlock/register.html', {'form':form})

def login_by_face(request):
    context = {}
    request.session['account'] = 'test1'
    return render(request, 'faceunlock/login_by_face.html', context)

def login_by_pwd(request):
    if request.method == 'POST':
        form = LoginByPwdForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            request.session['account'] = account
            request.session['nickname'] = get_object_or_404(User, pk=account).nickname
            
            return HttpResponseRedirect(reverse('faceunlock:index'))
    else:
        form = LoginByPwdForm()
        return render(request, 'faceunlock/login_by_pwd.html', {'form':form})

def logout(request):
    try:
        del request.session['account']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('faceunlock:index'))

@csrf_exempt
def add_faceset(request):
    if request.method == 'POST':
        image_base64 = request.POST.get('dataUrl')[22:]
        outer_id = request.session['account']
        #upload image(image_base64) to facepp 
        api = facepp.API(key='FR2qXQzfPwSzjZNC1KSdQBiJD8h_sVIx', secret='0M7jG1b4nxdp6eBH8nnirkcefUWD91C-')
        api.faceset.create(outer_id=outer_id)
        res = api.detect(image_base64=image_base64)
        api.faceset.addface(outer_id=outer_id, face_tokens=res["faces"][0]["face_token"])
        #设置session    @2017-8-19 00:14:28目前设置的这个session好像并没有用
        request.session['has_faceset'] = True
        #下面这个其实并没有发挥作用，可能是什么异步的原因，log显示这条虽然执行了，但是页面当时并没有跳转
        return HttpResponseRedirect(reverse('faceunlock:index'))
        
    return render(request, 'faceunlock/add_faceset.html')
