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
  <div class="min-h-screen" style="background: #f8f7f5;">
    <div class="w-full px-4 sm:px-6 lg:px-8">
      <div class="hero relative w-full py-12 sm:py-20 md:py-32 lg:py-40" style="background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); border-radius: 0 0 0 0;">
        <div class="max-w-6xl mx-auto">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center">
            <div>
              <h1 class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold mb-4 sm:mb-6 leading-tight" style="color: white;">
                Организуйте свои мысли
              </h1>
              <p class="text-base sm:text-lg md:text-xl mb-8 md:mb-10 leading-relaxed" style="color: #d0d0d0;">
                Простое и эффективное приложение для создания, редактирования и управления вашими заметками. Профессиональный инструмент с красивым интерфейсом.
              </p>
              <div class="flex flex-col sm:flex-row gap-4">
                <RouterLink 
                  to="/notes" 
                  class="px-8 sm:px-10 py-3.5 sm:py-4 rounded-lg font-bold text-base sm:text-lg transition-all duration-300 flex items-center justify-center gap-2 shadow-xl hover:shadow-2xl transform hover:scale-105 text-white"
                  style="background: #FF5722;"
                >
                  <svg class="w-5 h-5 sm:w-6 sm:h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                  </svg>
                  Мои заметки
                </RouterLink>
                
                <RouterLink 
                  to="/notes/create" 
                  class="px-8 sm:px-10 py-3.5 sm:py-4 rounded-lg font-bold text-base sm:text-lg transition-all duration-300 flex items-center justify-center gap-2 shadow-xl hover:shadow-2xl transform hover:scale-105"
                  style="background: white; color: #FF5722; border: 2px solid #FF5722;"
                >
                  <svg class="w-5 h-5 sm:w-6 sm:h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                  </svg>
                  Создать
                </RouterLink>
              </div>
            </div>
            
            <div class="hidden md:block">
              <div class="relative h-80 md:h-96 rounded-lg overflow-hidden shadow-2xl" style="background: linear-gradient(135deg, #FF5722 0%, #FF7043 100%); display: flex; align-items: center; justify-content: center;">
                <div class="text-center">
                  <div class="text-8xl mb-4">📝</div>
                  <p class="text-white text-xl font-semibold">Ваши идеи в одном месте</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="w-full py-16 sm:py-20 md:py-24">
        <div class="max-w-6xl mx-auto">
          <div class="text-center mb-12 md:mb-16">
            <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-4" style="color: #1a1a1a;">Почему SNotes?</h2>
            <p class="text-base sm:text-lg md:text-xl" style="color: #7a7a7a; max-width: 600px; margin: 0 auto;">
              Все необходимое для продуктивности в одном приложении
            </p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8 mb-12 md:mb-16">
            <div class="p-6 sm:p-8 rounded-xl transition-all duration-300 hover:shadow-xl transform hover:scale-105" style="background: white; border: 1px solid #e0e0e0;">
              <div class="w-14 h-14 rounded-lg flex items-center justify-center mb-4 text-3xl" style="background: rgba(255, 87, 34, 0.1);">
                ⚡
              </div>
              <h3 class="font-bold text-xl mb-3" style="color: #1a1a1a;">Молниеносно быстро</h3>
              <p style="color: #7a7a7a; line-height: 1.6;">Создавайте и редактируйте заметки со скоростью мысли. Все работает мгновенно.</p>
            </div>

            <div class="p-6 sm:p-8 rounded-xl transition-all duration-300 hover:shadow-xl transform hover:scale-105" style="background: white; border: 1px solid #e0e0e0;">
              <div class="w-14 h-14 rounded-lg flex items-center justify-center mb-4 text-3xl" style="background: rgba(255, 87, 34, 0.1);">
                🎨
              </div>
              <h3 class="font-bold text-xl mb-3" style="color: #1a1a1a;">Красивый дизайн</h3>
              <p style="color: #7a7a7a; line-height: 1.6;">Современный и чистый интерфейс, разработанный с вниманием к деталям.</p>
            </div>

            <div class="p-6 sm:p-8 rounded-xl transition-all duration-300 hover:shadow-xl transform hover:scale-105" style="background: white; border: 1px solid #e0e0e0;">
              <div class="w-14 h-14 rounded-lg flex items-center justify-center mb-4 text-3xl" style="background: rgba(255, 87, 34, 0.1);">
                📱
              </div>
              <h3 class="font-bold text-xl mb-3" style="color: #1a1a1a;">Адаптивный дизайн</h3>
              <p style="color: #7a7a7a; line-height: 1.6;">Работает на любом устройстве - телефоне, планшете или компьютере.</p>
            </div>

            <div class="p-6 sm:p-8 rounded-xl transition-all duration-300 hover:shadow-xl transform hover:scale-105" style="background: white; border: 1px solid #e0e0e0;">
              <div class="w-14 h-14 rounded-lg flex items-center justify-center mb-4 text-3xl" style="background: rgba(255, 87, 34, 0.1);">
                🔍
              </div>
              <h3 class="font-bold text-xl mb-3" style="color: #1a1a1a;">Поиск</h3>
              <p style="color: #7a7a7a; line-height: 1.6;">Быстро найдите нужную заметку с помощью мощной функции поиска.</p>
            </div>

            <div class="p-6 sm:p-8 rounded-xl transition-all duration-300 hover:shadow-xl transform hover:scale-105" style="background: white; border: 1px solid #e0e0e0;">
              <div class="w-14 h-14 rounded-lg flex items-center justify-center mb-4 text-3xl" style="background: rgba(255, 87, 34, 0.1);">
                📊
              </div>
              <h3 class="font-bold text-xl mb-3" style="color: #1a1a1a;">Статистика</h3>
              <p style="color: #7a7a7a; line-height: 1.6;">Отслеживайте количество заметок и следите за своей продуктивностью.</p>
            </div>

            <div class="p-6 sm:p-8 rounded-xl transition-all duration-300 hover:shadow-xl transform hover:scale-105" style="background: white; border: 1px solid #e0e0e0;">
              <div class="w-14 h-14 rounded-lg flex items-center justify-center mb-4 text-3xl" style="background: rgba(255, 87, 34, 0.1);">
                🚀
              </div>
              <h3 class="font-bold text-xl mb-3" style="color: #1a1a1a;">Простота</h3>
              <p style="color: #7a7a7a; line-height: 1.6;">Интуитивный интерфейс - не требует обучения, все просто и понятно.</p>
            </div>
          </div>

          <div class="text-center">
            <h3 class="text-2xl sm:text-3xl md:text-4xl font-bold mb-6" style="color: #1a1a1a;">Готовы начать?</h3>
            <p class="text-base sm:text-lg mb-8" style="color: #7a7a7a; max-width: 500px; margin: 0 auto 2rem;">
              Создайте свою первую заметку и начните организовывать свои мысли прямо сейчас
            </p>
            <RouterLink 
              to="/notes/create" 
              class="inline-block px-10 sm:px-12 py-4 rounded-lg font-bold text-lg transition-all duration-300 shadow-xl hover:shadow-2xl transform hover:scale-105"
              style="background: #FF5722; color: white;"
            >
              Начать сейчас
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>