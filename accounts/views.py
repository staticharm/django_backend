from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method=='POST':
        fname=request.POST['fnamee']
        lname=request.POST['lastname']
        email=request.POST['mail']
        password=request.POST['password']

        User.objects.create_user(first_name=fname,last_name=lname,password=password,email=email)
        return redirect('/')
    return render(request,"index.html")
