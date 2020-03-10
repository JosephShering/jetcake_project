from pprint import pprint
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import throttling
from rest_framework.response import Response

from . import throttles
from . import models
from . import serializers

class ProtectedViewSets(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    throttling_classes = [throttles.QuestionThrottleSustained]

class QuestionViewSet(ProtectedViewSets):
    serializer_class = serializers.QuestionSerializer

    """
        We don't want people asking a ton of questions instantly, so we slow down their question making ability
    """
    def get_throttles(self):
        if self.action == 'create':
            return [
                throttles.QuestionCreationThrottleSustained()
            ]
            
        return super().get_throttles();

    """
        We only want users to see their questions, and only be able to modify their questions.
    """
    def get_queryset(self):
        return self.request.user.questions.all()

class AnswerViewSet(ProtectedViewSets):
    serializer_class = serializers.AnswerSerializer

    def get_queryset(self):
        return self.request.user.answers.all()

class BookMarkedQuestionViewSet(ProtectedViewSets):
    serializer_class = serializers.BookmarkedQuestionSerializer

    def get_queryset(self):
        return self.request.user.bookmarked_questions.all()

class BookmarkedAnswerViewSet(ProtectedViewSets):
    serializer_class = serializers.BookmarkedAnswerSerializer
    
    def get_queryset(self):
        return self.request.user.bookmarked_answers.all()