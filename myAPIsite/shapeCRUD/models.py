from django.db import models

# Create your models here.
from django.db import models
import numpy as np


class Triangle(models.Model):
    angle_1 = models.IntegerField(default=0)
    angle_2 = models.IntegerField(default=0)
    angle_3 = models.IntegerField(default=0)
    length_1 = models.IntegerField(default=0)
    length_2 = models.IntegerField(default=0)
    length_3 = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='triangles', on_delete=models.CASCADE)


    def __str__(self):
        return f"Triangle"

    def area(self):
        return 0.5 * np.sin(self.angle_3) * self.length_1 * self.length_2

    def perimeter(self):
        return self.length_1 + self.length_2 + self.length_3


class Rectangle(models.Model):
    length_1 = models.IntegerField(default=0)
    length_2 = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='rectangles', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rectangle with sides {self.length_1} and {self.length_2}"

    def area(self):
        return self.length_1 * self.length_2

    def perimeter(self):
        return (self.length_1 + self.length_2) * 2


class Square(models.Model):
    length_1 = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='squares', on_delete=models.CASCADE)

    def __str__(self):
        return f"Square with sides {self.length_1}"

    def area(self):
        return self.length_1 * self.length_1

    def perimeter(self):
        return self.length_1 * 4


class Diamond(models.Model):
    length_1 = models.IntegerField(default=0)
    length_2 = models.IntegerField(default=0)
    angle_1 = models.IntegerField(default=0)
    angle_2 = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='diamonds', on_delete=models.CASCADE)

    def __str__(self):
        return f"Diamond with sides {self.length_1} and {self.length_2}"

    def area(self):
        return np.sin(self.angle_1) * self.length_1 * self.length_2

    def perimeter(self):
        return (self.length_1 + self.length_2) * 2