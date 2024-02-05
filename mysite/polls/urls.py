##mysite/mysite/polls/urls.py
##soubor jsem vytvorila ja nacita to co je ve views

##1] do souboru nahraju pohled na stranku
from django.urls import path

from . import views


app_name = "polls"


urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
]
