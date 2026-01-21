<script setup>
import { onMounted, computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useNotesStore } from '@/stores/notes'

const router = useRouter()
const notesStore = useNotesStore()
const searchQuery = ref('')

const { notes, loading, error, sortedNotes } = notesStore

onMounted(() => {
  notesStore.fetchNotes()
})

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const truncateContent = (content, maxLength = 150) => {
  if (content.length <= maxLength) return content
  return content.slice(0, maxLength) + '...'
}

const filteredNotes = computed(() => {
  if (!searchQuery.value.trim()) return sortedNotes
  return sortedNotes.filter(note => 
    note.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    note.content.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

const viewNote = (id) => {
  router.push(`/notes/${id}`)
}

const editNote = (id) => {
  router.push(`/notes/${id}/edit`)
}

const createNote = () => {
  router.push('/notes/create')
}

const deleteNote = async (id) => {
  if (confirm('Вы уверены, что хотите удалить эту заметку?')) {
    try {
      await notesStore.deleteNote(id)
    } catch (error) {
      console.error('Error deleting note:', error)
    }
  }
}
</script>

<template>
  <div class="w-full min-h-screen px-4 sm:px-6 lg:px-8 py-6 md:py-8" style="background: #f8f7f5;">
    <div class="max-w-6xl mx-auto">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8 md:mb-12">
        <div>
          <h1 class="text-3xl sm:text-4xl font-bold" style="color: #1a1a1a;">📚 Мои заметки</h1>
          <p class="mt-2 text-sm sm:text-lg" style="color: #FF5722;">
            Всего заметок: <span class="font-semibold">{{ notesStore.notesCount }}</span>
          </p>
        </div>
        <button
          @click="createNote"
          class="w-full sm:w-auto px-6 sm:px-8 py-3 rounded-xl font-semibold transition-all duration-300 flex items-center justify-center gap-2 shadow-lg hover:shadow-xl transform hover:scale-105 text-white"
          style="background: #FF5722;"
        >
          <svg class="w-5 h-5 sm:w-6 sm:h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          <span class="hidden sm:inline">Создать заметку</span>
          <span class="sm:hidden">Создать</span>
        </button>
      </div>

      <div class="mb-8 md:mb-10">
        <div class="relative">
          <svg class="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="color: #FF5722;">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск заметок..."
            class="w-full pl-12 pr-4 py-3 rounded-xl border-2 transition-all duration-300 text-sm sm:text-base"
            style="border-color: #e0e0e0; background: white; color: #1a1a1a;"
            @focus="$event.target.style.borderColor = '#FF5722'"
            @blur="$event.target.style.borderColor = '#e0e0e0'"
          />
        </div>
      </div>

      <div v-if="error" class="mb-6 animate-fadeIn">
        <div class="bg-red-50 border-l-4 border-red-400 p-4 rounded-lg flex justify-between items-center">
          <span style="color: #8b6f47;">⚠️ {{ error }}</span>
          <button 
            @click="notesStore.clearError()"
            class="text-red-500 hover:text-red-700 text-2xl font-bold"
          >
            ×
          </button>
        </div>
      </div>

      <div v-if="loading" class="flex justify-center py-20 md:py-32">
        <div class="text-center">
          <div class="w-12 h-12 md:w-16 md:h-16 rounded-full border-4 border-transparent mx-auto mb-4" style="border-top-color: #FF5722; border-right-color: #FF7043; animation: spin 1s linear infinite;"></div>
          <p style="color: #999999;" class="text-base md:text-lg">Загрузка заметок...</p>
        </div>
      </div>

      <div v-else-if="!loading && filteredNotes.length === 0" class="text-center py-20 md:py-32">
        <div class="text-5xl md:text-6xl mb-6">📝</div>
        <h3 class="text-xl md:text-2xl font-bold mb-3" style="color: #1a1a1a;">
          {{ searchQuery ? 'Заметки не найдены' : 'Пока нет заметок' }}
        </h3>
        <p class="mb-8 text-sm md:text-base" style="color: #999999;">
          {{ searchQuery ? 'Попробуйте изменить поисковый запрос' : 'Создайте свою первую заметку, чтобы начать организовывать свои мысли.' }}
        </p>
        <button
          v-if="!searchQuery"
          @click="createNote"
          class="px-6 py-3 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl text-white"
          style="background: #FF5722;"
        >
          ✨ Создать первую заметку
        </button>
      </div>

      <div v-else>
        <p class="mb-6 text-sm md:text-base" style="color: #FF5722;">
          Найдено заметок: <span class="font-semibold">{{ filteredNotes.length }}</span>
        </p>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-5 md:gap-6">
          <transition-group name="list" appear>
            <div
              v-for="note in filteredNotes"
              :key="note.id"
              class="group rounded-xl overflow-hidden transition-all duration-300 hover:shadow-2xl transform hover:scale-105 cursor-pointer"
              style="background: white; border: 1px solid #e0e0e0; box-shadow: 0 4px 12px rgba(255, 87, 34, 0.05);"
              @click="viewNote(note.id)"
            >
              <div class="p-5 sm:p-6 pb-4">
                <h2 class="text-lg sm:text-xl font-bold mb-2 line-clamp-2 group-hover:transition-colors" style="color: #1a1a1a;">
                  {{ note.title }}
                </h2>
                <p class="text-xs sm:text-sm mb-4 line-clamp-3" style="color: #999999;">
                  {{ truncateContent(note.content) }}
                </p>
                <p class="text-xs" style="color: #FF5722;">
                  {{ formatDate(note.created_at) }}
                </p>
              </div>

              <div class="px-5 sm:px-6 py-3 sm:py-4 flex flex-col sm:flex-row justify-between gap-2 border-t" style="border-color: #e0e0e0; background: #fafafa;">
                <button
                  @click.stop="editNote(note.id)"
                  class="px-3 sm:px-4 py-2 rounded-lg text-xs sm:text-sm font-medium transition-all duration-300 flex-1 sm:flex-initial"
                  style="background: rgba(255, 87, 34, 0.1); color: #FF5722;"
                  @mouseenter="$event.target.style.background = 'rgba(255, 87, 34, 0.2)'"
                  @mouseleave="$event.target.style.background = 'rgba(255, 87, 34, 0.1)'"
                >
                  ✏️ <span class="hidden sm:inline">Редактировать</span>
                </button>
                <button
                  @click.stop="deleteNote(note.id)"
                  class="px-3 sm:px-4 py-2 rounded-lg text-xs sm:text-sm font-medium transition-all duration-300 flex-1 sm:flex-initial"
                  style="background: rgba(220, 38, 38, 0.1); color: #dc2626;"
                  @mouseenter="$event.target.style.background = 'rgba(220, 38, 38, 0.2)'"
                  @mouseleave="$event.target.style.background = 'rgba(220, 38, 38, 0.1)'"
                >
                  🗑️ <span class="hidden sm:inline">Удалить</span>
                </button>
              </div>
            </div>
          </transition-group>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 0.3s ease-out;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.3s ease;
}

.list-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.list-leave-to {
  opacity: 0;
  transform: scale(0.95);
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>