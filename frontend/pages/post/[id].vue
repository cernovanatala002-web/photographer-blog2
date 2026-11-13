<template>
  <div>
    <!-- Шапка (можно скопировать из index.vue для единообразия) -->
    <section class="my-navigation">
      <nav class="navbar navbar-expand-lg custom-navbar">
          <div class="container-fluid">
              <NuxtLink to="/" class="navbar-brand d-flex align-items-center text-decoration-none">
                  <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="#4facfe" class="bi bi-journal-bookmark-fill me-2" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M6 1h6v7a.5.5 0 0 1-.757.429L9 7.083 6.757 8.43A.5.5 0 0 1 6 8V1z"/>
                    <path d="M3 0h10a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm0 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H3z"/>
                  </svg>
                  <span class="fw-bold fs-4" style="color: #333;">Чернова Екатерина</span>
              </NuxtLink>
          </div>
      </nav>
    </section>

    <!-- Основной контент поста -->
    <div class="container my-5" v-if="post">
      <div class="row justify-content-center">
        <div class="col-lg-8">
          <!-- Кнопка назад -->
          <NuxtLink to="/" class="btn btn-outline-secondary mb-4">← Назад к работам</NuxtLink>
          
          <!-- Заголовок и дата -->
          <h1 class="display-4 fw-bold mb-3">{{ post.title }}</h1>
          <p class="text-muted mb-4">Опубликовано: {{ new Date(post.created_at).toLocaleDateString('ru-RU') }}</p>
          
          <!-- Картинка поста (если есть) -->
          <img v-if="post.image" :src="post.image" class="img-fluid rounded mb-4 w-100 shadow" style="max-height: 600px; object-fit: cover;" alt="Картинка поста">
          
          <!-- Полный текст -->
          <div class="post-content fs-5" style="white-space: pre-wrap; line-height: 1.8;">
            {{ post.content }}
          </div>
        </div>
      </div>
    </div>
    
    <!-- Показываем загрузку, пока данные не пришли -->
    <div v-else class="container text-center my-5 py-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Загрузка...</span>
      </div>
      <p class="mt-3 text-muted">Загрузка работы...</p>
    </div>
  </div>
</template>

<script setup>
const route = useRoute()
const config = useRuntimeConfig()

// Получаем ID поста из адресной строки
const postId = route.params.id

// Запрашиваем конкретный пост у Django
const { data: post, error } = await useFetch(`${config.public.apiBase}posts/${postId}/`)

if (error.value) {
  console.error("Ошибка загрузки поста", error.value)
}
</script>