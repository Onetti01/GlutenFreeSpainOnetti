from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions
from .models import Sponsors


class ListSponsorsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Sponsors.objects.all().exists():
            users = Sponsors.objects.all()
            result = []
            for user in users:
                item = {}
                item['CIF'] = user.CIF
                item['name'] = user.name
                item['icon'] = user.icon
                item['email'] = user.email

                result.append(item)

            return JsonResponse({'Sponsors': result}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'No Sponsors found'}, status=status.HTTP_404_NOT_FOUND)
