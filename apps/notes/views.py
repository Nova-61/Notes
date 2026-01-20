from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Note
from .serializers import NoteSerializer, NoteCreateSerializer, NoteUpdateSerializer

# Create your views here.

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    
    def get_serializer_class(self):
        # Выор сериализатора в зависимости от метода запросба
        if self.request.method == 'POST':
            return NoteCreateSerializer
        return NoteSerializer
    
    def get(self, request, *args, **kwargs):
        # Обрабатка GET-запроса для получения списка заметок
        return super().get(request, *args, **kwargs)
    
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    # Выбор сериализатора в зависимости от метода запроса
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return NoteUpdateSerializer
        return NoteSerializer
    
    def update(self, request, *args, **kwargs):
        # Обработка PUT/PATCH-запроса для обновления заметки
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        # Обработка DELETE-запроса для удаления заметки
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Note deleted successfully.'},
            status=status.HTTP_204_NO_CONTENT
        )