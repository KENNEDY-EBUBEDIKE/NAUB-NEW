from django.db import models
from django.urls import reverse


class Course(models.Model):
    course_code = models.CharField(unique=True, blank=False, null=True, max_length=255)
    course_title = models.CharField(unique=True, blank=False, null=True, max_length=255)
    course_faculty = models.CharField(blank=False, null=True, max_length=255)
    course_department = models.CharField(blank=False, null=True, max_length=255)
    credit_unit = models.IntegerField(blank=False, null=True)

    class Meta:
        ordering = ('course_code',)

    def __str__(self):
        return self.course_code

    #     return reverse("delete_course", kwargs={"course_id": self.pk})


class StudentProfile(models.Model):

    # Basic Info
    first_name = models.CharField(blank=False, max_length=50)
    surname = models.CharField(blank=False, max_length=50)
    other_name = models.CharField(blank=True, null=True, max_length=50)

    # Contact Info
    phone_number = models.BigIntegerField(unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, null=False)

    # Academic Info
    matric_number = models.CharField(unique=True, max_length=22)
    faculty = models.CharField(null=True, max_length=100)
    department = models.CharField(null=True, max_length=100)
    admission_session = models.CharField(null=True, max_length=9)
    level = models.TextField(null=True)

    # Bio Info
    gender = models.CharField(null=True, max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(null=True, max_length=10)
    state_of_origin = models.CharField(null=True, blank=True, max_length=20)
    lga = models.CharField(null=True, max_length=50, blank=True)
    resident_address = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='image/', null=True, blank=True)

    is_flaged = models.CharField(null=True, max_length=200, default=None)
    is_active = models.BooleanField(default=True)

    courses = models.ManyToManyField('course', related_name='StudentProfile', blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('matric_number',)

    def __str__(self):
        return self.matric_number

    # def get_student_profile_url(self):
    #     return reverse("student_full_profile", kwargs={"student_id": self.pk})
    #
    # def get_student_profile_update_url(self):
    #     return reverse("student_profile_update", kwargs={"student_id": self.pk})
    #
    # def get_student_profile_deactivate_url(self):
    #     return reverse("student_profile_deactivate", kwargs={"student_id": self.pk})
    #
    # def get_flag_student_url(self):
    #     return reverse("flag_student", kwargs={"student_id": self.pk})


class ScanRecords(models.Model):
    student = models.ForeignKey('StudentProfile', on_delete=models.CASCADE, null=True, related_name='scan_records')
    scan_time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(null=True, max_length=50, blank=True, default='T.Y Buratai Gate')

    class Meta:
        ordering = ('scan_time',)

    def __str__(self):
        return self.student.matric_number
