from rest_framework import serializers
from .models import (
    Company, Branch, Staff, Customer, 
    Collateral, CollateralType, 
    Limit, InterestType, Loan
)
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = Company

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = Branch

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Staff

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Customer

class CollateralTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CollateralType

class CollateralSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Collateral        

class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Limit

class InterestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = InterestType        

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Loan
