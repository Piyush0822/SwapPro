from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def log_in(request):
    return render(request, 'log_in.html')
def reg_istar(request):
    return render(request ,'reg_istar.html')

def Contact_Us(request):
    return render(request , 'Contact_Us.html')

def About_Us(request):
    return render(request , 'About_Us.html')