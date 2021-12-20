from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Train number')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='from_city_set', verbose_name='From city')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='to_city_set', verbose_name='To city')


    class Meta:
        verbose_name = "train"
        verbose_name_plural = "trains"
        ordering = ['travel_time']



    def __str__(self):
        return f'Train {self.name} from {self.from_city}'

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('You should change "To city" field')
        qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city,
                                    travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('You should change "Travel time" field')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)