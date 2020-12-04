from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request): 
    # return HttpResponse("<h1>hello word</h1>")
    return render(request, 'home.html',{'name':'ram'})


def add(request):
    val1=request.POST['inp1']
    val2=request.POST['inp2']
    res = val1 + val2
    return render(request, 'result.html',{'result2':res})