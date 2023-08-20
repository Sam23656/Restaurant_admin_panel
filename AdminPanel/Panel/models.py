from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Food(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
