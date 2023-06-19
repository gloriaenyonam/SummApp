from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from users.models import APPUser

def home(request):
    return render(request, 'home.html')

def log_in(request):
    if request.method == "POST":
        email= request.POST.get("email_address")
        print("email_address", email)
        password= request.POST.get("password")
        print("password", password)
        try:
            APPUser.objects.get(email=email)
        except:
            messages.error(request, "Email does not exist.", extra_tags='error-class')
            return redirect("/log_in/")
        user = authenticate(email=email, password=password)
        print("user", user)
        if user is not None and user.is_active == True:
             login(request, user)
             return redirect("/")
        messages.error(request, "Password is incorrect.", extra_tags='error-class')
        return redirect("/log_in/")       

    return render(request, 'log_in.html')

def summary(request):
    return render(request, 'summary.html')

def friends_list(request):
    return render(request, 'friends_list.html')

def sign_up(request):   
#    print("method", request.method)
    if request.method == "POST":
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        email= request.POST.get("email_address")
        phone_number= request.POST.get("phone_number")
        country= request.POST.get("country")
        city= request.POST.get("city")
        password= request.POST.get("password")
        confirm_password= request.POST.get("confirm_password")
        if password != confirm_password:
            messages.error(request, "passwords don't match.", extra_tags='error-class')
            return redirect("/sign_up/")
        if len(password) < 6:
            messages.error(request, "password should be more than 6 characters.", extra_tags='error-class')
            return redirect("/sign_up/")
        try:
            APPUser.objects.get(email=email)
            print("email already exists")
        except:
            print("new user")
            new_user = APPUser.objects.create(email=email, first_name=first_name, last_name=last_name, phone_number=phone_number, country=country, city=city)
            new_user.set_password(password)
            new_user.save()
            return redirect("/log_in/")
        

    return render(request, 'sign_up.html')
    

def my_account(request):
    return render(request, 'my_account.html')
    
    
    
    