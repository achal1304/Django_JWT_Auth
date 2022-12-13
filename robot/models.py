from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class RobotCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Robot(models.Model):
    CURRENCY_CHOICES = (
        ('INR', 'Indian Rupee'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    )

    name = models.CharField(max_length=150, unique=True)
    robot_category = models.ForeignKey(
        RobotCategory,
        related_name = 'robot',
        on_delete = models.CASCADE
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name = 'robot',
        on_delete = models.CASCADE
    )
    currency = models.CharField(
        max_length = 3,
        choices = CURRENCY_CHOICES,
        default = 'INR'
    )
    manufacturing_date = models.DateTimeField()
    price = models.IntegerField(default=0, validators=[MinValueValidator(1)])

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



