from django.urls import path

from .views import *

urlpatterns = [
    path('list', ListBillsView.as_view())]
