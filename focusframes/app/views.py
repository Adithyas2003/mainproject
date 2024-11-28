from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import *


# Create your views here.
def e_shop_login(req):
    
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
           
        else:
            messages.warning(req, "invalid password")
            return redirect(e_shop_login)
    else:
        return render(req,'login.html')
	