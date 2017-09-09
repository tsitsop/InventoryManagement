# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Inventory(models.Model):
	name = models.CharField(max_length=20)

class Computer(models.Model):
	inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
	manufacturer = models.CharField(max_length=20)
	serial_number = models.IntegerField(default=0)
	comments = models.CharField(max_length=200)
