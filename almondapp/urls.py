from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.time_logs, name='time_logs'),
]
