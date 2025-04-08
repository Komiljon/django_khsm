from rest_framework import serializers
from .models import TrainApp, TrainAppCategory

class TrainAppSerializer(serializers.ModelSerializer):
    cat = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = TrainApp
        fields = ('__all__')

        
class TrainAppCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainApp
        fields = ('__all__')
        

class TrainAppCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainAppCategory
        fields = ('__all__')


        