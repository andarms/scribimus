from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/', views.MemberCreateView.as_view(), name='create'),
    url(
        r'^(?P<slug>[\w.@+-]+)/',
        views.MemberDetailView.as_view(),
        name='detail'
    ),
]
