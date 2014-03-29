from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^json', views.json_api, name='json'),
) 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
