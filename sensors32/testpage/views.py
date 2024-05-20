from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Devices
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import DevicesSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


def index(request):
    print(request)
    return render(request, "index.html")


def status(request):
    if request.method == "GET":
        return JsonResponse({"value": "bueno"})
    if request.method == "POST":
        print(request.body)


@csrf_exempt
def devices(request):
    if request.method == "GET":
        devices = Devices.objects.all()
        devices_json = serializers.serialize("json", devices)
        return JsonResponse(devices_json, safe=False)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        device = data.get("device", "")
        sensor_1 = data.get("sensor_1", "")
        sensor_2 = data.get("sensor_2", "")
        sensor_3 = data.get("sensor_3", "")
        response_data = {
            "device": device,
            "sensor_1": sensor_1,
            "sensor_2": sensor_2,
            "sensor_3": sensor_3,
        }

        if device == "":
            return JsonResponse({"error": "No device defined"}, status=400)

        query = Devices.objects.filter(device=device).first()

        if query is None:
            new_device = Devices()
            new_device.device = device
            new_device.sensor_1 = sensor_1
            new_device.sensor_2 = sensor_2
            new_device.sensor_3 = sensor_3
            new_device.save()
            return JsonResponse(response_data, status=200)

        else:
            query.sensor_1 = sensor_1
            query.sensor_2 = sensor_2
            query.sensor_3 = sensor_3
            query.save()
            return JsonResponse(response_data, status=200)

    return JsonResponse({"Hola": "mundo"})
