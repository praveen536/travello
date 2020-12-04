from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

# for logout
def logout(request):
    auth.logout(request)
    return redirect("/")

# for login 
def login(request):
    if request.method == 'POST':
        email = request.POST['email1']
        password = request.POST['password1']
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            print('you logged in..')
            return redirect("/")
        else:
            messages.info(request, 'invalid creadential')
            return redirect("login")

    else:
        return render(request, 'login.html')

# for register user
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        user_name = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd==cpwd:
            if User.objects.filter(username=user_name).exists():
                messages.add_message(request, messages.INFO, 'username taken.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, username=user_name, email=email, password=pwd)
                user.save()
                print('user created')
        else:
            messages.info(request,'Password not matching..')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'register.html')