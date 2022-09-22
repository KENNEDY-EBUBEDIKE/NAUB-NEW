import time
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from NAUB_RFID import rfid_code_utilities
from students.serializers import StudentProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def security_scan(request):
    owner = rfid_code_utilities.check_owner(rfid_code=request.data['rfid_code'])
    if owner and not owner.is_staff:
        ser_student = StudentProfileSerializer(owner)
        time.sleep(1)
        return Response(
            data={
                "success": True,
                'student': ser_student.data,
            },
            status=status.HTTP_200_OK)

    elif owner and owner.is_staff:
        return Response(
            data={
                "success": True,
            },
            status=status.HTTP_200_OK)
    else:
        return Response(
            data={
                "success": False,
                "message": "Card Does Not Exist"
            },
            status=status.HTTP_200_OK)
