from django.urls import path
from django.conf import settings
from .views import students_database, \
    register_student, student_profile, \
    edit_student_profile, update_rfid_code, register_course

urlpatterns = [
    path('students-database/', students_database, name='students_database'),
    path('student-profile/<int:pk>/', student_profile, name='student_profile'),
    path('register-student/', register_student, name='register_student'),
    path('update-rfid-code/', update_rfid_code, name='update_rfid_code'),
    path('edit-student-profile/', edit_student_profile, name='edit_student_profile'),
    path('register-course/', register_course, name='register_course'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
