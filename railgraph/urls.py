from django.conf.urls import patterns, url

from railgraph import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
