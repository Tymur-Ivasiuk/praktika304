from django.conf.urls.static import static
from django.urls import path

from praktika import settings
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:section_slug>', CategoryView.as_view(), name='category')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
