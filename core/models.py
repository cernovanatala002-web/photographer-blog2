from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст поста")
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Картинка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"