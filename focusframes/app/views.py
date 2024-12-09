from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User


# Create your views here.

def e_shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req, "invalid password")
            return redirect(e_shop_login)
    else:
        return render(req,'login.html')
	

def shop_home(req):
    data=product.objects.all()
    if 'shop' in req.session:
        return render(req,'shop/home.html',{'products':data})
    else:
        return redirect(e_shop_login)
    

def add_product(req):
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            dis=req.POST['dis']
            price=req.POST['price']
            o_price=req.POST['offer_price']
            file=req.FILES['img']
            data=product.objects.create(pid=pid,name=name,dis=dis,price=price,offer_price=o_price,img=file)

            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/addproduct.html')
    else:
        return redirect(e_shop_login)

	
def e_shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(e_shop_login)
def Register(req):
    if req.method=='POST':
        username=req.POST['uname']
        email=req.POST['email']
        password=req.POST['pswd']
        
        try:
            data=User.objects.create_user(first_name=username,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req,"username already exist")
            return redirect(Register)
        return redirect(e_shop_login)
    else:
        return render(req,'user/Register.html')


def user_home(req):
    if 'user' in req.session:
        data=product.objects.all()
        return render(req,'user/home.html',{'products':data})
    else:
        return redirect(e_shop_login)

def women_frames(req):
    if 'user' in req.session:
        if req.method == 'POST':
            pid = req.POST['pid']
            name = req.POST['name']
            dis = req.POST['dis']
            price = req.POST['price']
            o_price = req.POST['offer_price']
            file = req.FILES['img']

            data=product.objects.create(pid=pid,name=name,dis=dis,price=price,offer_price=o_price)
            data=product.objects.get(pk=pid)
            data.img=file
            data.save()
            
            return redirect('women_frames')
        else:
         
            products = product.objects.all()
            return render(req, 'user/womenframes.html', {'products': products})
    else:
        return redirect('e_shop_login')

def edit_product(req,pid):
    if req.method=='POST':
        pid=req.POST['pid']
        name=req.POST['name']
        dis=req.POST['dis']
        price=req.POST['price']
        o_price=req.POST['off_price']
        file=req.FILES.get('img')
        if file:
            product.objects.filter(pk=pid).update(pid=pid,name=name,dis=dis,price=price,offer_price=o_price)
            data=product.objects.get(pk=pid)
            data.img=file
            data.save()
        else:
            product.objects.filter(pk=pid).update(pid=pid,name=name,dis=dis,price=price,offer_price=o_price)
        return redirect(shop_home)
    else:
        data=product.objects.get(pk=pid)
        return render(req,'shop/edit.html',{'data':data})

def delete_product(req,pid):
    data=product.objects.get(pk=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)


def about(request):
    return render(request,'user/about.html')

