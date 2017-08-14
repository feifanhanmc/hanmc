from django.conf.urls import url
from django.contrib.auth.views import (login, logout, password_change,
                                       password_change_done, password_reset,
                                       password_reset_complete,
                                       password_reset_confirm,
                                       password_reset_done)

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
