from django.db import models
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = RichTextField(blank=True,verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name="Miniatura", upload_to='articles')
    public = models.BooleanField(verbose_name='Publicado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        #ordering = ['-id', 'created_at']
        #ordering = ['title']
        ordering = ['-id']

    def __str__(self):
        if self.public:
            publicado = '(publicado)'
        else:
            publicado = '(privado)'
        return f'{self.title} - {publicado}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


