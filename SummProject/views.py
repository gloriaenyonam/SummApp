from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def log_in(request):
    return render(request, 'log_in.html')
    