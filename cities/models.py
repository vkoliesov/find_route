from django.db import models
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"
        ordering = ['name']

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('cities:city_detail', kwargs={"pk": self.id})
    