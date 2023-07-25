from django.db import models
from .base_model import AppBaseModel

# Create your models here.
class DeviceInfo(AppBaseModel):
    device_fk_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    time_stamp = models.DateTimeField()
    speed = models.PositiveIntegerField()

