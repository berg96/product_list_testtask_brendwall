from django.core.validators import MinValueValidator
from django.db import models

MAX_LENGTH = 255
MIN_VALUE_PRICE = 1


class Product(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH, verbose_name='Название'
    )
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(
        validators=[MinValueValidator(MIN_VALUE_PRICE)],
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name[:20]} ({self.price}) - {self.description[:20]}'
