from django.urls import path
from django.conf import settings
from .views import courses_database, add_course, get_course

urlpatterns = [
    path('courses-database/', courses_database, name='courses_database'),
    path('add-course/', add_course, name='add_course'),
    path('get-course/<int:course_id>/', get_course, name='get_course'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
