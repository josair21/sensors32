from django.db import models

class Devices(models.Model):

    class Meta:

        db_table = 'devices'

    device = models.CharField(max_length=20, unique=True)
    sensor_1 = models.CharField(max_length=20)
    sensor_2 = models.CharField(max_length=20)
    sensor_3 = models.CharField(max_length=20)

    def __str__(self):
        return self.device