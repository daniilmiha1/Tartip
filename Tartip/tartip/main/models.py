from django.db import models

# Create your models here.
class FeedBack(models.Model):

    name = models.CharField(verbose_name='Имя',max_length=30,default='')
    email = models.EmailField('Почта')
    phone = models.CharField(verbose_name='Телефон',max_length=13,default='')
    message = models.TextField('Ваше сообщение или заказ')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class TartipCategory(models.Model):
    name = models.CharField(verbose_name='Тип продукции', max_length = 20)
    slug = models.SlugField('URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class Tartip(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=50)
    cat = models.ForeignKey('TartipCategory', on_delete=models.CASCADE, verbose_name='Тип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'


