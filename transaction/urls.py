from django.urls import path, include
from transaction.views import transaction_list, transaction_detail



urlpatterns = [
    path('', transaction_list, name="transaction_list"),
    path('<pk>', transaction_detail, name="transaction_detail"),
]
