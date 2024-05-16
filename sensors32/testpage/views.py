from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Devices
from rest_framework import generics
from .serializers import DevicesSerializer
from django.shortcuts import render


def index(request):
    print(request)
    return render(request, 'index.html')

def status(request):
    if request.method == "GET":
        return JsonResponse({"value": "bueno"})
    if request.method == "POST":
        print(request.body)

class DevicesList(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer