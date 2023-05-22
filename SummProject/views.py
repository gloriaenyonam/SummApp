from django.shortcuts import render

from users.models import APPUser

def home(request):
    return render(request, 'home.html')

def log_in(request):
    return render(request, 'log_in.html')

def summary(request):
    return render(request, 'summary.html')

def friends_list(request):
    return render(request, 'friends_list.html')

def sign_up(request):
    # print("method", request.method)
    # if request.method == "POST":
    #     email = ''
    #     APPUser.objects.filter(email=email)
    return render(request, 'sign_up.html')

def my_account(request):
    return render(request, 'my_account.html')
    
    
    
    