from django.urls import path, include
from card import views

urlpatterns = [
    path('', views.CardList.as_view()),
]
