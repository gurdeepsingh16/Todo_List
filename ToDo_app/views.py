from django.shortcuts import render,redirect
from ToDo_app.models import Todo_model
from .forms import Todo_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.
@never_cache
@login_required(login_url="login")
def home(request):
    if request.method =="GET":
        form = Todo_form()
        data = Todo_model.objects.all()
        return render(request,"home.html",{'data':data,'form':form})
    else:
        form = Todo_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"home.html")

@never_cache
@login_required(login_url="login")
def delete(request,id):
    try:
        data = Todo_model.objects.get(id=id)
        data.delete()
        return redirect("home")
    except Exception as e:
        print(e)
        return render(request,"home.html")

def update(request,id):
    data = Todo_model.objects.get(id=id)
    if request.method =="GET":
        form = Todo_form(instance=data)
        data = Todo_model.objects.all()
        return render(request,"home.html",{'data':data,'form':form})
    else:
        form = Todo_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"home.html")

    
def login_f(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Username/Password is Wrong")
            return redirect("login")


    return render(request,'login.html')

def logout_f(request):
    logout(request)
    return redirect("login")



def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        email=request.POST['email']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(email=email).exists():
                 messages.error(request,"Email Allready Exists ")
                 return redirect("signup")
            
            elif  User.objects.filter(username=username).exists():
                messages.error(request,"User Allready Exists ")
                return redirect("signup")
            
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                return redirect("login")
        else:
             messages.error(request,"Password Does Not match")
             return redirect("signup")


    return render(request,'signup.html')

