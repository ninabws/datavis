from django.shortcuts import render
from django.http import request
# Create your views here.
dt1 = [
      4,
      21,
      13,
      4,
      18,
      92,
      0
    ]

def index (request):
    return render (request, 'index.html', {'dt1': dt1})