<template>
  <div class="w-full min-h-screen px-4 sm:px-6 lg:px-8 py-6 md:py-8" style="background: #f8f7f5;">
    <div class="max-w-4xl mx-auto">
      <div class="text-center mb-10 md:mb-16">
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-3 sm:mb-4" style="color: #1a1a1a;">ℹ️ О приложении</h1>
        <p class="text-sm sm:text-base md:text-lg" style="color: #999999;">Узнайте больше о SNotes</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6 md:gap-8">
        <div class="space-y-4 sm:space-y-6">
          <div class="rounded-2xl p-5 sm:p-6 md:p-8 shadow-lg" style="background: white; border: 1px solid #e0e0e0;">
            <h2 class="text-xl sm:text-2xl font-bold mb-3 sm:mb-4" style="color: #1a1a1a;">📱 Что это?</h2>
            <p style="color: #7a7a7a;" class="leading-relaxed text-xs sm:text-sm md:text-base">
              SNotes — это современное веб-приложение для управления заметками. Оно разработано с использованием самых современных технологий и предоставляет удобный интерфейс для создания, редактирования и организации ваших мыслей и идей.
            </p>
          </div>

          <div class="rounded-2xl p-5 sm:p-6 md:p-8 shadow-lg" style="background: white; border: 1px solid #e0e0e0;">
            <h2 class="text-xl sm:text-2xl font-bold mb-3 sm:mb-4" style="color: #1a1a1a;">🛠️ Технологии</h2>
            <div class="space-y-2 sm:space-y-3">
              <div class="flex items-center gap-3">
                <span style="color: #FF5722;" class="text-lg sm:text-xl flex-shrink-0">✓</span>
                <span style="color: #7a7a7a;" class="text-xs sm:text-sm md:text-base"><strong>Backend:</strong> Django REST Framework</span>
              </div>
              <div class="flex items-center gap-3">
                <span style="color: #FF5722;" class="text-lg sm:text-xl flex-shrink-0">✓</span>
                <span style="color: #7a7a7a;" class="text-xs sm:text-sm md:text-base"><strong>Frontend:</strong> Vue.js 3 + Vite</span>
              </div>
              <div class="flex items-center gap-3">
                <span style="color: #FF5722;" class="text-lg sm:text-xl flex-shrink-0">✓</span>
                <span style="color: #7a7a7a;" class="text-xs sm:text-sm md:text-base"><strong>Стили:</strong> Tailwind CSS</span>
              </div>
              <div class="flex items-center gap-3">
                <span style="color: #FF5722;" class="text-lg sm:text-xl flex-shrink-0">✓</span>
                <span style="color: #7a7a7a;" class="text-xs sm:text-sm md:text-base"><strong>База данных:</strong> SQLite/PostgreSQL</span>
              </div>
            </div>
          </div>

          <div class="rounded-2xl p-5 sm:p-6 md:p-8 shadow-lg" style="background: white; border: 1px solid #e0e0e0;">
            <h2 class="text-xl sm:text-2xl font-bold mb-3 sm:mb-4" style="color: #1a1a1a;">🎨 Дизайн</h2>
            <p style="color: #7a7a7a;" class="leading-relaxed mb-4 text-xs sm:text-sm md:text-base">
              Приложение разработано с использованием профессиональной цветовой палитры: оранжевый и темные цвета создают современный и стильный вид.
            </p>
            <div class="flex gap-2 sm:gap-3">
              <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-lg flex-shrink-0" style="background: white; border: 1px solid #e0e0e0;"></div>
              <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-lg flex-shrink-0" style="background: #f8f7f5; border: 1px solid #e0e0e0;"></div>
              <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-lg flex-shrink-0" style="background: #FF5722; border: 1px solid #FF5722;"></div>
            </div>
          </div>
        </div>

        <div class="space-y-4 sm:space-y-6">
          <div class="rounded-2xl p-5 sm:p-6 md:p-8 shadow-lg" style="background: #FF5722; border: 1px solid #FF5722; color: white;">
            <h2 class="text-xl sm:text-2xl font-bold mb-3 sm:mb-4">⭐ Особенности</h2>
            <ul class="space-y-2 sm:space-y-3">
              <li class="flex items-start gap-3">
                <span class="text-lg sm:text-xl flex-shrink-0">✨</span>
                <span class="text-xs sm:text-sm md:text-base">Быстрое создание и редактирование заметок</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-lg sm:text-xl flex-shrink-0">📱</span>
                <span class="text-xs sm:text-sm md:text-base">Адаптивный дизайн для всех устройств</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-lg sm:text-xl flex-shrink-0">🔒</span>
                <span class="text-xs sm:text-sm md:text-base">Безопасное хранение данных</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-lg sm:text-xl flex-shrink-0">⚡</span>
                <span class="text-xs sm:text-sm md:text-base">Молниеносная скорость работы</span>
              </li>
              <li class="flex items-start gap-3">
                <span class="text-lg sm:text-xl flex-shrink-0">🎯</span>
                <span class="text-xs sm:text-sm md:text-base">Интуитивный интерфейс</span>
              </li>
            </ul>
          </div>

          <div class="rounded-2xl p-5 sm:p-6 md:p-8 shadow-lg" style="background: white; border: 1px solid #e0e0e0;">
            <h2 class="text-xl sm:text-2xl font-bold mb-3 sm:mb-4" style="color: #1a1a1a;">👨‍💻 Разработка</h2>
            <p style="color: #7a7a7a;" class="leading-relaxed mb-4 text-xs sm:text-sm md:text-base">
              Это приложение создано как учебный проект для демонстрации лучших практик разработки современных веб-приложений.
            </p>
            <p style="color: #999999;" class="text-xs sm:text-sm">
              Версия 1.0 • 2025 • Все права защищены
            </p>
          </div>

          <div class="rounded-2xl p-5 sm:p-6 md:p-8 shadow-lg" style="background: white; border: 1px solid #e0e0e0;">
            <h2 class="text-xl sm:text-2xl font-bold mb-3 sm:mb-4" style="color: #1a1a1a;">📞 Контакты</h2>
            <p style="color: #7a7a7a;" class="leading-relaxed mb-4 text-xs sm:text-sm md:text-base">
              Если у вас есть вопросы или предложения по улучшению приложения, не стесняйтесь обращаться к разработчику.
            </p>
            <button class="px-3 sm:px-4 py-2 rounded-lg font-semibold transition-all duration-300 text-xs sm:text-sm text-white" style="background: #FF5722;">
              📧 Email
            </button>
          </div>
        </div>
      </div>

      <div class="text-center mt-10 md:mt-16 p-5 sm:p-6 md:p-8 rounded-2xl" style="background: white; border: 1px solid #e0e0e0;">
        <h3 class="text-lg sm:text-xl md:text-2xl font-bold mb-2 sm:mb-3" style="color: #1a1a1a;">Спасибо за использование SNotes! 💖</h3>
        <p style="color: #999999;" class="text-xs sm:text-sm md:text-base">Надеемся, что приложение помогает вам организовывать ваши мысли и идеи</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
