from rest_framework.serializers import ModelSerializer

from .models import ExtendedUser, Question, Answer


class ExtendedUserSerializer(ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
