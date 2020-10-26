from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages

from .forms import QuestionForm, AnswerForm, SearchForm, CreateUserForm
from .models import Question, Answer


def register_page(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
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

    context = {}
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


def top_users(request):
    users = User.objects.all()[:10]
    context = {
        'title': 'Топ пользователей',
        'users': users,
    }
    return render(request, 'main/top_users.html', context)


def search_question(request):
    error = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # results = Question.objects.all()
            # query = request.POST.get('q', None)
            return redirect('result')
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

    # def get_queryset(self, request):
    #     # Получаем не отфильтрованный кверисет всех моделей
    #     queryset = Question.objects.all()
    #     q = self.request.GET.get("q")
    #     if q:
    #         # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
    #         results = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
    #         context = {
    #             'title': 'Результаты запроса',
    #             'results': results,
    #         }
    #         return render(request, 'main/result_search_question.html', context)
    #     results = queryset
    #     context = {
    #         'title': 'Результаты запроса',
    #         'results': results,
    #     }
    #     return render(request, 'main/result_search_question.html', context)

    # query = request.POST.get('q')
    results = Question.objects.filter(Q(title__icontains='q') | Q(description__icontains='q'))
    # results = list(chain(*query_set))
    # results.sort(key=lambda x: x.created_date, reverse=True)
    # results = query_set
    context = {
        'title': 'Результаты запроса',
        'results': results,
    }
    return render(request, 'main/result_search_question.html', context)


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
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author_id = request.user
            answer.question_id = Question.objects.get(id=id)
            answer.save()
        else:
            error = 'Сначала введите ответ'
    form = AnswerForm()
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question_id=id)
    context = {
        'title': 'Вопрос номер ' + str(id),
        'question': question,
        'answers': answers,
        'form': form,
        'error': error,
    }
    return render(request, 'main/question.html', context)

