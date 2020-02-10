from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'', profiles, name="profiles"),
    path('user/<pk>', profile, name="profile"),
    path('', include('pwa.urls')),
]
