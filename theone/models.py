from django.db import models

class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return f"Point(x: {self.x}, y: {self.y})"


class PolarPoint(models.Model):
    radius = models.FloatField()
    angle = models.FloatField()
    cartesian_point = models.OneToOneField(Point, on_delete=models.CASCADE)

    def __str__(self):
        return f"Point(radius: {self.radius}, angle: {self.angle})"

class LocalStatus(models.Model):
    point = models.OneToOneField(Point, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"Status(temperature: {self.temperature}, humidity: {self.humidity})"
