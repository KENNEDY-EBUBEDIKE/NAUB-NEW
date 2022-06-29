import time
from .models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import MyAuthTokenSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# from rest_framework import status


@api_view(["POST"])
# @permission_classes(IsAuthenticated)
def login(request):
    time.sleep(1)
    if request.method == "POST":
        serializer = MyAuthTokenSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user)
            return Response({
                'success': True,
                'token': token.key,
                'user': user_serializer.data
            })
        else:
            return Response({
                'success': False,
                'error': serializer.errors
            })


@api_view(["GET"])
def logout(request):
    try:
        request.user.auth_token.delete()
        return Response({'success': True})
    except Exception as e:
        print(e)
        return Response({'success': False})


@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def users(request):
    users = User.objects.all()
    user_serializer = UserSerializer(users, many=True)
    return Response({
        'success': True,
        'user': user_serializer.data
    })


@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def register(request):
    if request.method == "POST":
        try:
            print(request.data)
        except Exception as e:
            print(e)
        return Response({
            'success': True,
        })
