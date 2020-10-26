from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from django import forms

from .models import Question, Answer


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вопрос'
            }),
        }


class AnswerForm(ModelForm):

    class Meta:
        model = Answer
        fields = ["text"]
        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ответ'
            }),
        }


class SearchForm(ModelForm):

    class Meta:
        model = Question
        fields = ["title"]
        widgets = {
            "title": TextInput(attrs={
                'name': 'q',
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }),
        }


# class AuthUserForm(AuthenticationForm, ModelForm):
#
#     class Meta:
#         model = User
#         fields = ("username", "password",)
#
#
# class RegisterUserForm(ModelForm):
#
#     class Meta:
#         model = User
#         fields = ("username", "password",)
#
#
# class SearchForm(ModelForm):
#
#     class Meta:
#         model = Question
