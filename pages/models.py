from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Modelo para representar uma página ou postagem do blog
class Page(models.Model):
    title = models.CharField(max_length=200)  # Título da página
    subtitle = models.CharField(max_length=200)  # Subtítulo da página
    content = RichTextField()  # Conteúdo rico com suporte a formatação
    image = models.ImageField(upload_to='pages/images/')  # Imagem obrigatória da página
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação automática
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor da página

    def __str__(self):
        return self.title  # Representação em string do objeto