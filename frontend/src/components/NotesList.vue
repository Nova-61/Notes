<!-- frontend/src/components/NotesList.vue -->
<script setup>
import { onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useNotesStore } from '@/stores/notes'

const router = useRouter()
const notesStore = useNotesStore()

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
  <div class="w-full min-h-screen p-6" style="background: linear-gradient(135deg, #f5f1ed 0%, #f0ebe7 100%);">
    <!-- Header -->
    <div class="flex justify-between items-center mb-12 max-w-6xl mx-auto">
      <div>
        <h1 class="text-4xl font-bold" style="color: #6b5844;">📚 Мои заметки</h1>
        <p class="mt-2 text-lg" style="color: #a67c52;">
          Всего заметок: <span class="font-semibold">{{ notesStore.notesCount }}</span>
        </p>
      </div>
      <button
        @click="createNote"
        class="px-8 py-3 rounded-xl font-semibold transition-all duration-300 flex items-center gap-2 shadow-lg hover:shadow-xl transform hover:scale-105"
        style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); color: white;"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Создать заметку
      </button>
    </div>

    <!-- Error Message -->
    <div v-if="error" class="max-w-6xl mx-auto mb-6">
      <div class="bg-red-50 border-l-4 border-red-400 p-4 rounded-lg flex justify-between items-center">
        <span style="color: #8b6f47;">⚠️ {{ error }}</span>
        <button 
          @click="notesStore.clearError()"
          class="text-red-500 hover:text-red-700 text-2xl"
        >
          ×
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex justify-center py-24">
      <div class="text-center">
        <div class="w-16 h-16 rounded-full border-4 border-transparent mx-auto mb-4" style="border-top-color: #a67c52; border-right-color: #d4a574; animation: spin 1s linear infinite;"></div>
        <p style="color: #999999;" class="text-lg">Загрузка заметок...</p>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else-if="!loading && sortedNotes.length === 0" class="text-center py-24 max-w-2xl mx-auto">
      <div class="text-6xl mb-6">📝</div>
      <h3 class="text-2xl font-bold mb-3" style="color: #6b5844;">Пока нет заметок</h3>
      <p class="mb-8" style="color: #999999;">Создайте свою первую заметку, чтобы начать организовывать свои мысли.</p>
      <button
        @click="createNote"
        class="px-6 py-3 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl"
        style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); color: white;"
      >
        ✨ Создать первую заметку
      </button>
    </div>

    <!-- Notes Grid -->
    <div v-else class="max-w-6xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="note in sortedNotes"
          :key="note.id"
          class="group rounded-xl overflow-hidden transition-all duration-300 hover:shadow-2xl transform hover:scale-105 cursor-pointer"
          style="background: white; border: 1px solid #e8ddd5; box-shadow: 0 2px 8px rgba(167, 124, 82, 0.08);"
          @click="viewNote(note.id)"
        >
          <!-- Card Header -->
          <div class="p-6 pb-4">
            <h2 class="text-xl font-bold mb-2 line-clamp-2 group-hover:transition-colors" style="color: #6b5844;">
              {{ note.title }}
            </h2>
            <p class="text-sm mb-4 line-clamp-3" style="color: #999999;">
              {{ truncateContent(note.content) }}
            </p>
            <p class="text-xs" style="color: #d4a574;">
              {{ formatDate(note.created_at) }}
            </p>
          </div>

          <!-- Card Footer -->
          <div class="px-6 py-4 flex justify-end gap-3 border-t" style="border-color: #e8ddd5; background: #f5f1ed;">
            <button
              @click.stop="editNote(note.id)"
              class="px-4 py-2 rounded-lg text-sm font-medium transition-colors duration-300"
              style="background: rgba(166, 124, 82, 0.1); color: #a67c52;"
              @mouseenter="$event.target.style.background = 'rgba(166, 124, 82, 0.2)'"
              @mouseleave="$event.target.style.background = 'rgba(166, 124, 82, 0.1)'"
            >
              ✏️ Редактировать
            </button>
            <button
              @click.stop="deleteNote(note.id)"
              class="px-4 py-2 rounded-lg text-sm font-medium transition-colors duration-300"
              style="background: rgba(220, 38, 38, 0.1); color: #dc2626;"
              @mouseenter="$event.target.style.background = 'rgba(220, 38, 38, 0.2)'"
              @mouseleave="$event.target.style.background = 'rgba(220, 38, 38, 0.1)'"
            >
              🗑️ Удалить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>