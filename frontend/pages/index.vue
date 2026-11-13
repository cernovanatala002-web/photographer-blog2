<template>
  <div>
    <!-- НАВИГАЦИЯ (Бежевая шапка) -->
    <section class="my-navigation">
      <nav class="navbar navbar-expand-lg custom-navbar">
          <div class="container-fluid">
              <!-- Иконка и имя -->
              <a href="#" class="navbar-brand d-flex align-items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="#4facfe" class="bi bi-journal-bookmark-fill me-2" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M6 1h6v7a.5.5 0 0 1-.757.429L9 7.083 6.757 8.43A.5.5 0 0 1 6 8V1z"/>
                    <path d="M3 0h10a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm0 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H3z"/>
                  </svg>
                  <span class="fw-bold fs-4" style="color: #333;">Чернова Екатерина</span>
              </a>
              
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
                  <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <div class="navbar-nav me-auto mb-2 mb-lg-0 ms-4">
                      <a class="nav-link active" href="#">Главная</a>
                      <a class="nav-link" href="#">Контакты</a>
                  </div>
                  <form class="d-flex" role="search">
                      <input class="form-control me-2" type="search" placeholder="Поиск" aria-label="Поиск">
                      <button class="btn btn-outline-primary" type="submit">Найти</button>
                  </form>
            </div>
          </div>
      </nav>
    </section>

    <!-- КАРУСЕЛЬ (3 слайда) -->
    <section class="my-carousel">
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"></button>
        </div>
        <div class="carousel-inner">
          <!-- Первый слайд (с вашим представлением) -->
          <div class="carousel-item active">
            <img src="/img/first_img.jpg" class="d-block w-100" alt="Первая картинка">
            <div class="carousel-caption d-none d-md-block">
              <h5>Чернова Екатерина</h5>
              <p>Фотограф из Самары. Здесь вы можете увидеть мои работы.</p>
            </div>
          </div>
          <!-- Второй слайд -->
          <div class="carousel-item">
            <img src="/img/second_img.jpg" class="d-block w-100" alt="Вторая картинка">
            <div class="carousel-caption d-none d-md-block">
              <h5>Свежие новости</h5>
              <p>Узнайте первыми о новых статьях.</p>
            </div>
          </div>
          <!-- Третий слайд -->
          <div class="carousel-item">
            <img src="/img/third_img.jpg" class="d-block w-100" alt="Третья картинка">
            <div class="carousel-caption d-none d-md-block">
              <h5>Полезные материалы</h5>
              <p>Много интересного впереди.</p>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
          <span class="carousel-control-prev-icon"></span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
          <span class="carousel-control-next-icon"></span>
        </button>
      </div>
    </section>

    <!-- ДИНАМИЧЕСКИЕ ПОСТЫ -->
    <section class="all-posts">
      <div class="container">
        <h1 class="my-4">Мои работы</h1>
        
        <!-- Если постов нет, покажем сообщение -->
        <div v-if="posts.length === 0" class="text-center my-5">
          <p class="text-muted">Пока нет ни одной записи. Добавьте первую через админку!</p>
        </div>

        <div class="row">
            <!-- Цикл v-for перебирает посты, которые мы получили из Django -->
            <div class="col-md-4" v-for="post in posts" :key="post.id">
                <div class="card mb-4 shadow-sm h-100">
                    
                    <!-- Оборачиваем картинку в NuxtLink для перехода на страницу поста -->
                    <NuxtLink :to="`/post/${post.id}`">
                        <img :src="post.image ? post.image : '/img/first_img.jpg'" alt="" class="card-img-top">
                    </NuxtLink>
                    
                    <div class="card-body d-flex flex-column">
                        <h4 class="card-title">{{ post.title }}</h4>
                        <p class="card-text flex-grow-1">{{ post.content.substring(0, 100) }}...</p>
                        
                        <div class="d-flex justify-content-between align-items-center mt-3">
                            <div class="btn-group">
                                <!-- Кнопка также ведет на страницу поста -->
                                <NuxtLink :to="`/post/${post.id}`" class="btn btn-sm btn-outline-secondary">Читать →</NuxtLink>
                            </div>
                            <small class="text-muted fw-bold">
                                {{ new Date(post.created_at).toLocaleDateString('ru-RU') }}
                            </small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const posts = ref([])
const config = useRuntimeConfig()

onMounted(async () => {
  try {
    const response = await $fetch(`${config.public.apiBase}posts/`)
    posts.value = response
  } catch (error) {
    console.error("Ошибка загрузки постов. Проверьте, запущен ли Django:", error)
  }
})
</script>