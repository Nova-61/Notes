<!-- frontend/src/views/HomeView.vue -->
<script setup>
import { RouterLink } from 'vue-router'
import { useNotesStore } from '@/stores/notes'
import { onMounted } from 'vue'

const notesStore = useNotesStore()

onMounted(() => {
  // Загружаем заметки для показа статистики
  notesStore.fetchNotes()
})
</script>

<template>
  <div class="min-h-screen" style="background: linear-gradient(135deg, #f5f1ed 0%, #f0ebe7 100%)">
    <div class="w-full px-4 sm:px-6 lg:px-8 py-16">
      <!-- Hero Section -->
      <div class="text-center mb-20">
        <h1 class="text-5xl md:text-7xl font-bold mb-6" style="color: #6b5844;">
          Добро пожаловать в 📝
          <span style="background: linear-gradient(135deg, #a67c52 0%, #d4a574 100%); background-clip: text; -webkit-background-clip: text; -webkit-text-fill-color: transparent;">SNotes</span>
        </h1>
        <p class="text-xl mb-12 max-w-3xl mx-auto" style="color: #999999;">
          Самое красивое и удобное приложение для создания, редактирования и управления вашими заметками с теплой и уютной палитрой.
        </p>
        
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <RouterLink 
            to="/notes" 
            class="px-10 py-4 rounded-xl font-bold text-lg transition-all duration-300 flex items-center justify-center gap-2 shadow-lg hover:shadow-xl transform hover:scale-105"
            style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); color: white;"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            Мои заметки
          </RouterLink>
          
          <RouterLink 
            to="/notes/create" 
            class="px-10 py-4 rounded-xl font-bold text-lg transition-all duration-300 flex items-center justify-center gap-2 shadow-lg hover:shadow-xl transform hover:scale-105"
            style="background: white; color: #a67c52; border: 2px solid #d4a574;"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
            </svg>
            Создать заметку
          </RouterLink>
        </div>
      </div>

      <!-- Statistics -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20 max-w-4xl mx-auto">
        <div class="rounded-2xl shadow-lg p-8 text-center transition-all duration-300 hover:shadow-2xl hover:scale-105" style="background: white; border: 2px solid #e8ddd5;">
          <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4" style="background: rgba(166, 124, 82, 0.1); color: #a67c52;">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h3 class="text-4xl font-bold mb-2" style="color: #6b5844;">{{ notesStore.notesCount }}</h3>
          <p style="color: #999999;">Всего заметок</p>
        </div>

        <div class="rounded-2xl shadow-lg p-8 text-center transition-all duration-300 hover:shadow-2xl hover:scale-105" style="background: white; border: 2px solid #e8ddd5;">
          <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4" style="background: rgba(166, 124, 82, 0.1); color: #a67c52;">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <h3 class="text-4xl font-bold mb-2" style="color: #6b5844;">⚡</h3>
          <p style="color: #999999;">Молниеносно быстро</p>
        </div>

        <div class="rounded-2xl shadow-lg p-8 text-center transition-all duration-300 hover:shadow-2xl hover:scale-105" style="background: white; border: 2px solid #e8ddd5;">
          <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4" style="background: rgba(166, 124, 82, 0.1); color: #a67c52;">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h-2m0 0H8m4 0v6m0-6v-2m0 2V8" />
            </svg>
          </div>
          <h3 class="text-4xl font-bold mb-2" style="color: #6b5844;">💎</h3>
          <p style="color: #999999;">Премиум опыт</p>
        </div>
      </div>

      <!-- Features -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center max-w-6xl mx-auto">
        <div>
          <h2 class="text-4xl font-bold mb-8" style="color: #6b5844;">✨ Возможности</h2>
          <div class="space-y-6">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-lg flex items-center justify-center flex-shrink-0 text-2xl" style="background: rgba(166, 124, 82, 0.1); color: #a67c52;">
                ✍️
              </div>
              <div>
                <h3 class="font-bold text-lg mb-2" style="color: #6b5844;">Создание заметок</h3>
                <p style="color: #999999;">Создавайте новые заметки с красивым форматированием и предпросмотром</p>
              </div>
            </div>
            
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-lg flex items-center justify-center flex-shrink-0 text-2xl" style="background: rgba(166, 124, 82, 0.1); color: #a67c52;">
                ✏️
              </div>
              <div>
                <h3 class="font-bold text-lg mb-2" style="color: #6b5844;">Редактирование</h3>
                <p style="color: #999999;">Изменяйте заметки в любой момент с полной сохранностью данных</p>
              </div>
            </div>
            
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-lg flex items-center justify-center flex-shrink-0 text-2xl" style="background: rgba(166, 124, 82, 0.1); color: #a67c52;">
                📊
              </div>
              <div>
                <h3 class="font-bold text-lg mb-2" style="color: #6b5844;">Организация</h3>
                <p style="color: #999999;">Все заметки отсортированы по дате, легко найти нужное</p>
              </div>
            </div>
            
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-lg flex items-center justify-center flex-shrink-0 text-2xl" style="background: rgba(166, 124, 82, 0.1); color: #a67c52;">
                🎨
              </div>
              <div>
                <h3 class="font-bold text-lg mb-2" style="color: #6b5844;">Прекрасный дизайн</h3>
                <p style="color: #999999;">Теплая и уютная цветовая палитра, приятно использовать</p>
              </div>
            </div>
          </div>
        </div>

        <div class="rounded-2xl shadow-2xl p-10 transition-all duration-300 hover:shadow-xl hover:scale-105" style="background: white; border: 2px solid #e8ddd5;">
          <h3 class="text-2xl font-bold mb-4" style="color: #6b5844;">🚀 Начните прямо сейчас!</h3>
          <p class="mb-8" style="color: #999999;">
            Создайте свою первую заметку и почувствуйте удобство работы с красивым интерфейсом. Все просто и интуитивно!
          </p>
          <RouterLink 
            to="/notes/create" 
            class="w-full py-4 rounded-xl font-bold text-lg transition-all duration-300 inline-flex items-center justify-center gap-2 shadow-lg hover:shadow-xl transform hover:scale-105"
            style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); color: white;"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
            </svg>
            Создать первую заметку
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>