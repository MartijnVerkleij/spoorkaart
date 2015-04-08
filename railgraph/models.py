from django.db import models

# Create your models here.

class Station(models.Model):
	tel_code = models.CharField(max_length=10)
	name = models.CharField(max_length=150)
	location_lat = models.DecimalField(max_digits=13, decimal_places=10)
	location_lon = models.DecimalField(max_digits=13, decimal_places=10)
	tracks = models.IntegerField(default=1)
	
	tel_code.primary_key = True
	
	def __str__(self):
		return self.tel_code

class Track(models.Model):
	station_1 = models.ForeignKey(Station, related_name='station1')
	station_2 = models.ForeignKey(Station, related_name='station2')
	width = models.IntegerField(default=1)

	def __str__(self):
		return self.station_1.tel_code + ' ' + self.station_2.tel_code
