from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Zodiac(models.Model):
    aries = models.TextField()  # (Ram): #March 21–April 19
    taurus = models.TextField()  # (Bull): #April 20–May 20
    gemini = models.TextField()  # (Twins): #May 21–June 21
    cancer = models.TextField()  # (Crab): #June 22–July 22
    leo = models.TextField()  # (Lion): #July 23–August 22
    virgo = models.TextField()  # (Virgin): #August 23–September 22
    libra = models.TextField()  # (Balance): #September 23–October 23
    scorpius = models.TextField()  # (Scorpion): #October 24–November 21
    sagittarius = models.TextField()  # (Archer): #November 22–December 21
    capricornus = models.TextField()  # (Goat): #December 22–January 19
    aquarius = models.TextField()  # (Water Bearer): #January 20–February 18
    pisces = models.TextField()  # (Fish): February 19–March 20

    month = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ]
     )


    def __str__(self):
        return f''