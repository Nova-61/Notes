<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()
const mobileMenuOpen = ref(false)
</script>

<template>
  <div class="min-h-screen flex flex-col" style="background: #f8f7f5;">
    <nav style="background: #ffffff; box-shadow: 0 4px 12px rgba(255, 87, 34, 0.1); border-bottom: 2px solid #e0e0e0; position: sticky; top: 0; z-index: 50;">
      <div class="w-full px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <div class="flex items-center flex-shrink-0">
            <RouterLink to="/" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
              <svg class="w-7 h-7 md:w-8 md:h-8" style="color: #FF5722;" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-5.04-6.71l-2.75 3.54-2.29-2.92c-.2-.26-.53-.4-.85-.4-.32 0-.65.14-.86.4l-2.29 2.92 4.15 5.29 4.15-5.29-2.75-3.54z"/>
              </svg>
              <span class="text-lg md:text-2xl font-bold" style="color: #1a1a1a;">SNotes</span>
            </RouterLink>
          </div>

          <div class="hidden md:flex items-center space-x-2 lg:space-x-4">
            <RouterLink 
              to="/" 
              class="px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300 hover:transform hover:scale-105"
              style="color: #7a7a7a;"
              :style="{ color: route.path === '/' ? '#FF5722' : '#7a7a7a', backgroundColor: route.path === '/' ? 'rgba(255, 87, 34, 0.15)' : 'transparent' }"
            >
              🏠 Главная
            </RouterLink>
            <RouterLink 
              to="/notes" 
              class="px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300 hover:transform hover:scale-105"
              style="color: #7a7a7a;"
              :style="{ color: route.path.startsWith('/notes') ? '#FF5722' : '#7a7a7a', backgroundColor: route.path.startsWith('/notes') ? 'rgba(255, 87, 34, 0.15)' : 'transparent' }"
            >
              📝 Заметки
            </RouterLink>
            <RouterLink 
              to="/about" 
              class="px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300 hover:transform hover:scale-105"
              style="color: #7a7a7a;"
              :style="{ color: route.path === '/about' ? '#FF5722' : '#7a7a7a', backgroundColor: route.path === '/about' ? 'rgba(255, 87, 34, 0.15)' : 'transparent' }"
            >
              ℹ️ О приложении
            </RouterLink>
          </div>

          <button
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="md:hidden p-2 rounded-lg transition-colors"
            style="color: #FF5722; background: rgba(255, 87, 34, 0.1);"
          >
            <svg v-if="!mobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <transition name="menu">
          <div v-if="mobileMenuOpen" class="md:hidden pb-4 border-t" style="border-color: #e0e0e0; background: rgba(255, 255, 255, 0.5);">
            <RouterLink 
              to="/" 
              class="block px-4 py-3 rounded-lg text-sm font-medium transition-all duration-300 mb-2"
              style="color: #7a7a7a;"
              :style="{ color: route.path === '/' ? '#FF5722' : '#7a7a7a', backgroundColor: route.path === '/' ? 'rgba(255, 87, 34, 0.15)' : 'transparent' }"
              @click="mobileMenuOpen = false"
            >
              🏠 Главная
            </RouterLink>
            <RouterLink 
              to="/notes" 
              class="block px-4 py-3 rounded-lg text-sm font-medium transition-all duration-300 mb-2"
              style="color: #7a7a7a;"
              :style="{ color: route.path.startsWith('/notes') ? '#FF5722' : '#7a7a7a', backgroundColor: route.path.startsWith('/notes') ? 'rgba(255, 87, 34, 0.15)' : 'transparent' }"
              @click="mobileMenuOpen = false"
            >
              📝 Заметки
            </RouterLink>
            <RouterLink 
              to="/about" 
              class="block px-4 py-3 rounded-lg text-sm font-medium transition-all duration-300"
              style="color: #7a7a7a;"
              :style="{ color: route.path === '/about' ? '#FF5722' : '#7a7a7a', backgroundColor: route.path === '/about' ? 'rgba(255, 87, 34, 0.15)' : 'transparent' }"
              @click="mobileMenuOpen = false"
            >
              ℹ️ О приложении
            </RouterLink>
          </div>
        </transition>
      </div>
    </nav>

    <main class="flex-1 w-full overflow-x-hidden">
      <RouterView />
    </main>

    <footer style="background: #ffffff; border-top: 2px solid #e0e0e0;" class="mt-auto">
      <div class="w-full py-8 px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto mb-8">
          <div>
            <h3 class="font-semibold mb-3" style="color: #1a1a1a;">Об SNotes</h3>
            <p class="text-sm" style="color: #999999;">Приложение для создания и управления заметками с современным интерфейсом.</p>
          </div>
          <div>
            <h3 class="font-semibold mb-3" style="color: #1a1a1a;">Навигация</h3>
            <ul class="text-sm space-y-1">
              <li><RouterLink to="/" class="text-sm transition-colors hover:underline" style="color: #FF5722;">Главная</RouterLink></li>
              <li><RouterLink to="/notes" class="text-sm transition-colors hover:underline" style="color: #FF5722;">Заметки</RouterLink></li>
              <li><RouterLink to="/about" class="text-sm transition-colors hover:underline" style="color: #FF5722;">О приложении</RouterLink></li>
            </ul>
          </div>
          <div>
            <h3 class="font-semibold mb-3" style="color: #1a1a1a;">Технологии</h3>
            <p class="text-sm" style="color: #999999;">Django REST Framework<br>Vue.js 3<br>Tailwind CSS</p>
          </div>
        </div>
        <hr style="border-color: #e0e0e0;" class="mb-6">
        <p class="text-center text-sm" style="color: #999999;">
          © 2025 SNotes. Все права защищены 🎨
        </p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.router-link-exact-active {
  color: #FF5722 !important;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.menu-enter-active, .menu-leave-active {
  transition: all 0.3s ease;
}

.menu-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.menu-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@media (max-width: 640px) {
  :deep(*) {
    scroll-behavior: smooth;
  }
}
</style>