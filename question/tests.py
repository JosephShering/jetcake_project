import json
from django.test import TestCase
from django.urls import include
from django.urls import path
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import URLPatternsTestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate

from . import models

username = 'test_username'

class QuestionTests(APITestCase):
    fixtures = ['users', 'questions', 'answers', 'tokens']

    def setUp(self):
        token = Token.objects.get(user__username=username)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = reverse('question-list')
        data = {
            'title': 'Test Question',
            'description': 'This is a test question'
        }
        response = self.client.post(url, data)
        self.test_question = response.data
        
    def test_create_question(self):
        url = reverse('question-list')
        data = {
            'title': 'Test Question',
            'description': 'Test Description'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_list_questions(self):
        url = reverse('question-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_question(self):
        url = reverse('question-detail', args=[69])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_question(self):
        update_question_url = reverse('question-detail', args=[69])
        response = self.client.put(update_question_url, {
            'title': 'New Title',
            'description': 'New Description'
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_question(self):
        url = reverse('question-detail', args=[69])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)



class AnswerTests(APITestCase):
    fixtures = ['users', 'questions', 'answers', 'tokens']

    def setUp(self):
        token = Token.objects.get(user__username=username)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')


    def test_list_answers(self):
        url = reverse('answer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_answer(self):
        url = reverse('answer-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_answer(self):
        url = reverse('answer-list')
        response = self.client.post(url, {
            'body': 'body',
            'question': 69
        })
        self.assertEqual(response.status_code, 201)

    def test_update_answer(self):
        url = reverse('answer-detail', args=[1])
        data = {
            'body': 'updated body',
            'question': 69
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_delete_answer(self):
        url = reverse('answer-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)



class BookmarkedQuestions(APITestCase):
    fixtures = ['users', 'questions', 'answers', 'tokens', 'bookmarked_questions', 'bookmarked_answers']

    def setUp(self):
        token = Token.objects.get(user__username=username)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_list_bookmarked_questions(self):
        url = reverse('bookmarked-question-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_retrieve_bookmarked_question(self):
        url = reverse('bookmarked-question-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bookmarked_question(self):
        url = reverse('bookmarked-question-list')
        response = self.client.post(url, {
            'body': 'body',
            'question': 69
        })
        self.assertEqual(response.status_code, 201)

    def test_update_bookmarked_question(self):
        url = reverse('bookmarked-question-detail', args=[1])
        response = self.client.put(url, {
            'body': 'wefwfd',
            'question': 69
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_bookmarked_question(self):
        url = reverse('bookmarked-question-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)


class BookmarkedAnswers(APITestCase):
    fixtures = ['users', 'questions', 'answers', 'tokens', 'bookmarked_questions', 'bookmarked_answers']

    def setUp(self):
        token = Token.objects.get(user__username=username)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_list_bookmarked_answers(self):
        url = reverse('bookmarked-answer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_bookmarked_answer(self):
        url = reverse('bookmarked-answer-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bookmarked_answer(self):
        url = reverse('bookmarked-answer-list')
        response = self.client.post(url, {
            'answer': 1
        })
        self.assertEqual(response.status_code, 201)

    def test_update_bookmarked_answer(self):
        url = reverse('bookmarked-answer-detail', args=[1])
        response = self.client.put(url, {
            'answer': 2
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_bookmarked_answer(self):
        url = reverse('bookmarked-answer-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)