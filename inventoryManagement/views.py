# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import FormView
from inventoryManagement.forms import InventoryForm, ComputerForm
from django.shortcuts import render

# Create your views here.
class InventoryManagementView(FormView):
	template_name = 'inventoryManagement/index.html'
	form_class = InventoryForm
