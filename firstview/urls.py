from .views import *
from django.urls import path

urlpatterns = [
    path('', inicio),
    path('padre/', padre),
    path('madre/', madre),
    path('hermana/', hermana),
]