from django.urls import path
from django.conf import settings
from .views import staff_database

urlpatterns = [
    path('staff-database/', staff_database, name='staff_database'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
