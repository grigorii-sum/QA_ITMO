from django.test import Client, TestCase


class NewQuestionsViewTest(TestCase):

    def test_register_page_view(self):
        c = Client()
        context = {
            'username': 'ilya',
            'password1': 'ilya12345678',
            'password2': 'ilya12345678',
        }
        resp = c.post('/login/', context)

        self.assertEqual(resp.status_code, 200)

    def test_login_page_view(self):
        c = Client()
        context = {
            'username': 'ilya',
            'password': 'ilya12345678',
        }
        resp = c.post('/login/', context)

        self.assertEqual(resp.status_code, 200)

    def test_search_question_view(self):
        c = Client()
        context = {
            'title': 'question',
        }
        resp = c.post('/search-question', context)

        self.assertEqual(resp.status_code, 200)

    def test_create_question_view(self):
        c = Client()
        context = {
            'title': 'question 1',
            'description': 'this is the best question',
        }
        resp = c.post('/create-question', context)

        self.assertEqual(resp.status_code, 200)

    def test_question_view(self):
        c = Client()
        context = {
            'text': 'this is the best answer',
        }
        resp = c.post('/question/<int:id>', context)

        self.assertEqual(resp.status_code, 200)

