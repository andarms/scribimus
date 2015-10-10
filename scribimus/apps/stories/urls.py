from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.StoryListView.as_view(), name='list'),
    url(r'^create/', views.StoryCreateView.as_view(), name='create'),
]
