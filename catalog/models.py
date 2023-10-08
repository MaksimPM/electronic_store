from django.db import models
from django.contrib.auth import get_user_model

# from _datetime import datetime

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    # created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    product_pic = models.ImageField(upload_to='products', verbose_name='Изображение', **NULLABLE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_last_change = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contacts(models.Model):
    contact_name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Описание')
    preview = models.ImageField(verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} ({self.slug})'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Version(models.Model):
    product_version = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name_version = models.CharField(max_length=100, verbose_name='Наименование версии')
    number_version = models.IntegerField(verbose_name='Номер версии')
    active_version = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product_version} ({self.name_version}:{self.number_version})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
