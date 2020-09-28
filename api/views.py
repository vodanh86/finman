# api/views.py
from rest_framework import viewsets, generics
from .models import Branch, Staff, Customer, Collateral, CollateralType, Limit
from .serializers import (
    BranchSerializer, StaffSerializer, CustomerSerializer,
    CollateralTypeSerializer, CollateralSerializer,
    LimitSerializer, InterestTypeSerializer, LoanSerializer
)

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CollateralTypeViewSet(viewsets.ModelViewSet):
    queryset = CollateralType.objects.all()
    serializer_class = CollateralTypeSerializer

class CollateralViewSet(viewsets.ModelViewSet):
    queryset = Collateral.objects.all()
    serializer_class = CollateralSerializer

class LimitViewSet(viewsets.ModelViewSet):
    queryset = Limit.objects.all()
    serializer_class = LimitSerializer
