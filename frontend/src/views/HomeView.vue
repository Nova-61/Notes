<!-- frontend/src/views/HomeView.vue -->
<script setup>
import { RouterLink } from 'vue-router'
import { useNotesStore } from '@/stores/notes'
import { onMounted } from 'vue'

const notesStore = useNotesStore()

onMounted(() => {
  notesStore.fetchNotes()
})
</script>

<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Section - Минималистичный -->
    <section class="h-screen flex items-center justify-center overflow-hidden relative">
      <div class="absolute inset-0 bg-gradient-to-br from-gray-50 via-white to-gray-50"></div>
      
      <div class="relative w-full max-w-7xl px-6 sm:px-12 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <!-- Text Content -->
        <div class="flex flex-col justify-center">
          <p class="text-sm tracking-widest uppercase text-gray-400 mb-6 font-semibold">Добро пожаловать</p>
          <h1 class="text-6xl sm:text-7xl lg:text-8xl font-light leading-tight mb-8" style="color: #1a1a1a; letter-spacing: -0.02em;">
            SNotes
          </h1>
          <p class="text-lg sm:text-xl text-gray-600 leading-relaxed mb-12 max-w-md font-light">
            Минималистичное приложение для управления вашими заметками. Просто, красиво, эффективно.
          </p>
          
          <div class="flex flex-col sm:flex-row gap-6">
            <RouterLink 
              to="/notes" 
              class="px-8 py-4 text-center font-semibold transition-all duration-300 hover:scale-105 border-2"
              style="border-color: #a67c52; color: white; background: #a67c52;"
            >
              Мои заметки
            </RouterLink>
            
            <RouterLink 
              to="/notes/create" 
              class="px-8 py-4 text-center font-semibold transition-all duration-300 hover:scale-105 border-2"
              style="border-color: #a67c52; color: #a67c52; background: transparent;"
            >
              Новая заметка
            </RouterLink>
          </div>
        </div>

        <!-- Image/Visual -->
        <div class="relative h-96 lg:h-full flex items-center justify-center">
          <div class="absolute inset-0 bg-gradient-to-br from-gray-100 to-gray-200 opacity-50"></div>
          <div class="relative">
            <div class="text-center">
              <svg class="w-40 h-40 sm:w-56 sm:h-56 mx-auto" style="color: #d4a574; opacity: 0.4;" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-5.04-6.71l-2.75 3.54-2.29-2.92c-.2-.26-.53-.4-.85-.4-.32 0-.65.14-.86.4l-2.29 2.92 4.15 5.29 4.15-5.29-2.75-3.54z"/>
              </svg>
              <p class="mt-6 text-gray-400 text-sm uppercase tracking-wide">Упорядочивайте свои мысли</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Statistics Section -->
    <section class="bg-gray-50 py-20 sm:py-32 px-6 sm:px-12">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-20">
          <div class="text-center">
            <p class="text-5xl sm:text-6xl font-light mb-2" style="color: #a67c52;">{{ notesStore.notesCount }}</p>
            <p class="text-gray-500 text-sm uppercase tracking-widest font-semibold">Заметок создано</p>
          </div>
          
          <div class="text-center">
            <p class="text-5xl sm:text-6xl font-light mb-2" style="color: #a67c52;">∞</p>
            <p class="text-gray-500 text-sm uppercase tracking-widest font-semibold">Возможностей</p>
          </div>
          
          <div class="text-center">
            <p class="text-5xl sm:text-6xl font-light mb-2" style="color: #a67c52;">100%</p>
            <p class="text-gray-500 text-sm uppercase tracking-widest font-semibold">Открытый код</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 sm:py-32 px-6 sm:px-12 bg-white">
      <div class="max-w-7xl mx-auto">
        <h2 class="text-4xl sm:text-5xl font-light mb-20 text-center" style="color: #1a1a1a;">Основные возможности</h2>
        
        <div class="space-y-24">
          <!-- Feature 1 -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            <div class="h-80 bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center order-2 md:order-1">
              <svg class="w-32 h-32" style="color: #d4a574; opacity: 0.3;" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
              </svg>
            </div>
            <div class="order-1 md:order-2">
              <h3 class="text-3xl font-light mb-4" style="color: #1a1a1a;">Создание</h3>
              <p class="text-gray-600 leading-relaxed text-lg font-light mb-6">
                Быстро создавайте новые заметки с красивым интерфейсом. Интуитивные элементы управления и удобная сортировка.
              </p>
            </div>
          </div>

          <!-- Feature 2 -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            <div class="h-80 bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center">
              <svg class="w-32 h-32" style="color: #d4a574; opacity: 0.3;" fill="currentColor" viewBox="0 0 24 24">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25z"/>
              </svg>
            </div>
            <div>
              <h3 class="text-3xl font-light mb-4" style="color: #1a1a1a;">Редактирование</h3>
              <p class="text-gray-600 leading-relaxed text-lg font-light mb-6">
                Легко изменяйте свои заметки в любой момент. Все изменения сохраняются автоматически с полной историей.
              </p>
            </div>
          </div>

          <!-- Feature 3 -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            <div class="h-80 bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center order-2 md:order-1">
              <svg class="w-32 h-32" style="color: #d4a574; opacity: 0.3;" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
              </svg>
            </div>
            <div class="order-1 md:order-2">
              <h3 class="text-3xl font-light mb-4" style="color: #1a1a1a;">Организация</h3>
              <p class="text-gray-600 leading-relaxed text-lg font-light mb-6">
                Заметки автоматически организуются по дате создания. Быстрый поиск и удобная навигация.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 sm:py-32 px-6 sm:px-12" style="background: #f5f1ed;">
      <div class="max-w-3xl mx-auto text-center">
        <h2 class="text-4xl sm:text-5xl font-light mb-8" style="color: #1a1a1a;">Начните использовать SNotes прямо сейчас</h2>
        <p class="text-lg text-gray-600 mb-12 font-light">Создавайте и организуйте ваши заметки с минималистичным дизайном</p>
        
        <RouterLink 
          to="/notes/create" 
          class="inline-block px-12 py-5 text-center font-semibold transition-all duration-300 hover:scale-105 border-2"
          style="border-color: #a67c52; color: white; background: #a67c52; font-size: 1.1rem;"
        >
          Создать заметку
        </RouterLink>
      </div>
    </section>

    <!-- Footer Stats -->
    <section class="bg-gray-50 py-12 px-6 sm:px-12 border-t border-gray-200">
      <div class="max-w-7xl mx-auto">
        <p class="text-center text-gray-500 text-sm font-light">
          © 2025 SNotes. Создано с минимализмом и любовью к простоте.
        </p>
      </div>
    </section>
  </div>
</template>