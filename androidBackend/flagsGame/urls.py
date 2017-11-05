from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^flagsGame', views.allFlags, name='login')
]

