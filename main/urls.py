from typing import List
from . import views
from django.urls import path
from .views import ListData

urlpatterns = [
    path('',views.index ),
    path('api/',ListData.as_view() ),
]