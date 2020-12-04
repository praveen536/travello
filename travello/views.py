from django.shortcuts import render
from django.http import HttpResponse
from .models import Designation
# Create your views here.
def index(request):
    # dest1 = Designation()
    # dest1.name='America'
    # dest1.price='300'
    # dest1.img='destination_1.jpg'
    # dest1.desc='raipur is good city'
    # dest1.offer='false'
    
    # dest2 = Designation()
    # dest2.name='Italy'
    # dest2.price='400'
    # dest2.img='destination_2.jpg'
    # dest2.desc='bilasput is good city'
    # dest2.offer='true'

    # dests = [dest1, dest2, dest3]
    # return render(request, 'index.html', {'price': 1700,'dests':dests})

    dests = Designation.objects.all() 
    return render(request, 'index.html', {'dests':dests})

def about(request):
    return render(request, 'about.html')