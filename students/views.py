import time
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import StudentProfile
from .serializers import StudentProfileSerializer
from rest_framework.permissions import IsAuthenticated


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
# @permission_classes((IsAuthenticated, ))
def student_profile(request, pk):
    time.sleep(1)
    student = StudentProfile.objects.get(id=pk)
    ser_student = StudentProfileSerializer(student)
    return Response({
        'success': True,
        'student': ser_student.data
    })


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
