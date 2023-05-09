from rest_framework import serializers

from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
          'id',
          'operator', 
          'phone', 
          'date', 
          'sum', 
          'status'
        )
        
    def create(self, validated_data):
        return Transaction.objects.create(validated_data)
        
