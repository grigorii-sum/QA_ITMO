from django.test import TestCase
from main.models import ExtendedUser, Question, Answer


class ExtendedUserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ExtendedUser.objects.create(user_id='grisha', count_answer=0)

    def test_user_id_label(self):
        extended_user = ExtendedUser.objects.get(id=1)
        field_label = extended_user._meta.get_field('user_id').verbose_name
        self.assertEquals(field_label, 'user id')

    def test_count_answer_label(self):
        extended_user = ExtendedUser.objects.get(id=1)
        field_label = extended_user._meta.get_field('count_answer').verbose_name
        self.assertEquals(field_label, 'count answer')

    def test_user_id_max_length(self):
        extended_user = ExtendedUser.objects.get(id=1)
        max_length = extended_user._meta.get_field('user_id').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_count_answer(self):
        extended_user = ExtendedUser.objects.get(id=1)
        object_name = '%s' % extended_user.count_answer
        self.assertEquals(object_name, str(extended_user))


class QuestionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Question.objects.create(author_id=None, title='Question1', description='a lot of words')

    def test_author_id_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('author_id').verbose_name
        self.assertEquals(field_label, 'author id')

    def test_title_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_created_date_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('created_date').verbose_name
        self.assertEquals(field_label, 'created date')

    def test_title_max_length(self):
        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_title(self):
        question = Question.objects.get(id=1)
        object_name = '%s' % question.title
        self.assertEquals(object_name, str(question))


class AnswerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        question = Question.objects.create(author_id=None, title='Question1', description='a lot of words')
        Answer.objects.create(author_id=None, text='a lot of words', question_id=question)

    def test_author_id_label(self):
        answer = Answer.objects.get(id=1)
        field_label = answer._meta.get_field('author_id').verbose_name
        self.assertEquals(field_label, 'author id')

    def test_text_label(self):
        answer = Answer.objects.get(id=1)
        field_label = answer._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_question_id_label(self):
        answer = Answer.objects.get(id=1)
        field_label = answer._meta.get_field('question_id').verbose_name
        self.assertEquals(field_label, 'question id')

    def test_created_date_label(self):
        answer = Answer.objects.get(id=1)
        field_label = answer._meta.get_field('created_date').verbose_name
        self.assertEquals(field_label, 'created date')

    def test_object_name_is_text(self):
        answer = Answer.objects.get(id=1)
        object_name = '%s' % answer.text
        self.assertEquals(object_name, str(answer))
