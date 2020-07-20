from django.db import models

# Create your models here.
class Driver(models.Model):
	name = models.CharField(max_length=100,default='')
	current_x = models.PositiveIntegerField(default=0,null=False,blank=False)
	current_y = models.PositiveIntegerField(default=0,null=False,blank=False)
	booked = models.BooleanField(default=False)

	def __str__(self):
		return self.name