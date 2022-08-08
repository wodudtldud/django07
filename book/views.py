from django.shortcuts import render, redirect
from .models import Book
# Create your views here.
def create(request):
    if request.method =="POST":
        sn = request.POST.get("sname")
        su = request.POST.get("surl")
        sc = request.POST.get("scon")
        im = request.POST.get("impo")
        Book(site_name=sn, maker=request.user, site_url=su, site_con=sc, impo=bool(im) ).save()
        return redirect("book:index") 
    return render(request, "book/create.html")


def index(request):
    b = request.user.book_set.all()
    context = {
        "bset" : b
    }
    return render(request, "book/index.html", context)