from django.db import models

# Create your models here.

class Pessoa(models.Model):
    name = models.CharField(max_length=100, default="Nome")
    idade = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    dono = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

