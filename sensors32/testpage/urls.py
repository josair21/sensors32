from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("status", views.status, name="status"),
    path('devices', views.DevicesList.as_view(), name='devices-list'),
]