from django.urls import path
from . import views

app_name = 'pbm'

urlpatterns = [
    path('', views.index, name='index'),
    path('pbm', views.pbmquestions, name='pbmquestions'),
    path('pbm/consent', views.consent, name='pbmconsent')
]
