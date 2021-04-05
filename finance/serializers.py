from rest_framework import serializers

from .models import CsvData


class FinanceDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CsvData
        fields = '__all__'


class ParseDataSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
