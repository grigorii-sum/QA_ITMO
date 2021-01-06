from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import CreateUserForm, QuestionForm, AnswerForm, SearchForm, UpdateForm
from .models import ExtendedUser, Question, Answer


def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            extended_user = ExtendedUser.create(request.POST.get('username'))
            extended_user.save()

            form.save()
            return redirect('login')
    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'main/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('new')

    context = {
        'title': 'Вход',
    }
    return render(request, 'main/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def new_questions(request):
    questions = Question.objects.order_by('-created_date')[:5]
    context = {
        'title': 'Новые вопросы',
        'questions': questions,
    }
    return render(request, 'main/new_questions.html', context)


@login_required
def top_users(request):
    extended_users = ExtendedUser.objects.order_by('-count_answer')[:10]
    context = {
        'title': 'Топ 10 пользователей',
        'extended_users': extended_users,
    }
    return render(request, 'main/top_users.html', context)


def search_question(request):
    error = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = request.POST.get('title')
            results = Question.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
            context = {
                'title': 'Результаты поиска',
                'results': results,
            }
            return render(request, 'main/result_search_question.html', context)
        else:
            error = 'Сначала введите поисковый запрос'
    form = SearchForm()
    context = {
        'title': 'Поиск',
        'form': form,
        'error': error,
    }
    return render(request, 'main/search_question.html', context)


def result_search_question(request):
    context = {
        'title': 'Результаты запроса',
    }
    return render(request, 'main/result_search_question.html', context)


@login_required
def create_question(request):
    error = ''
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author_id = request.user
            question.save()
            return redirect('new')
        else:
            error = 'Форма была заполнена неверно'
    else:
        form = QuestionForm()
    context = {
        'title': 'Создание вопроса',
        'form': form,
        'error': error,
    }
    return render(request, 'main/create_question.html', context)


def question(request, id):
    error = ''

    if request.POST:
        form = AnswerForm(request.POST)

        if form.is_valid():
            extended_user = ExtendedUser.objects.get(user_id=request.user.username)
            extended_user.count_answer += 1
            extended_user.save()

            answer = form.save(commit=False)
            answer.author_id = request.user
            answer.question_id = Question.objects.get(id=id)
            answer.save()
        else:
            error = 'Сначала введите ответ'

    form = AnswerForm()
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question_id=id, is_best=False)
    best_answer = Answer.objects.filter(question_id=id, is_best=True)
    context = {
        'title': 'Вопрос номер ' + str(id),
        'question': question,
        'answers': answers,
        'form': form,
        'error': error,
        'best_answer': best_answer,
    }
    return render(request, 'main/question.html', context)


@login_required
def choose_best_answer(request, id):
    change_form = UpdateForm()
    answers = Answer.objects.filter(question_id=id)
    question = Question.objects.get(id=id)
    context = {
        'title': 'Выбор лучшего ответа для вопроса номер ' + str(id),
        'change_form': change_form,
        'question': question,
        'answers': answers,
    }
    return render(request, 'main/choose_best_answer.html', context)


@login_required
def change_answer_status(request, id):
    answer = Answer.objects.get(id=id)
    answer.is_best = True
    answer.save()

    question_id = answer.question_id.id

    question = Question.objects.get(id=question_id)

    return redirect('question', id=question.id)
