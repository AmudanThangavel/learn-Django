from turtle import color
from django.db import models

# Create your models here.


class car_detail(models.Model):
    number = models.CharField(max_length=10)
    company = models.CharField(max_length=20)
    varient = models.CharField(max_length=20)
    model = models.IntegerField()
    owner = models.IntegerField()
    fuel = models.CharField(max_length=10)
    tyre = models.CharField(max_length=10)
    insurence = models.CharField(max_length=20)
    FC = models.DateField()
    colour = models.CharField(max_length=10)
    chase_number = models.CharField(max_length=20)
    engine_number = models.CharField(max_length=20)
    buy_price = models.IntegerField()

    def __str__(self):
        return f"model {self.number} {self.company}"


class learn(models.Model):
    competetion = models.CharField(max_length=20)
    collage = models.CharField(max_length=10)
    date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.competetion} {self.collage} {self.date}"
