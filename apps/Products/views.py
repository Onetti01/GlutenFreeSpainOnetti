from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions
from .models import Products


class ListProductsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Products.objects.all().exists():
            users = Products.objects.all()
            result = []
            for user in users:
                item = {}
                item['id'] = user.id
                item['name'] = user.name
                item['description'] = user.description
                item['price'] = user.price
                item['is_vegetarian'] = user.is_vegetarian
                item['category'] = user.category
                item['image'] = user.image

                result.append(item)

            return JsonResponse({'Products': result}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'No Products found'}, status=status.HTTP_404_NOT_FOUND)
