from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'City name: {self.name}'


class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'Street name: {self.name}'


class Shop(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f'Shop name: {self.name}'
