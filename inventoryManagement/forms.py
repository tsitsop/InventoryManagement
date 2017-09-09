from django import forms

from crispy_forms.helper import FormHelper

class InventoryForm(forms.Form):
	name = forms.CharField(label="Inventory Name", required=True, max_length=20)


class ComputerForm(forms.Form):
	manufacturer = forms.CharField(label="Manufacturer", required=True, max_length=20)
	serial_number = forms.IntegerField(label="Serial Number", required=True)
	comments = forms.CharField(label="Comments", required=True, max_length=200) 	

# https://godjango.com/29-crispy-forms/ 
# 3:30
