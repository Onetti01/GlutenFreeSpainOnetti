from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions
from .models import Users
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt


def set_login_cookie(response, user):
    response.set_cookie('user_id', user.id)
    response.set_cookie('name', user.name)
    response.set_cookie('email', user.email)


class ListUsersView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Users.objects.all().exists():
            users = Users.objects.all()
            result = []
            for user in users:
                item = {}
                item['id'] = user.id
                item['name'] = user.name
                item['last_name'] = user.last_name
                item['email'] = user.email
                item['password'] = user.password
                item['birth_date'] = user.birth_date
                result.append(item)
            return JsonResponse({'users': result}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'No users found'}, status=status.HTTP_404_NOT_FOUND)


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'name': user.name,
                'last_name': user.last_name,
                'email': user.email,
                'password': user.password,
                'birth_date': user.birth_date
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"errors": serializer.errors}, status=status.HTTP_404_NOT_FOUND)


class CustomLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        try:
            user = Users.objects.get(email=email)
            if user.check_password(password):
                response = JsonResponse(
                    {'message': 'Login successful'}, status=status.HTTP_200_OK)
                # Guarda las cookies de inicio de sesión
                set_login_cookie(response, user)
                return response
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Users.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class CheckAuthenticationView(APIView):
    def get(self, request, format=None):
        if 'user_id' in request.COOKIES and 'username' in request.COOKIES:
            user_id = request.COOKIES['user_id']
            username = request.COOKIES['username']
            # Realiza cualquier verificación adicional que necesites aquí
            user_data = {
                'user_id': user_id,
                'username': username,
            }
            return JsonResponse({'is_authenticated': True, 'user': user_data})
        else:
            return JsonResponse({'is_authenticated': False})
