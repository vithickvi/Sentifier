from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class trends(models.Model):
	trend1 = models.CharField(max_length=30,blank=True)
	trend2 = models.CharField(max_length=30,blank=True)
	trend3 = models.CharField(max_length=30,blank=True)
	trend4 = models.CharField(max_length=30,blank=True)
	trend5 = models.CharField(max_length=30,blank=True)
	count1 = models.CharField(max_length=30,blank=True)
	count2 = models.CharField(max_length=30,blank=True)
	count3 = models.CharField(max_length=30,blank=True)
	count4 = models.CharField(max_length=30,blank=True)
	count5 = models.CharField(max_length=30,blank=True)
	ctry = models.CharField(max_length=30,blank=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)



class tweethist(models.Model):
	# searchid = models.ForeignKey('trends')
	searchreq= models.CharField(max_length=30,blank=True)
	tweet = models.CharField(max_length=30,blank=True)
	status = models.CharField(max_length=30,blank=True)
	maxid = models.CharField(max_length=30,blank=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)


class trendsfull(models.Model):
	trend = models.CharField(max_length=30,blank=True)
	count = models.CharField(max_length=30,blank=True,null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
