from django.db import models

# Create your models here.

class Table(models.Model):
	SHAPES = ((1, 'rectangle'), (0, 'oval'))

	number = models.IntegerField(unique=True)
	chairs_count = models.IntegerField(default = 0)
	shape = models.IntegerField(choices = SHAPES, default = 'rectangle')
	width = models.FloatField(default = 0)
	height = models.FloatField(default = 0)
	pos_X = models.FloatField(default = 0)
	pos_y = models.FloatField(default = 0)
	booked = models.TextField(blank = True, default = "") # editable = False
	def __str__(self):
		return ("Table # "+str(self.number))