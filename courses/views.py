import time
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def courses_database(request):
    time.sleep(1)
    all_courses = Course.objects.all()
    serialized_courses = CourseSerializer(all_courses, many=True)
    return Response({
        'success': True,
        'courses': serialized_courses.data
    })


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def add_course(request):
    if request.method == "POST":
        time.sleep(1)
        course_serializer = CourseSerializer(data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response({
                'success': True,
                'message': "Course Added Successfully"
            })
        else:
            return Response({
                'success': False,
                'error': course_serializer.errors
            })


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def get_course(request, course_id):
    if request.method == "GET":
        course = Course.objects.get(id=course_id)
        serialized_course = CourseSerializer(course)
        return Response({
            'success': True,
            'course': serialized_course.data
        })
    elif request.method == "PATCH":
        course = Course.objects.get(id=course_id)
        course_serializer = CourseSerializer(instance=course, data=request.data, partial=True)
        if course_serializer.is_valid():
            course_serializer.save()
        return Response({
            'success': True,
            'message': "Course Updated Successfully"
        }, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        course = Course.objects.get(id=course_id)
        course.delete()
        return Response({
            'success': True,
            'message': "Course Deleted Successfully"
        })
