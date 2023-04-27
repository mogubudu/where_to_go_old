from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        help_text=('Поставь галочку, если нужно опубликовать место.'),
        default=False
        )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              related_name='images')
    image = models.ImageField(verbose_name='Картинка')
    position = models.PositiveSmallIntegerField(verbose_name='Позиция')

    def __str__(self):
        return f'{self.position} {self.place}'
