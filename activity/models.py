from django.db import models

# Create your models here.


class Activity(models.Model):
	name 		=		models.CharField(max_length=120)
	distance   	=   	models.DecimalField(max_digits=10,decimal_places=1)
	location 	=		models.CharField(max_length=120)
	review 		=		models.IntegerField()

	def __str__(self):
		return self.name