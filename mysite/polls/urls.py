##mysite/mysite/polls/urls.py
##soubor jsem vytvorila ja nacita to co je ve views

##1] do souboru nahraju pohled na stranku
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
]
