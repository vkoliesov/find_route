from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Route name')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Total travel time')
    from_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='route_from_city_set', verbose_name='From city')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name='To city')
    trains = models.ManyToManyField('trains.Train', verbose_name='Trains list')


    class Meta:
        verbose_name = "route"
        verbose_name_plural = "routes"
        ordering = ['travel_times']



    def __str__(self):
        return f'Route {self.name} from {self.from_city}'

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('You should change "To city" field')
        qs = Route.objects.filter(from_city=self.from_city, to_city=self.to_city,
                                    travel_times=self.travel_times).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('You should change "Travel time" field')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)