# serializers.py
from rest_framework import serializers

class LlmSerializer(serializers.Serializer):
    sentence = serializers.CharField()
    response = serializers.CharField(required=False)
