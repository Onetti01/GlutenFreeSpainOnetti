from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions
from .models import Users
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login


@method_decorator(csrf_exempt, name='dispatch')
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
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'id': user.id,
                'name': user.name,
                'last_name': user.last_name,
                'email': user.email,
                'birth_date': user.birth_date
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"errors": serializer.errors}, status=status.HTTP_404_NOT_FOUND)


class CustomLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Users.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
