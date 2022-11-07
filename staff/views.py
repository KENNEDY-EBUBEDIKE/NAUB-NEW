import time
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import StaffProfile
from .serializers import StaffProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from NAUB_RFID import rfid_code_utilities


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def staff_database(request):
    time.sleep(1)
    all_staff = StaffProfile.objects.all()
    ser_staff = StaffProfile(all_staff, many=True)
    return Response({
        'success': True,
        'students': ser_staff.data
    })
