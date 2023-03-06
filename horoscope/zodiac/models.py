from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class ZodiacSigns(models.Model):
    sign_name = models.CharField(max_length=11)
    from_date = models.CharField(max_length=30)
    to_date = models.CharField(max_length=30)
    sign_image = models.ImageField(upload_to='images', null=True)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.sign_name}: {self.from_date}-{self.to_date}'


class SignHoroscope(models.Model):
    sign_horoscope = models.TextField()
    sign = models.ForeignKey(ZodiacSigns, on_delete=models.CASCADE)
    date = models.DateField()
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'Horoscope for {self.sign} on {self.date}'
#
