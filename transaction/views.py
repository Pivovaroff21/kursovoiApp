from django.shortcuts import render
from .serializers import TransactionSerializer
from .models import Transaction
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def transaction_list(request):
    if request.method == "GET":
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(serializer.data,safe=False)


@api_view(['GET'])
def transaction_detail(request,pk):
    if request.method == "GET":
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction)
        return JsonResponse(serializer.data , safe=False)

# If i want send 1 field need to write serializer for it with 1 field
