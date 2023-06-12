from rest_framework import serializers
from .models import *

# creating serializer for model 
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
