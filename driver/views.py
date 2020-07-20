from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
import os, json
from user.models import Ride
# Create your views here.

class RegisterDriver(APIView):

	def post(self,request):
		# add name and curret location fof the user
		try:
			name = request.POST.get('name')
			x = request.POST.get('x')
			y = request.POST.get('y')
			driver = Driver.objects.create(name=name,current_x=int(x),current_y=int(y))
			return Response({'status':True,'result': driver.pk })
		except Exception as e:
			return Response({'status':False,'result': repr(e)})

class UpdateLocation(APIView):

	def post(self,request):
		try:
			user = request.POST.get('id')
			x = request.POST.get('x')
			y = request.POST.get('y')
			driver = Driver.objects.filter(pk=int(user))
			if not driver.exists():
				return Response({'status':False,'error': 'DRIVER DOES NOT EXISTS' })
			else:
				driver = driver[0]
				driver.current_x = int(x)
				driver.current_y = int(y)
				driver.save()
				return Response({'status':True,'result':'LOCATION UPDATED'})
		except Exception as e:
			return Response({'status':False,'result': repr(e)})

# Toi correct
class UpdateAvailability(APIView):

	def post(self,request):
		try:
			user = request.POST.get('id')
			available = request.POST.get('available')
			driver = Driver.objects.filter(pk=int(user))
			if not driver.exists():
				return Response({'status':False,'error': 'DRIVER DOES NOT EXISTS' })
			else:
				print(available)
				driver = driver[0]
				if int(available) == 0:
					driver.booked = True
					driver.save()
				elif int(available) == 1:
					driver.booked = False
					driver.save()
				return Response({'status':True,'result':'AVAILABILITY UPDATED'})
		except Exception as e:
			return Response({'status':False,'result': repr(e)})



class EndTrip(APIView):

	def get(self,request):
		try:
			user = request.GET.get('id')
			driver = Driver.objects.filter(pk=int(user))
			if not driver.exists():
				return Response({'status':False,'error': 'DRIVER DOES NOT EXISTS' })
			else:
				driver = driver[0]
				ride = Ride.objects.filter(driver=driver)
				if not ride.exists():
					return Response({'status':False,'result':'DRIVER DOES HAVE ANY RIDES'})
				else:
					ride = ride[0]
					# End the trip
					ride.complete = True
					ride.save()

					# Make the driver available to take ride
					driver.booked = False
					driver.save()
					return Response({'status':True,'result': 'TRIP ENDED'})
		except Exception as e:
			return Response({'status':False,'result': repr(e)})







