from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.home),
    path("hotellist", views.HotelList.as_view())
]