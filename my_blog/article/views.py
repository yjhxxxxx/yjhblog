from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def detail(request,my_args):
	return HttpResponse("You're looking at my_args%s."%my_args)

