from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import User
from django.utils import timezone
import hashlib

def sign_in_template(request):
    return render(request, 'users/sign_in.html')

def sign_up_template(request):
    return render(request, 'users/sign_up.html')

def sign_in(request):
    try:
        user = User.objects.get(email=request.POST['email'])
        hashed = hashlib.md5(request.POST['password'].encode()).hexdigest()
        if user.password == hashed:
            request.session['auth'] = user.email
            # request.flash['response'] = "Welcome, "+user.email
            return redirect('/')
        else:
            # request.flash['response'] = "Incorrect email or password"
            return redirect('/users/sign_in')
    except:
        # request.flash['response'] = "Incorrect email or password"
        return redirect('/users/sign_in')

def sign_up(request):
    if request.POST.get('email') and request.POST.get('password'):
        try:
            user = User.objects.get(email=request.POST['email'])
            # request.flash['response'] = "This email is already taken!"
            return redirect('/users/sign_up')
        except:
            hashed = hashlib.md5(request.POST['password'].encode()).hexdigest()
            user = User(email=request.POST['email'], password=hashed)
            user.save()
            request.session['auth'] = user.email
            # request.flash['response'] = "Welcome, "+user.email
            return redirect('/')
    else:
        return redirect('/users/sign_up')

def log_out(request):
    request.session['auth'] = None
    # request.flash['response'] = "Logged out!"
    return redirect('/')
