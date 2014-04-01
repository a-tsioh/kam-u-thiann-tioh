from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from core import views

urlpatterns = patterns('',
  url(r'^$', views.IndexView.as_view()),
  url(r'^(?P<id>\d+)/$', views.IndexView.as_view()),
  url(r'^json$', views.json_api, name='json'),
  url(r'^json/(?P<id>\d+)/$', views.json_api, name='json'),
) 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
