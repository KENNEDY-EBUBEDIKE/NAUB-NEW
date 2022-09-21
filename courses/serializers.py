from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):

        course = Course()

        course.course_code = validated_data.get('course_code', course.course_code)
        course.course_title = validated_data.get('course_title', course.course_title)
        course.course_faculty = validated_data.get('course_faculty', course.course_faculty)
        course.course_department = validated_data.get('course_department', course.course_department)
        course.credit_unit = validated_data.get('credit_unit', course.credit_unit)
        course.course_type = validated_data.get('course_type', course.course_type)

        course.save()
        return course

    def update(self, instance, validated_data):
        instance.course_code = validated_data.get('course_code', instance.course_code)
        instance.course_title = validated_data.get('course_title', instance.course_title)
        instance.course_faculty = validated_data.get('course_faculty', instance.course_faculty)
        instance.course_department = validated_data.get('course_department', instance.course_department)
        instance.credit_unit = validated_data.get('credit_unit', instance.credit_unit)
        instance.course_type = validated_data.get('course_type', instance.course_type)
        instance.save()
        return instance
