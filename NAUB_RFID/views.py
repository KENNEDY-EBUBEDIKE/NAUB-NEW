from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_faculties(request):
    return Response({'success': True, 'faculties': [
        'ARTS, MANAGEMENT AND SOCIAL SCIENCE',
        'ENGINEERING AND TECHNOLOGY',
        'COMPUTING',
        'NATURAL AND APPLIED SCIENCE',
        'ENVIRONMENTAL SCIENCE'
    ]})
