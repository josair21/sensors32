from rest_framework import serializers
from .models import Devices

class DevicesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Devices
        fields = ('device', 'sensor_1', "sensor_2", "sensor_3")