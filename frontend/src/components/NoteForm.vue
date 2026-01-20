<!-- frontend/src/components/NoteForm.vue -->
<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useNotesStore } from '@/stores/notes'

const props = defineProps({
  mode: {
    type: String,
    default: 'create',
    validator: (value) => ['create', 'edit'].includes(value)
  }
})

const router = useRouter()
const route = useRoute()
const notesStore = useNotesStore()

const isEditMode = computed(() => props.mode === 'edit')
const pageTitle = computed(() => isEditMode.value ? 'Редактировать заметку' : 'Создать заметку')

const form = reactive({
  title: '',
  content: ''
})

const errors = ref({})
const saving = ref(false)

// Валидация
const validateForm = () => {
  errors.value = {}
  
  if (!form.title.trim()) {
    errors.value.title = 'Заголовок обязателен'
  } else if (form.title.length > 200) {
    errors.value.title = 'Заголовок не может быть длиннее 200 символов'
  }
  
  if (!form.content.trim()) {
    errors.value.content = 'Содержание обязательно'
  } else if (form.content.length > 10000) {
    errors.value.content = 'Содержание не может быть длиннее 10000 символов'
  }
  
  return Object.keys(errors.value).length === 0
}

// Загрузка существующей заметки для редактирования
onMounted(async () => {
  if (isEditMode.value) {
    const noteId = parseInt(route.params.id)
    try {
      const note = await notesStore.fetchNote(noteId)
      form.title = note.title
      form.content = note.content
    } catch (error) {
      console.error('Error loading note:', error)
      router.push('/notes')
    }
  }
})

// Сохранение заметки
const saveNote = async () => {
  if (!validateForm()) return
  
  saving.value = true
  
  try {
    const noteData = {
      title: form.title.trim(),
      content: form.content.trim()
    }
    
    if (isEditMode.value) {
      const noteId = parseInt(route.params.id)
      await notesStore.updateNote(noteId, noteData)
    } else {
      await notesStore.createNote(noteData)
    }
    
    router.push('/notes')
  } catch (error) {
    console.error('Error saving note:', error)
  } finally {
    saving.value = false
  }
}

// Отмена
const cancel = () => {
  router.push('/notes')
}

// Обработка изменений в форме для очистки ошибок
const clearFieldError = (field) => {
  if (errors.value[field]) {
    delete errors.value[field]
  }
}
</script>

<template>
  <div class="w-full min-h-screen p-6" style="background: linear-gradient(135deg, #f5f1ed 0%, #f0ebe7 100%);">
    <div class="max-w-3xl mx-auto">
      <!-- Header -->
      <div class="mb-8 flex items-center gap-4">
        <button
          @click="cancel"
          class="p-2 rounded-lg transition-all duration-300 hover:shadow-lg"
          style="background: white; color: #a67c52; border: 1px solid #e8ddd5;"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
        </button>
        <h1 class="text-4xl font-bold" style="color: #6b5844;">
          {{ pageTitle === 'Редактировать заметку' ? '✏️ Редактировать заметку' : '✍️ Создать заметку' }}
        </h1>
      </div>

      <!-- Form -->
      <form @submit.prevent="saveNote" class="space-y-6">
        <!-- Title Field -->
        <div>
          <label for="title" class="block text-sm font-semibold mb-2" style="color: #6b5844;">
            Заголовок *
          </label>
          <input
            id="title"
            v-model="form.title"
            @input="clearFieldError('title')"
            type="text"
            placeholder="Введите заголовок заметки..."
            class="w-full px-5 py-3 rounded-xl border-2 transition-all duration-300 font-medium"
            style="border-color: #e8ddd5; background: white; color: #3d3d3d;"
            @focus="$event.target.style.borderColor = '#a67c52'; $event.target.style.boxShadow = '0 0 0 3px rgba(166, 124, 82, 0.1)'"
            @blur="$event.target.style.borderColor = '#e8ddd5'; $event.target.style.boxShadow = 'none'"
            :style="{ borderColor: errors.title ? '#dc2626' : '#e8ddd5' }"
          />
          <div class="flex justify-between mt-2">
            <p v-if="errors.title" class="text-sm" style="color: #dc2626;">⚠️ {{ errors.title }}</p>
            <p class="text-sm ml-auto" style="color: #999999;">{{ form.title.length }}/200</p>
          </div>
        </div>

        <!-- Content Field -->
        <div>
          <label for="content" class="block text-sm font-semibold mb-2" style="color: #6b5844;">
            Содержание *
          </label>
          <textarea
            id="content"
            v-model="form.content"
            @input="clearFieldError('content')"
            rows="12"
            placeholder="Введите содержание заметки..."
            class="w-full px-5 py-3 rounded-xl border-2 transition-all duration-300 font-medium resize-none"
            style="border-color: #e8ddd5; background: white; color: #3d3d3d; font-family: 'Segoe UI', sans-serif;"
            @focus="$event.target.style.borderColor = '#a67c52'; $event.target.style.boxShadow = '0 0 0 3px rgba(166, 124, 82, 0.1)'"
            @blur="$event.target.style.borderColor = '#e8ddd5'; $event.target.style.boxShadow = 'none'"
            :style="{ borderColor: errors.content ? '#dc2626' : '#e8ddd5' }"
          ></textarea>
          <div class="flex justify-between mt-2">
            <p v-if="errors.content" class="text-sm" style="color: #dc2626;">⚠️ {{ errors.content }}</p>
            <p class="text-sm ml-auto" style="color: #999999;">{{ form.content.length }}/10000</p>
          </div>
        </div>

        <!-- Actions -->
        <div class="flex gap-4 pt-8">
          <button
            type="submit"
            :disabled="saving || notesStore.loading"
            class="flex-1 px-8 py-3 rounded-xl font-bold transition-all duration-300 flex items-center justify-center gap-2 shadow-lg hover:shadow-xl transform hover:scale-105 disabled:opacity-50"
            style="background: linear-gradient(135deg, #a67c52 0%, #8b6f47 100%); color: white;"
          >
            <svg 
              v-if="saving || notesStore.loading" 
              class="animate-spin h-5 w-5" 
              fill="none" 
              viewBox="0 0 24 24"
            >
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            {{ saving ? '⏳ Сохранение...' : (isEditMode ? '💾 Сохранить' : '✨ Создать') }}
          </button>
          
          <button
            type="button"
            @click="cancel"
            class="px-8 py-3 rounded-xl font-semibold transition-all duration-300 hover:shadow-lg"
            style="background: white; color: #999999; border: 2px solid #e8ddd5;"
          >
            Отмена
          </button>
        </div>
      </form>

      <!-- Preview Section -->
      <div v-if="form.content" class="mt-12 pt-8" style="border-top: 2px solid #e8ddd5;">
        <h3 class="text-2xl font-bold mb-6" style="color: #6b5844;">👁️ Предварительный просмотр</h3>
        <div class="rounded-xl p-8 shadow-lg" style="background: white; border: 1px solid #e8ddd5;">
          <h4 class="text-2xl font-bold mb-4" style="color: #6b5844;">
            {{ form.title || '(без заголовка)' }}
          </h4>
          <p class="whitespace-pre-wrap leading-relaxed text-base" style="color: #7a7a7a;">
            {{ form.content }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>