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
  <div class="w-full min-h-screen px-4 sm:px-6 lg:px-8 py-6 md:py-8 relative overflow-hidden" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%); background-size: 400% 400%; animation: gradientShift 15s ease infinite;">
    <div class="max-w-3xl mx-auto relative z-10">
      <div v-if="notesStore.loading" class="flex justify-center py-24">
        <div class="text-center">
          <div class="w-12 h-12 md:w-16 md:h-16 rounded-full border-4 border-transparent mx-auto mb-4" style="border-top-color: #FF5722; border-right-color: #FF7043; animation: spin 1s linear infinite;"></div>
          <p style="color: white;" class="text-base md:text-lg font-semibold">Загрузка заметки...</p>
        </div>
      </div>

      <div v-else-if="notesStore.error" class="text-center py-24">
        <div class="bg-red-50 border-l-4 border-red-400 p-4 sm:p-6 rounded-lg mb-6 backdrop-blur-sm" style="background: rgba(255, 255, 255, 0.95);">
          <p style="color: #dc2626;" class="text-sm sm:text-base">⚠️ {{ notesStore.error }}</p>
        </div>
        <button
          @click="goBack"
          class="px-6 py-3 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl text-sm sm:text-base text-white"
          style="background: #FF5722;"
        >
          Вернуться к списку
        </button>
      </div>

      <div v-else-if="notesStore.currentNote" class="space-y-4 md:space-y-6">
        <div class="flex flex-col gap-4">
          <div class="flex items-start gap-2 sm:gap-4">
            <button
              @click="goBack"
              class="p-2 rounded-lg transition-all duration-300 hover:shadow-lg flex-shrink-0 backdrop-blur-sm"
              style="background: rgba(255, 255, 255, 0.95); color: #FF5722; border: 1px solid rgba(255, 255, 255, 0.3);"
            >
              <svg class="w-5 h-5 sm:w-6 sm:h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
              </svg>
            </button>
            <h1 class="text-2xl sm:text-3xl md:text-4xl font-bold backdrop-blur-sm" style="color: white; text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);">
              📖 {{ notesStore.currentNote.title }}
            </h1>
          </div>
          
          <div class="flex flex-col sm:flex-row gap-3">
            <button
              @click="editNote"
              class="px-4 sm:px-6 py-2.5 sm:py-3 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105 flex items-center justify-center gap-2 text-sm sm:text-base flex-1 sm:flex-initial text-white backdrop-blur-sm"
              style="background: #FF5722;"
            >
              <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
              <span class="hidden sm:inline">Редактировать</span>
              <span class="sm:hidden">Редакт.</span>
            </button>
            
            <button
              @click="deleteNote"
              class="px-4 sm:px-6 py-2.5 sm:py-3 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105 text-sm sm:text-base flex-1 sm:flex-initial backdrop-blur-sm"
              style="background: rgba(220, 38, 38, 0.2); color: white; border: 2px solid rgba(220, 38, 38, 0.4);"
            >
              🗑️ <span class="hidden sm:inline">Удалить</span>
            </button>
          </div>
        </div>

        <div class="rounded-xl p-4 sm:p-6 backdrop-blur-md" style="background: rgba(255, 255, 255, 0.95); border: 1px solid rgba(255, 255, 255, 0.3);">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 text-xs sm:text-sm">
            <div>
              <span class="font-semibold block mb-1.5" style="color: #1a1a1a;">Создано:</span>
              <p style="color: #999999;">{{ formatDate(notesStore.currentNote.created_at) }}</p>
            </div>
            <div v-if="notesStore.currentNote.updated_at !== notesStore.currentNote.created_at">
              <span class="font-semibold block mb-1.5" style="color: #1a1a1a;">Последнее изменение:</span>
              <p style="color: #999999;">{{ formatDate(notesStore.currentNote.updated_at) }}</p>
            </div>
          </div>
        </div>

        <div class="rounded-xl shadow-lg p-5 sm:p-8 md:p-10 backdrop-blur-md" style="background: rgba(255, 255, 255, 0.95); border: 1px solid rgba(255, 255, 255, 0.3);">
          <div class="whitespace-pre-wrap leading-relaxed text-sm sm:text-base md:text-lg" style="color: #7a7a7a;">
            {{ notesStore.currentNote.content }}
          </div>
        </div>
      </div>

      <div v-else class="text-center py-20 md:py-32">
        <div class="text-5xl md:text-6xl mb-6">📭</div>
        <h3 class="text-xl md:text-2xl font-bold mb-3 backdrop-blur-sm" style="color: white; text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);">Заметка не найдена</h3>
        <p class="mb-8 text-sm md:text-base backdrop-blur-sm" style="color: rgba(255, 255, 255, 0.9);">Запрашиваемая заметка не существует или была удалена.</p>
        <button
          @click="goBack"
          class="px-6 py-3 rounded-xl font-semibold transition-all duration-300 shadow-lg hover:shadow-xl text-sm sm:text-base text-white"
          style="background: #FF5722;"
        >
          Вернуться к списку
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>