from rest_framework import generics, viewsets
from khm_questions.serializers import KhmQuestionsSerializer, KhmQuestionsCrudSerializer, KhmCatSerializer, UserSerializer
from .models import KhmQuestions, KhmQuestionsCategory
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
 
class KhmQuestionsViewSet(viewsets.ModelViewSet):
    queryset = KhmQuestions.objects.all()
    serializer_class = KhmQuestionsSerializer  

    
class KhmQuestionsCrudViewSet(viewsets.ModelViewSet):
    queryset = KhmQuestions.objects.all()
    serializer_class = KhmQuestionsCrudSerializer
    

class KhmCategoryViewSet(viewsets.ModelViewSet):
    queryset = KhmQuestionsCategory.objects.all()
    serializer_class = KhmCatSerializer