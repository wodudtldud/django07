from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
def delete(request):
    cp = request.POST.get("cpass")
    u = request.user
    if check_password(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    return redirect("acc:profile")

def chpass(request):
    cp = request.POST.get("cpass")
    u = request.user
    if check_password(cp, u.password):
        np = request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect("acc:login")
    else:
        pass # 20일차
    return redirect("acc:update")

def update(request):
    if request.method == "POST":
        u = request.user
        ue = request.POST.get("umail")
        uc = request.POST.get("ucomm")
        up = request.FILES.get("upic")
        u.email , u.comment = ue, uc
        if up:
            u.pic.delete()
            u.pic = up
        u.save()
        return redirect("acc:profile")
    return render(request, "acc/update.html")


def profile(request):
    return render(request, "acc/profile.html")


def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
        return redirect("acc:login")
    return render(request, "acc/signup.html")

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            return redirect("acc:index")
        else: # 20 일차에 메세지
            pass
    return render(request, "acc/login.html")

def index(request):
    return render(request, "acc/index.html")