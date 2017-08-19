from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^login_by_face', views.login_by_face, name='login_by_face'),
    url(r'^login_by_pwd', views.login_by_pwd, name='login_by_pwd'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^add_faceset', views.add_faceset, name='add_faceset'),
]