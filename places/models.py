from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

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
