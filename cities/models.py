from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"
        ordering = ['name']

    def __str__(self):
        return self.name 