from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('id', 'number', 'balance', 'month', 'year', 'cvv')

    def create(self, validated_data):
        return Card.objects.create(validated_data)
