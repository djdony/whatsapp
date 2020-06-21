from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    path('', include('settings.urls')),
    #prefix_default_language= False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


