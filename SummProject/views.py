from django.shortcuts import render, redirect

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
#    print("method", request.method)
    if request.method == "POST":
        first_name= request.POST.get("first_name")
        print("first_name")
        last_name= request.POST.get("last_name")
        print("last_name")
        email= request.POST.get("email_address")
        print("email")
        phone_number= request.POST.get("phone_number")
        print("phone_number")
        country= request.POST.get("country")
        print("country")
        city= request.POST.get("city")
        print("city")
        password= request.POST.get("password")
        print("password")
        confirm_password= request.POST.get("confirm_password")
        print("confirm_password")
        if password != confirm_password:
            print("passwords don't match")
            return ""
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
    
    
    
    