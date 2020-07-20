from django.db import models
from driver.models import Driver
from datetime import datetime

# Create your models here.

# User Model
class User(models.Model):
	name = models.CharField(max_length=100,default='')
	current_x = models.PositiveIntegerField(default=0,null=False,blank=False)
	current_y = models.PositiveIntegerField(default=0,null=False,blank=False)
	craeted_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name


class Ride(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
	driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, null=False)
	start_x = models.PositiveIntegerField(default=0,null=False,blank=False)
	start_y = models.PositiveIntegerField(default=0,null=False,blank=False)
	end_x = models.PositiveIntegerField(default=0,null=False,blank=False)
	end_y = models.PositiveIntegerField(default=0,null=False,blank=False)
	complete = models.BooleanField(default=False)
	craeted_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.user.name



