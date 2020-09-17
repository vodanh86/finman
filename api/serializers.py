from rest_framework import serializers
from .models import Store, Staff


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "company", "store_name", "address")
        model = Store

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "full_name", "birth_day", "address")
        model = Staff