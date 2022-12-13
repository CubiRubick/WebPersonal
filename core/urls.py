from django.urls import path
from core import views

urlpatterns = [
    path('about/', views.about, name="about"),
]
