from django.urls import path, include
# from transaction.views import transaction_list, transaction_detail
from transaction import views


urlpatterns = [
    path('', views.TransactionList.as_view()),
    path('<int:pk>/', views.TransactionDetail.as_view()),
]
