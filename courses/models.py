from django.db import models


class Course(models.Model):
    course_code = models.CharField(unique=True, blank=False, null=True, max_length=255)
    course_title = models.CharField(unique=True, blank=False, null=True, max_length=255)
    course_faculty = models.CharField(blank=False, null=True, max_length=255)
    course_department = models.CharField(blank=False, null=True, max_length=255)
    credit_unit = models.IntegerField(blank=False, null=True)
    course_type = models.CharField(blank=False, null=True, max_length=255)

    class Meta:
        ordering = ('course_code',)

    def __str__(self):
        return self.course_code

    # def get_delete_course_url(self):
    #     return reverse("delete_course", kwargs={"course_id": self.pk})
