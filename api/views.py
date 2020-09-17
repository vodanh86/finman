# api/views.py
from rest_framework import viewsets
from .models import Store, Staff
from .serializers import StoreSerializer, StaffSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer