from rest_framework import serializers
from django.utils. html import escape
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        # проверка на пустое содержание
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty or whitespace.")
        return escape(value)
    
    def validate_content(self, value):
        # проверка на пустое содержание
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty or whitespace.")
        return escape(value)
    
class NoteCreateSerializer(NoteSerializer):
    pass

class NoteUpdateSerializer(NoteSerializer):
    # Для обновления заметок, делает поля необязательными
    title = serializers.CharField(required=False)
    conent = serializers.CharField(required=False)
