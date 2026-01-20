<template>
  <div class="w-full min-h-screen p-6" style="background: linear-gradient(135deg, #f5f1ed 0%, #f0ebe7 100%);">
    <div class="max-w-4xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-16">
        <h1 class="text-5xl font-bold mb-4" style="color: #6b5844;">ℹ️ О приложении</h1>
        <p class="text-xl" style="color: #999999;">Узнайте больше о SNotes</p>
      </div>

      <!-- Main Content -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- Left Column -->
        <div class="space-y-6">
          <div class="rounded-2xl p-8 shadow-lg" style="background: white; border: 2px solid #e8ddd5;">
            <h2 class="text-2xl font-bold mb-4" style="color: #6b5844;">📱 Что это?</h2>
            <p style="color: #7a7a7a;" class="leading-relaxed">
              SNotes — это современное веб-приложение для управления заметками. Оно разработано с использованием самых современных технологий и предоставляет удобный интерфейс для создания, редактирования и организации ваших мыслей и идей.
            </p>
          </div>

          <div class="rounded-2xl p-8 shadow-lg" style="background: white; border: 2px solid #e8ddd5;">
            <h2 class="text-2xl font-bold mb-4" style="color: #6b5844;">🛠️ Технологии</h2>
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <span style="color: #a67c52;" class="text-xl">✓</span>
                <span style="color: #7a7a7a;"><strong>Backend:</strong> Django REST Framework</span>
              </div>
              <div class="flex items-center gap-3">
                <span style="color: #a67c52;" class="text-xl">✓</span>
                <span style="color: #7a7a7a;"><strong>Frontend:</strong> Vue.js 3 + Vite</span>
              </div>
              <div class="flex items-center gap-3">
                <span style="color: #a67c52;" class="text-xl">✓</span>
                <span style="color: #7a7a7a;"><strong>Стили:</strong> Tailwind CSS</span>
              </div>
              <div class="flex items-center gap-3">
                <span style="color: #a67c52;" class="text-xl">✓</span>
                <span style="color: #7a7a7a;"><strong>База данных:</strong> SQLite/PostgreSQL</span>
              </div>
            </div>
          </div>

          <div class="rounded-2xl p-8 shadow-lg" style="background: white; border: 2px solid #e8ddd5;">
            <h2 class="text-2xl font-bold mb-4" style="color: #6b5844;">🎨 Дизайн</h2>
            <p style="color: #7a7a7a;" class="leading-relaxed mb-4">
              Приложение разработано с использованием теплой и уютной цветовой палитры: белый, бежевый и коричневый цвета создают комфортную атмосферу для работы.
            </p>
            <div class="flex gap-3">
              <div class="w-16 h-16 rounded-lg" style="background: white; border: 2px solid #e8ddd5;"></div>
              <div class="w-16 h-16 rounded-lg" style="background: #f5f1ed; border: 2px solid #e8ddd5;"></div>
              <div class="w-16 h-16 rounded-lg" style="background: #a67c52; border: 2px solid #8b6f47;"></div>
            </div>
          </div>
        </div>

        <!-- Right Column -->
        <div class="space-y-6">
          <div class="rounded-2xl p-8 shadow-lg" style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); border: 2px solid #8b6f47; color: white;">
            <h2 class="text-2xl font-bold mb-4">⭐ Особенности</h2>
            <ul class="space-y-3">
              <li class="flex items-start gap-3">
                <span class="text-lg">✨</span>
                <span>Быстрое создание и редактирование заметок</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-lg">📱</span>
                <span>Адаптивный дизайн для всех устройств</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-lg">🔒</span>
                <span>Безопасное хранение данных</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-lg">⚡</span>
                <span>Молниеносная скорость работы</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-lg">🎯</span>
                <span>Интуитивный интерфейс</span>
              </li>
            </ul>
          </div>

          <div class="rounded-2xl p-8 shadow-lg" style="background: white; border: 2px solid #e8ddd5;">
            <h2 class="text-2xl font-bold mb-4" style="color: #6b5844;">👨‍💻 Разработка</h2>
            <p style="color: #7a7a7a;" class="leading-relaxed mb-4">
              Это приложение создано как учебный проект для демонстрации лучших практик разработки современных веб-приложений.
            </p>
            <p style="color: #999999;" class="text-sm">
              Версия 1.0 • 2025 • Все права защищены
            </p>
          </div>

          <div class="rounded-2xl p-8 shadow-lg" style="background: white; border: 2px solid #e8ddd5;">
            <h2 class="text-2xl font-bold mb-4" style="color: #6b5844;">📞 Контакты</h2>
            <p style="color: #7a7a7a;" class="leading-relaxed">
              Если у вас есть вопросы или предложения по улучшению приложения, не стесняйтесь обращаться к разработчику.
            </p>
            <div class="mt-4 flex gap-3">
              <button class="px-4 py-2 rounded-lg font-semibold transition-all duration-300" style="background: rgba(166, 124, 82, 0.1); color: #a67c52;">
                📧 Email
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="text-center mt-16 p-8 rounded-2xl" style="background: white; border: 2px solid #e8ddd5;">
        <h3 class="text-xl font-bold mb-2" style="color: #6b5844;">Спасибо за использование SNotes! 💖</h3>
        <p style="color: #999999;">Надеемся, что приложение помогает вам организовывать ваши мысли и идеи</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Additional styles if needed */
</style>
