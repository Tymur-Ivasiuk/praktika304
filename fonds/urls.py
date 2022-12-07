from django.conf.urls.static import static
from django.urls import path

from praktika import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('zsu/', zsu, name='zsu'),
    path('support/', support, name='support'),
    path('charity/', charity, name='charity'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
