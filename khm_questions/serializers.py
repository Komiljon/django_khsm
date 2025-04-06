from rest_framework import serializers
from django.contrib.auth.models import User
from .models import KhmQuestions, KhmQuestionsCategory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_active']

class KhmQuestionsSerializer(serializers.ModelSerializer):
    cat = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = KhmQuestions
        fields = ('__all__')

        
class KhmQuestionsCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhmQuestions
        fields = ('__all__')
        

class KhmCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhmQuestionsCategory
        fields = ('__all__')


        