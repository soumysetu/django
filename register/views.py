from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request, "register/index.html")
def signup(request):
    if request.method == "POST":
        username = request.POST['username'] 
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        pwd = request.POST['password']  
        confirm_password = request.POST['confirm_password']  

        myuser = User.objects.create_user(username=username, password=pwd)
        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()
        messages.success(request, "your account is successfully created")
        return redirect('signin')

    return render(request, "register/signup.html")
def signin(request):
    if request.method == "POST":
        username = request.POST['username'] 
        pwd = request.POST['password']
        user = authenticate(request,username=username, password=pwd)
        print(user)
        
        if user is not None:
            login(request, user)
            first_name = user.first_name
            print("yayyyy")
            return render(request,"register/quiz.html")
        else:
            messages.error(request, "bad credential")
            return redirect('home')

    return render(request, "register/signin.html")

def quiz(request):
    return render(request, "register/quiz.html")
   
def signout(request):
    
    return redirect('home')

def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('')
        context={'form':form}
        return render(request,'register/addQuestion.html',context)
    else: 
        return redirect('quiz')