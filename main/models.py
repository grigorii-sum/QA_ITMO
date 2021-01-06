from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone


class ExtendedUser(models.Model):
    user_id = models.CharField(max_length=100)
    count_answer = models.IntegerField(null=False)

    def __str__(self):
        return str(self.count_answer)

    @classmethod
    def create(cls, user_id):
        extended_user = cls(user_id=user_id, count_answer=0)
        return extended_user

    class Meta:
        verbose_name = 'Расширенный пользователь'
        verbose_name_plural = 'Расширенные пользователи'


class QuestionManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        queryset = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query) | Q(description__icontains=query))
            queryset = queryset.filter(or_lookup)
        return queryset


class Question(models.Model):
    objects = QuestionManager()

    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    is_best = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
