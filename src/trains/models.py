from django.db import models
from django.core.exceptions import ValidationError


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Train number')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.name = models.ForeignKey('cities.City', related_name='from_city_set',
                                                on_delete=models.CASCADE,
                                                verbose_name='From city'
                                                )
    to_city = models.name = models.ForeignKey('cities.City', related_name='to_city_set',
                                                on_delete=models.CASCADE,
                                                verbose_name='To city'
                                                )


    def __str__(self):
        return f'Train №{self.name} from {self.from_city}'

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['travel_time']

    
    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Change arrive city')
        qs = Train.objects.filter(
            from_city=self.from_city, to_city=self.to_city,
            travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Change travel time')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)