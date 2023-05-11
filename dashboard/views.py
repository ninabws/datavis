from django.shortcuts import render
from django.http import request
from .models import cadastro
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

 
def index (request):
  dt = []
  values = cadastro.objects.all()
  for v in values:
    dt.append(v.value)
  return render (request, 'index.html', {'dt1': dt})
  
  