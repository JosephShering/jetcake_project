from django.urls import path
from django.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register('questions', views.QuestionViewSet, basename='question')
router.register('answers', views.AnswerViewSet, basename='answer')
router.register('bookmarked_questions', views.BookMarkedQuestionViewSet, basename='bookmarked-question')
router.register('bookmarked_answers', views.BookmarkedAnswerViewSet, basename='bookmarked-answer')

urlpatterns = [
    path('', include(router.urls))
]
