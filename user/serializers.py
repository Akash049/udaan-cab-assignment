from rest_framework import serializers
from .models import *

class RideSerializers(serializers.Serializer):
	class Meta:
		model = Ride
		fields = ['id','driver','start_x','start_y','end_x','end_y','craeted_on']