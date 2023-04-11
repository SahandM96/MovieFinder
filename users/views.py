from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import exceptions
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .authentication import generate_access_token, JWTAuthentication


@api_view(['POST'])
def register(request):
    md = request.data
    if md['password'] != md['password_confirm']:
        raise APIException('Password not equal')
    print(md)
    ser = UserSerializer(data=md)
    ser.is_valid(raise_exception=True)
    ser.save()
    return Response(ser.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()

    if user is None:
        raise exceptions.NotFound("user Not Found")

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Check user or password")

    data = {"message": "Wellcome", "data": user}

    response = Response()

    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'message': "You are logged in"
    }
    return response


class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({
            'data': serializer.data
        })


@api_view(['POST'])
def logout(request):
    response = Response()
    if request.COOKIES.get('jwt'):
        response.delete_cookie(key='jwt')
        response.data = {
            'message': 'logged out'
        }
        return response

    response.data = {
        'message': 'you are not logged in'
    }
    return response


@api_view(['GET'])
def users(request):
    all_users = UserSerializer(User.objects.all(), many=True)
    return Response(all_users.data)
