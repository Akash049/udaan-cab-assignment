from django.shortcuts import render
from .models import *
from driver.models import Driver
from rest_framework.views import APIView
from rest_framework.response import Response
import os, json
import math
from .serializers import *
# Create your views here.

SEARCH_DIST = 3

class RegisterUser(APIView):

	def post(self,request):
		# add name and curret location fof the user
		try:
			name = request.POST.get('name')
			x = request.POST.get('x')
			y = request.POST.get('y')
			user = User.objects.create(name=name,current_x=int(x),current_y=int(y))
			return Response({'status':True , result: user.pk })
		except Exception as e:
			return Response({'status':False,'result': repr(e)})

class ConnectDriver(APIView):

	def post(self,request):
		try:
			user = request.POST.get('user')
			x = request.POST.get('start_x')
			y = request.POST.get('start_y')
			end_x = request.POST.get('end_x')
			end_y = request.POST.get('end_y')

			user = User.objects.filter(pk=int(user))
			if not user.exists():
				return Response({'status':False,'error':'User Does Not Exists'})
			else:
				# Check for the driver available
				drivers = Driver.objects.filter(booked=False)
				min_dist = -1
				itr = 0
				available_driver = ""
				for driver in drivers:
					distance = math.sqrt( (driver.current_x - int(x))**2  + (driver.current_y - int(y))**2 )
					if distance <= SEARCH_DIST:
						if itr == 0:
							itr = 1
							min_dist = distance
							available_driver = driver
						else:
							if distance < min_dist:
								min_dist = distance
								available_driver = driver
				if min_dist == -1:
					return Response({'status':False,'result':'NO DRIVER AVAILABLE'})
				else:
					# Create a ride
					ride = Ride.objects.create(user=user[0],driver=available_driver,start_x=int(x),start_y=int(y),end_x=int(end_x),end_y=int(end_y))
					# Book the driver
					available_driver.booked = True
					available_driver.save()
					return Response({'status':True,'result':ride.pk})
		except Exception as e:
			return Response({'status':False,'result': repr(e)})


# Update rides to array
class FetchRides(APIView):
	
	def get(self,request):
		try:
			userId = request.GET.get('id')
			user = User.objects.filter(pk=int(userId))
			if not user.exists():
				return Response({'status':False,'result':'USER DOES NOT EXISTS'})
			else:
				user = user[0]
				rides = Ride.objects.filter(user=user)
				rides_array = RideSerializers(rides,many=True)
				return Response({'status':True,'result': rides})
		except Exception as e:
			return Response({'status':False,'result': repr(e)})











