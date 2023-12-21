from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=444, null=True)
    owner = models.CharField(max_length=333, null=True)
    type_of = models.CharField(max_length=123, null=True)
    seria = models.CharField(max_length=120, null=True)
    expire = models.CharField(max_length=123, null=True)
    price = models.CharField(max_length=123, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=123)
    telegram_id = models.CharField(max_length=123, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=233)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
