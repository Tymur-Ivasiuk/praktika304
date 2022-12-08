from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Section(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Назва')
    desc = models.CharField(max_length=255, blank=True, verbose_name='Опис')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото секції')

    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='SLUG')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'section_slug': self.slug})

    class Meta:
        verbose_name = 'Розділ'
        verbose_name_plural = "Розділи"

class Fonds(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Назва фонду')
    desc = models.TextField(verbose_name='Опис')
    url_global = models.CharField(max_length=1000, unique=True, verbose_name='URL-посилання')
    section_id = models.ForeignKey('Section', on_delete=models.CASCADE, verbose_name='Розділ')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')

    def get_absolute_url(self):
        return reverse('category', kwargs={'section_slug': self.section_id.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фонд'
        verbose_name_plural = "Фонди"

class Photos(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    fond_id = models.ForeignKey('Fonds', on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def image_tag(self):
        return mark_safe(f'<img src="{self.photo.url}" height="100" />')
    image_tag.short_description = 'Фото'

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

class Quotes(models.Model):
    desc = models.TextField(verbose_name='Цитата')
    author = models.CharField(max_length=255, verbose_name='Автор')
    section_id = models.ForeignKey('Section', on_delete=models.CASCADE)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = "Цитати"
