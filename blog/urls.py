from django.conf.urls import url
from . import views

urls_patterns = [
    url(r'^$', views.post_list, name='post_list'),

]
