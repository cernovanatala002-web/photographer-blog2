export default defineNuxtConfig({
  devtools: { enabled: true },

  // В css оставляем только локальные файлы (если style.css существует)
  css: [
    '~/assets/style.css'
  ],

  app: {
    head: {
      // Добавляем CDN-ссылку на Bootstrap в head.link
      link: [
        { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' }
      ],
      script: [
        { src: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js', tagPosition: 'bodyClose' }
      ]
    }
  },

  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000/api/'
    }
  }
})