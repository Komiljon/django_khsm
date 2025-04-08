from rest_framework import generics, viewsets
from trainapp.serializers import TrainAppSerializer, TrainAppCrudSerializer, TrainAppCatSerializer, UserSerializer
from .models import TrainApp, TrainAppCategory
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
 
class TrainAppViewSet(viewsets.ModelViewSet):
    queryset = TrainApp.objects.all()
    serializer_class = TrainAppSerializer  

    
class TrainAppCrudViewSet(viewsets.ModelViewSet):
    queryset = TrainApp.objects.all()
    serializer_class = TrainAppCrudSerializer
    

class TrainAppCatViewSet(viewsets.ModelViewSet):
    queryset = TrainAppCategory.objects.all()
    serializer_class = TrainAppCatSerializer