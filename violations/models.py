from django.db import models
from vehicles.models import Vehicle
from officers.models import Officer

# Create your models here.


class Violation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.license_plate} - {self.timestamp}"
