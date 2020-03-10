from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^token/', obtain_auth_token),
    url(r'', include('question.urls'))
]
