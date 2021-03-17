from django.db import models

# Create your models here.

class Feet(models.Model):
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)


class Leg(models.Model):
    feet = models.ForeignKey(Feet, on_delete=models.CASCADE, null=True)


class Table(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class TableLeg(models.Model):
   leg = models.ForeignKey(Leg, on_delete=models.PROTECT, null=True)
   table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)

   class Meta:
       unique_together = ("leg", "table")