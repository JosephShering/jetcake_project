from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=1024)
    user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='questions')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'question'

class Answer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    question = models.ForeignKey('Question', models.CASCADE, related_name='answers')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='answers')

class BookmarkedQuestion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    question = models.ForeignKey('Question', models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE, related_name='bookmarked_questions')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'question_bookmarked_question'

class BookmarkedAnswer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    answer = models.ForeignKey('Answer', models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE, related_name='bookmarked_answers')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'question_bookmarked_answer'