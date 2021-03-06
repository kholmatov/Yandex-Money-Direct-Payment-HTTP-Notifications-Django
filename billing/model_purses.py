from django.db import models
from datetime import *

from commons.handler import Handle

class PursesManager(models.Manager):
	def Create(self, **kwargs):
		result = None
		# your code here
		return result

	def Get(self, **kwargs):
		result = None
		# your code here
		return result

	def Update(self, **kwargs):
		result = None
		# your code here
		return result
		
	def Reset(self, **kwargs):
		result = None
		# your code here
		return result
		
class Purses(models.Model):
	amount = models.FloatField(null = False, default = 0.00)
	date_lastupdated = models.DateTimeField(null = False, default=datetime.utcnow)
	# and your other fields to get purse consistent
	
	objects = PursesManager()

	def __unicode__(self):
		return self.id

	class Meta:
		db_table = "purses"
		ordering = ('id',)
