from django.test import TestCase

from main.forms import QuestionForm, AnswerForm, SearchForm
from main.models import Question, Answer


class QuestionFormTest(TestCase):

    def test_valid_question_form(self):
        question = Question.objects.create(author_id=None, title='Question1', description='a lot of words')
        data = {
            "title": question.title,
            "description": question.description,
        }
        form = QuestionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_question_form(self):
        question = Question.objects.create(author_id=None, title='Question1', description='')
        data = {
            "title": question.title,
            "description": question.description,
        }
        form = QuestionForm(data=data)
        self.assertFalse(form.is_valid())


class AnswerFormTest(TestCase):

    def test_valid_answer_form(self):
        question = Question.objects.create(author_id=None, title='Question1', description='a lot of words')
        answer = Answer.objects.create(author_id=None, text='a lot of words', question_id=question)
        data = {
            "text": answer.text,
        }
        form = AnswerForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_answer_form(self):
        question = Question.objects.create(author_id=None, title='Question1', description='a lot of words')
        answer = Answer.objects.create(author_id=None, text='', question_id=question)
        data = {
            "text": answer.text,
        }
        form = AnswerForm(data=data)
        self.assertFalse(form.is_valid())


class SearchFormTest(TestCase):

    def test_valid_search_form(self):
        result = 'question'
        data = {
            "title": result,
        }
        form = SearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_search_form(self):
        result = ''
        data = {
            "title": result,
        }
        form = SearchForm(data=data)
        self.assertFalse(form.is_valid())
