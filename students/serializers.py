from rest_framework import serializers
from .models import StudentProfile
from courses.models import Course
from courses.serializers import CourseSerializer


class StudentProfileSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=False, required=False)
    rfid_code = serializers.SerializerMethodField()
    last_scan = serializers.SerializerMethodField()
    total_registered_units = serializers.SerializerMethodField()

    class Meta:
        model = StudentProfile
        fields = "__all__"

    def get_rfid_code(self, obj):
        return obj.get_rfid_code()

    def get_last_scan(self, obj):
        return obj.get_last_scan()

    def get_total_registered_units(self, obj):
        return obj.get_total_registered_units()

    def create(self, validated_data):

        student = StudentProfile()
        student.surname = validated_data.get('surname', student.surname)
        student.first_name = validated_data.get('first_name', student.first_name)
        student.other_name = validated_data.get('other_name', student.other_name)

        student.email = validated_data.get('email', student.email)
        student.phone_number = validated_data.get('phone_number', student.phone_number)

        student.matric_number = validated_data.get('matric_number', student.matric_number)
        student.faculty = validated_data.get('faculty', student.faculty)
        student.department = validated_data.get('department', student.department)
        student.admission_session = validated_data.get('admission_session', student.admission_session)
        student.level = validated_data.get('level', student.level)

        student.gender = validated_data.get('gender', student.gender)
        student.date_of_birth = validated_data.get('date_of_birth', student.date_of_birth)
        student.nationality = validated_data.get('nationality', student.nationality)
        student.state_of_origin = validated_data.get('state_of_origin', student.state_of_origin)
        student.lga = validated_data.get('lga', student.lga)
        student.resident_address = validated_data.get('resident_address', student.resident_address)
        student.photo = validated_data.get('photo', student.photo)

        student.save()
        return student

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.other_name = validated_data.get('other_name', instance.other_name)

        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.matric_number = validated_data.get('matric_number', instance.matric_number)
        instance.faculty = validated_data.get('faculty', instance.faculty)
        instance.department = validated_data.get('department', instance.department)
        instance.admission_session = validated_data.get('admission_session', instance.admission_session)
        instance.level = validated_data.get('level', instance.level)

        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.state_of_origin = validated_data.get('state_of_origin', instance.state_of_origin)
        instance.lga = validated_data.get('lga', instance.lga)
        instance.resident_address = validated_data.get('resident_address', instance.resident_address)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.is_flaged = validated_data.get('is_flaged', instance.is_flaged)

        instance.save()
        return instance
