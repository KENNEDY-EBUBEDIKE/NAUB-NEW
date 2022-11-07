import time
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import StudentProfile
from courses.models import Course
from .serializers import StudentProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from NAUB_RFID import rfid_code_utilities


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def students_database(request):
    time.sleep(1)
    all_students = StudentProfile.objects.all()
    ser_students = StudentProfileSerializer(all_students, many=True)
    return Response({
        'success': True,
        'students': ser_students.data
    })


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def student_profile(request, pk):
    time.sleep(1)
    student = StudentProfile.objects.get(id=pk)
    ser_student = StudentProfileSerializer(student)

    return Response({
        'success': True,
        'student': ser_student.data
    })


def dummy_function_based_view(request):
    pass


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def register_student(request):
    if request.method == "POST":
        time.sleep(1)
        student_serializer = StudentProfileSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({
                'success': True,
                'student': student_serializer.data
            })
        else:
            return Response({
                'success': False,
                'error': student_serializer.errors
            })


@api_view(['PUT', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def edit_student_profile(request):
    if request.method == 'PUT' or request.method == 'PATCH':
        if request.method == 'PUT':  # Complete Update of all fields
            student_serializer = StudentProfileSerializer(instance=request.user, data=request.data)
        elif request.method == 'PATCH':  # Partial Update of desired fields
            student = StudentProfile.objects.get(id=request.data['pk'])
            student_serializer = StudentProfileSerializer(instance=student, data=request.data, partial=True)
        else:
            student_serializer = StudentProfileSerializer()
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(
                data={
                    "success": True,
                    "message": "Updated Successfully"
                      },
                status=status.HTTP_200_OK)
        else:
            print(student_serializer.errors)
            return Response(
                data={"success": False,
                      "error": student_serializer.errors},
                status=status.HTTP_200_OK
            )


@api_view(['PATCH'])
@permission_classes((IsAuthenticated, ))
def update_rfid_code(request):
    if request.method == "PATCH":
        student = StudentProfile.objects.get(id=request.data['pk'])
        resp = rfid_code_utilities.update_rfid_code(student, request.data['rfid_code'])
        if resp["success"]:
            return Response(
                data={
                    "success": True,
                    "message": "Updated Successfully"
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    "success": False,
                    "message": f'This RFID Card belongs to {resp["owner"].surname} {resp["owner"].first_name}'
                },
                status=status.HTTP_200_OK
            )


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def register_course(request):
    if request.method == "POST":
        student = StudentProfile.objects.get(id=request.data['pk'])
        courses = request.data['courses'].split(',')
        if len(courses) >= 1:
            for c in courses:
                cc = Course.objects.get(course_code=c)
                student.courses.add(cc)
            student.save()
            return Response(
                data={
                    "success": True,
                    "message": "Registered Successfully"
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    "success": False,
                    "message": "Empty Selection"
                },
                status=status.HTTP_200_OK
            )


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def de_register_course(request):
    if request.method == "POST":
        student = StudentProfile.objects.get(id=request.data['pk'])
        course = Course.objects.get(course_code=request.data['course'])
        student.courses.remove(course)
        student.save()
        return Response(
            data={
                "success": True,
                "message": "Course De-Registered Successfully"
            },
            status=status.HTTP_200_OK
        )
