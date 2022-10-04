from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'pbm'

urlpatterns = [
    path('', views.index, name='index'),
    path('pbm', views.pbmquestions, name='pbmquestions'),
    path('pbm/consent', views.consent, name='pbmconsent')
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
