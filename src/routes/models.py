from django.db import models
from django.core.exceptions import ValidationError


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Route name')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Total travel time')
    from_city = models.name = models.ForeignKey('cities.City', related_name='route_from_city_set',
                                                on_delete=models.CASCADE,
                                                verbose_name='From city'
                                                )
    to_city = models.name = models.ForeignKey('cities.City', related_name='route_to_city_set',
                                                on_delete=models.CASCADE,
                                                verbose_name='To city'
                                                )

    trains = models.ManyToManyField('trains.Train', verbose_name='Trains list')


    def __str__(self):
        return f'Route {self.name} from {self.from_city}'

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']
