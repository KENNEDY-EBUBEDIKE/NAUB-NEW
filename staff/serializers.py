from rest_framework import serializers
from .models import StaffProfile


class StaffProfileSerializer(serializers.ModelSerializer):
    rfid_code = serializers.SerializerMethodField()
    last_scan = serializers.SerializerMethodField()

    class Meta:
        model = StaffProfile
        fields = "__all__"

    def get_rfid_code(self, obj):
        return obj.get_rfid_code()

    def get_last_scan(self, obj):
        return obj.get_last_scan()

    def create(self, validated_data):
        staff = StaffProfile()
        staff.surname = validated_data.get('surname', staff.surname)
        staff.first_name = validated_data.get('first_name', staff.first_name)
        staff.other_name = validated_data.get('other_name', staff.other_name)

        staff.email = validated_data.get('email', staff.email)
        staff.phone_number = validated_data.get('phone_number', staff.phone_number)

        staff.staff_id = validated_data.get('staff_id', staff.staff_id)
        staff.unit = validated_data.get('unit', staff.unit)
        staff.department = validated_data.get('department', staff.department)
        staff.employment_date = validated_data.get('employment_date', staff.employment_date)
        staff.level = validated_data.get('level', staff.level)

        staff.gender = validated_data.get('gender', staff.gender)
        staff.date_of_birth = validated_data.get('date_of_birth', staff.date_of_birth)
        staff.nationality = validated_data.get('nationality', staff.nationality)
        staff.state_of_origin = validated_data.get('state_of_origin', staff.state_of_origin)
        staff.lga = validated_data.get('lga', staff.lga)
        staff.resident_address = validated_data.get('resident_address', staff.resident_address)
        staff.photo = validated_data.get('photo', staff.photo)

        staff.save()
        return staff
