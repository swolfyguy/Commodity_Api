from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Element(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)


class Commodity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    inventory = models.IntegerField()
    price = models.IntegerField()
    chemical_composition = models.ManyToManyField(
        "Element", through="Composition", related_name="commodities"
    )


class Composition(models.Model):
    element_id = models.ForeignKey("Element", on_delete=models.SET_NULL, null=True)
    commodity_id = models.ForeignKey("Commodity", on_delete=models.SET_NULL, null=True)
    percentage = models.FloatField(validators=[MaxValueValidator(100)], null=False)
