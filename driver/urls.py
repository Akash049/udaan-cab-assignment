from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
	path('register/',RegisterDriver.as_view(),name="reg"),
	path('location_update/',UpdateLocation.as_view(),name="location_update"),
	path('availability_update/',UpdateAvailability.as_view(),name="availability_update"),
	path('end_trip/',EndTrip.as_view(),name="end_trip"),
]