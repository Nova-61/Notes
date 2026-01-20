<!-- frontend/src/App.vue -->
<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="min-h-screen flex flex-col" style="background-color: #f5f1ed;">
    <!-- Navigation -->
    <nav style="background: linear-gradient(135deg, #ffffff 0%, #f5f1ed 100%); box-shadow: 0 2px 8px rgba(167, 124, 82, 0.1); border-bottom: 1px solid #e8ddd5;">
      <div class="w-full px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo -->
          <div class="flex items-center">
            <RouterLink to="/" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
              <svg class="w-8 h-8" style="color: #a67c52;" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-5.04-6.71l-2.75 3.54-2.29-2.92c-.2-.26-.53-.4-.85-.4-.32 0-.65.14-.86.4l-2.29 2.92 4.15 5.29 4.15-5.29-2.75-3.54z"/>
              </svg>
              <span class="text-2xl font-bold" style="color: #6b5844;">SNotes</span>
            </RouterLink>
          </div>

          <!-- Navigation Links -->
          <div class="flex items-center space-x-8">
            <RouterLink 
              to="/" 
              class="px-3 py-2 rounded-lg text-sm font-medium transition-all duration-300"
              style="color: #7a7a7a;"
              :style="{ color: $route.path === '/' ? '#a67c52' : '#7a7a7a', backgroundColor: $route.path === '/' ? 'rgba(166, 124, 82, 0.1)' : 'transparent' }"
            >
              🏠 Главная
            </RouterLink>
            <RouterLink 
              to="/notes" 
              class="px-3 py-2 rounded-lg text-sm font-medium transition-all duration-300"
              style="color: #7a7a7a;"
              :style="{ color: $route.path.startsWith('/notes') ? '#a67c52' : '#7a7a7a', backgroundColor: $route.path.startsWith('/notes') ? 'rgba(166, 124, 82, 0.1)' : 'transparent' }"
            >
              📝 Заметки
            </RouterLink>
            <RouterLink 
              to="/about" 
              class="px-3 py-2 rounded-lg text-sm font-medium transition-all duration-300"
              style="color: #7a7a7a;"
              :style="{ color: $route.path === '/about' ? '#a67c52' : '#7a7a7a', backgroundColor: $route.path === '/about' ? 'rgba(166, 124, 82, 0.1)' : 'transparent' }"
            >
              ℹ️ О приложении
            </RouterLink>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-1 w-full">
      <RouterView />
    </main>

    <!-- Footer -->
    <footer style="background: linear-gradient(135deg, #ffffff 0%, #f5f1ed 100%); border-top: 1px solid #e8ddd5;" class="mt-auto">
      <div class="w-full py-8 px-4 sm:px-6 lg:px-8">
        <p class="text-center text-sm" style="color: #999999;">
          © 2025 SNotes. Создано с помощью Django REST Framework и Vue.js 🎨
        </p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.router-link-exact-active {
  color: #a67c52 !important;
}
</style>