from rest_framework import serializers

from . import models

class UserOwnedSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

class QuestionSerializer(UserOwnedSerializer):
    class Meta:
        model = models.Question
        fields = ['id', 'title', 'description', 'user', 'created', 'modified']

class AnswerSerializer(UserOwnedSerializer):
    class Meta:
        model = models.Answer
        fields = ['id', 'body', 'question', 'user', 'created', 'modified']

class BookmarkedQuestionSerializer(UserOwnedSerializer):
    class Meta:
        model = models.BookmarkedQuestion
        fields = ['id', 'question', 'user', 'created', 'modified']

class BookmarkedAnswerSerializer(UserOwnedSerializer):
    class Meta:
        model = models.BookmarkedAnswer
        fields = ['id', 'answer', 'user', 'created', 'modified']