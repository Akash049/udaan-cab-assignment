from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
	path('register/',RegisterUser.as_view(),name="reg"),
	path('connect_driver/',ConnectDriver.as_view(),name="connect_driver"),
	path('fetch_rides/',FetchRides.as_view(),name="fetch_rides")
]