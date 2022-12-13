from django.urls import path
from porfolio import views as Pfolio

urlpatterns = [
    path('', Pfolio.portfolio, name="portfolio"),
]
