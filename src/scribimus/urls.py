from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^members/', include('apps.members.urls', namespace='members')),
    url(r'^stories/', include('apps.stories.urls', namespace='stories')),
    url(r'^login/$', 'apps.members.views.login_view', name='login'),
    url(r'^logout/$', 'apps.members.views.logout_view', name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
