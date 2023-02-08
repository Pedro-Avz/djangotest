from django.contrib import admin
from django.urls import path

from teste.views import current_datetime

urlpatterns = [
    path('now/', current_datetime),
]