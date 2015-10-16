from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.StoryListView.as_view(), name='list'),
    url(r'^create/', views.StoryCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)$', views.StoryUpdateView.as_view(), name='edit'),
    url(
        r'^delete/(?P<pk>\d+)$',
        views.StoryDeleteView.as_view(),
        name='delete'
    ),
    url(
        r'^category/([\w-]+)/$',
        views.StoryCategoryListView.as_view(),
        name='category'
    ),
    url(
        r'^explore/$',
        views.ExploreView.as_view(),
        name='explore'
    ),
    url(
        r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/$',
        views.StoryDetailView.as_view(),
        name='detail'
    ),
]
