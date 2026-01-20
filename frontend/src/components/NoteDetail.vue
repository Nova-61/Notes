<!-- frontend/src/components/NoteDetail.vue -->
<script setup>
import { onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useNotesStore } from '@/stores/notes'

const router = useRouter()
const route = useRoute()
const notesStore = useNotesStore()

const noteId = computed(() => parseInt(route.params.id))

onMounted(() => {
  if (noteId.value) {
    notesStore.fetchNote(noteId.value)
  }
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

const goBack = () => {
  router.push('/notes')
}

const editNote = () => {
  router.push(`/notes/${noteId.value}/edit`)
}

const deleteNote = async () => {
  if (confirm('Вы уверены, что хотите удалить эту заметку?')) {
    try {
      await notesStore.deleteNote(noteId.value)
      router.push('/notes')
    } catch (error) {
      console.error('Error deleting note:', error)
    }
  }
}
</script>

<template>
  <div class="w-full min-h-screen p-6" style="background: linear-gradient(135deg, #f5f1ed 0%, #f0ebe7 100%);">
    <div class="max-w-3xl mx-auto">
      <!-- Loading State -->
      <div v-if="notesStore.loading" class="flex justify-center py-24">
        <div class="text-center">
          <div class="w-16 h-16 rounded-full border-4 border-transparent mx-auto mb-4" style="border-top-color: #a67c52; border-right-color: #d4a574; animation: spin 1s linear infinite;"></div>
          <p style="color: #999999;" class="text-lg">Загрузка заметки...</p>
        </div>
      </div>

      <!-- Error State -->
      <div v-else-if="notesStore.error" class="text-center py-24">
        <div class="bg-red-50 border-l-4 border-red-400 p-6 rounded-lg mb-6">
          <p style="color: #8b6f47;">⚠️ {{ notesStore.error }}</p>
        </div>
        <button
          @click="goBack"
          class="px-6 py-3 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl"
          style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); color: white;"
        >
          Вернуться к списку
        </button>
      </div>

      <!-- Note Content -->
      <div v-else-if="notesStore.currentNote" class="space-y-6">
        <!-- Header with Actions -->
        <div class="flex items-start justify-between gap-4">
          <div class="flex items-center gap-4">
            <button
              @click="goBack"
              class="p-2 rounded-lg transition-all duration-300 hover:shadow-lg"
              style="background: white; color: #a67c52; border: 1px solid #e8ddd5;"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
              </svg>
            </button>
            <h1 class="text-4xl font-bold" style="color: #6b5844;">
              📖 {{ notesStore.currentNote.title }}
            </h1>
          </div>
          
          <div class="flex gap-3">
            <button
              @click="editNote"
              class="px-6 py-2 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105 flex items-center gap-2"
              style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); color: white;"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
              Редактировать
            </button>
            
            <button
              @click="deleteNote"
              class="px-6 py-2 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105"
              style="background: rgba(220, 38, 38, 0.1); color: #dc2626; border: 2px solid rgba(220, 38, 38, 0.2);"
            >
              🗑️ Удалить
            </button>
          </div>
        </div>

        <!-- Note Meta Information -->
        <div class="rounded-xl p-6" style="background: white; border: 2px solid #e8ddd5;">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
            <div>
              <span class="font-semibold block mb-2" style="color: #6b5844;">Создано:</span>
              <p style="color: #999999;">{{ formatDate(notesStore.currentNote.created_at) }}</p>
            </div>
            <div v-if="notesStore.currentNote.updated_at !== notesStore.currentNote.created_at">
              <span class="font-semibold block mb-2" style="color: #6b5844;">Последнее изменение:</span>
              <p style="color: #999999;">{{ formatDate(notesStore.currentNote.updated_at) }}</p>
            </div>
          </div>
        </div>

        <!-- Note Content -->
        <div class="rounded-xl shadow-lg p-10" style="background: white; border: 2px solid #e8ddd5;">
          <div class="whitespace-pre-wrap leading-relaxed text-lg" style="color: #7a7a7a;">
            {{ notesStore.currentNote.content }}
          </div>
        </div>
      </div>

      <!-- Not Found State -->
      <div v-else class="text-center py-24">
        <div class="text-6xl mb-6">📭</div>
        <h3 class="text-2xl font-bold mb-3" style="color: #6b5844;">Заметка не найдена</h3>
        <p class="mb-8" style="color: #999999;">Запрашиваемая заметка не существует или была удалена.</p>
        <button
          @click="goBack"
          class="px-8 py-3 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl"
          style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); color: white;"
        >
          Вернуться к списку
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>