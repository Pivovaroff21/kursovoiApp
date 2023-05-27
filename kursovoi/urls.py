from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', include('transaction.urls')),
    path('cards/', include('card.urls')),
    path('login/', obtain_auth_token),
]
