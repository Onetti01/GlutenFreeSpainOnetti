from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions
from .models import Bills


class ListBillsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Bills.objects.all().exists():
            users = Bills.objects.all()
            result = []
            for user in users:
                item = {}
                item['id'] = user.id
                item['is_paid'] = user.is_paid
                item['CIF_sponsor'] = user.CIF_sponsor
                item['pdf'] = user.pdf
                item['suscription'] = user.suscription

                result.append(item)

            return JsonResponse({'Bills': result}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'No Bills found'}, status=status.HTTP_404_NOT_FOUND)
