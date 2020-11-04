# api/views.py
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from django.http import JsonResponse
from api.controllers.customerController import searchCustomer
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
    
    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request, *args, **kwargs):
        # custom code
        phoneNumber = request.GET.get("phoneNumber")
        customers = []
        if phoneNumber:
            customers = CustomerSerializer(searchCustomer(phoneNumber), many=True)
        return JsonResponse(customers.data, safe=False)

class CollateralTypeViewSet(viewsets.ModelViewSet):
    queryset = CollateralType.objects.all()
    serializer_class = CollateralTypeSerializer

class CollateralViewSet(viewsets.ModelViewSet):
    queryset = Collateral.objects.all()
    serializer_class = CollateralSerializer

class LimitViewSet(viewsets.ModelViewSet):
    queryset = Limit.objects.all()
    serializer_class = LimitSerializer
