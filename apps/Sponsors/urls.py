from django.urls import path

from .views import *

urlpatterns =[
    path('list', ListSponsorsView.as_view())
]