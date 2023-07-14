from django.db import models
from django.urls import reverse


class DiaryModel(models.Model):
    content = models.TextField(verbose_name='Текст')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)

    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return f'{self.time_create}'

    # def get_absolute_url(self):
    #     return reverse('diaries', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Заметка дневника'
        verbose_name_plural = 'Дневник'
        ordering = ['-time_create', 'id']


class NotesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Текст')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)

    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('notes', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-time_create', 'id']


class ContactUsModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Контент(проблемы)')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)

    is_published = models.BooleanField(verbose_name='Публикация', default=True)


    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('problems', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы'
        ordering = ['-time_create', 'id']

