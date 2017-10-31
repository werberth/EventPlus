from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^events/', include('eventplus.events.urls', namespace='events')),
    url(r'^talks/', include('eventplus.talks.urls', namespace='talks')),
    url(
        r'^accounts/',
        include(
            'eventplus.accounts.urls',
            namespace='accounts'
        )
    )
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
