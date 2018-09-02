from django.shortcuts import render
from .models import Banks,Branches
from django.core import serializers
from .forms import branch_form,branch_form2
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
	return render(request,'banking/home.html')

def bank_ifsc(request):
	if request.method == "POST":
		product_data=[]
		query = request.POST["q"]
		psobjs = Branches.objects.filter(ifsc=query)
		queryset = Banks.objects.filter(id__in=psobjs.values('bank_id')).values()
		for name in queryset:
			names=name['name']
		psobjs=psobjs.values()
		for student in psobjs:
			product_d = {
				'branch': student['branch'],
				'address': student['address'],
				'city': student['city'],
				'district': student['district'],
				'state': student['state'],
			}

			product_data.append(product_d)
		print(product_data)
		if not product_data:
			product_data=None
			names=None
		return render(request,'banking/detailsbyifsc.html',{'product_data':product_data,'names':names})
	else:
		form=branch_form()
		return render(request,'banking/seachbyifsc.html')

def bank_name(request):
	if request.method == "POST":
		product_data=[]
		query1 = request.POST["name"]
		query2 = request.POST["city"]
		psobjs = Banks.objects.filter(name=query1)
		queryset = Branches.objects.filter(bank_id__in=psobjs.values('id')).filter(city=query2).values()
		for student in queryset:
			product_d = {
				'branch': student['branch'],
				'address': student['address'],
				'district': student['district'],
				'state': student['state'],
			}

			product_data.append(product_d)
		print(product_data)
		if not product_data:
			product_data=None
		return render(request,'banking/detailsbyname.html',{'product_data':product_data})
	else:
		form=branch_form2()
		return render(request,'banking/searchbyname.html')