from django.contrib import admin
from django.urls import path, include

from .views import MainView

urlpatterns = [
    path('', views.MainView.as_view()),
]
