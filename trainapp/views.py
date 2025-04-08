from rest_framework import viewsets
from trainapp.serializers import TrainAppSerializer, TrainAppCrudSerializer, TrainAppCatSerializer, UserSerializer
from .models import TrainApp, TrainAppCategory
 
class TrainAppViewSet(viewsets.ModelViewSet):
    queryset = TrainApp.objects.all()
    serializer_class = TrainAppSerializer  

    
class TrainAppCrudViewSet(viewsets.ModelViewSet):
    queryset = TrainApp.objects.all()
    serializer_class = TrainAppCrudSerializer
    

class TrainAppCatViewSet(viewsets.ModelViewSet):
    queryset = TrainAppCategory.objects.all()
    serializer_class = TrainAppCatSerializer