from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class StaffProfile(models.Model):
    # Basic Info
    first_name = models.CharField(blank=False, max_length=50, null=True)
    surname = models.CharField(blank=False, max_length=50, null=True)
    other_name = models.CharField(blank=True, null=True, max_length=50)

    # Contact Info
    phone_number = models.BigIntegerField(unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, null=False)

    # Academic Info
    staff_id = models.CharField(unique=True, max_length=22)
    unit = models.CharField(null=True, max_length=100)
    department = models.CharField(null=True, max_length=100)
    employment_date = models.DateField(auto_now_add=False)
    level = models.TextField(null=True)

    # Bio Info
    gender = models.CharField(null=True, max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(null=True, max_length=10, default="Nigerian")
    state_of_origin = models.CharField(null=True, blank=True, max_length=20)
    lga = models.CharField(null=True, max_length=50, blank=True)
    resident_address = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='image/', null=True, blank=True)

    is_flaged = models.CharField(null=True, max_length=200, default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    reg_date = models.DateTimeField(auto_now_add=True)

    rfid_code = GenericRelation('users.CodeBase', related_query_name='staff_profile')

    class Meta:
        ordering = ('staff_id',)

    def __str__(self):
        return self.staff_id

    def get_rfid_code(self):
        q = self.rfid_code.all()
        if q:
            return q[0].rfid_code
        else:
            return None

    def get_last_scan(self):
        q = self.rfid_code.all()
        if q:
            return q[0].last_scan
        else:
            return None
