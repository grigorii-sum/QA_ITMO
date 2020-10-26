from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # попробовать при поиске передать значения через скобки (как в функции)
    path('', views.new_questions, name='new'),
    path('top-users', views.top_users, name='top'),
    path('search-question', views.search_question, name='search'),
    path('result-search-question', views.result_search_question, name='result'),
    path('create-question', views.create_question, name='create'),
    path('question/<int:id>', views.question, name='question'),
]
