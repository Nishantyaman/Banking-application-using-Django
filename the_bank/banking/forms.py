# from django.forms import ModelForm
from django import forms
from .models import Banks,Branches

# Create your models here.
class branch_form(forms.ModelForm):
	class Meta:
		model=Branches
		fields=['ifsc']

	def __str__(self):
		return self.title

class branch_form2(forms.Form):
	bank_name = forms.CharField(help_text="Enter bank name")
	bank_city = forms.CharField(help_text="Enter city")

