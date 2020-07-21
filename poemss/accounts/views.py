from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

def join(request):
    if request.method == 'POST':
        #get form values
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        if password == password2:
            #check username
            if User.objects.filter(username= username).exists():
                messages.error(request, 'That username is taken')
                return redirect('join')
            else:
                if User.objects.filter(email= email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('join')
                else:
                    user= User.objects.create_user(username= username, password= password, email= email)
                    user.save()
                    messages.success(request, 'you are now registered in')
                    return redirect('login')
        else:
            messages.error(request, 'Password donot match')
            return redirect('join')
            
    else:
        return render(request, 'accounts/join.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')



def logout(request):

    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('login') 
    

def profile(request):
    return render(request, 'accounts/profile.html')