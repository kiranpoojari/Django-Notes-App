from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import Note
# Create your views here.

@login_required
def home(request):
    notes=Note.objects.filter(user=request.user)
    return render(request,'index.html', { 'notes':notes})

@login_required
def get_note(request,pk):
    get_notes=Note.objects.get(pk=pk)
    return render(request,'note.html', { 'get_notes':get_notes})

@login_required
def add_note(request):
    if request.method=="POST":
        new_title=request.POST['title']
        new_content=request.POST['note']
        add=Note(user=request.user,title=new_title, content=new_content)
        add.save()
        return redirect( 'home')
    return render(request, "add_note.html")

@login_required
def delete_note(request,id):
    del_note=Note.objects.get(id=id)
    del_note.delete()
    return redirect( 'home')

@login_required
def update_note(request,id):
    u_note=Note.objects.get(id=id)
    if request.method=='POST':
        u_note.title=request.POST['title']
        u_note.content=request.POST['content']
        u_note.save()

        return redirect('notes', pk=id  )
    return render(request, 'update_note.html',{'u_note':u_note})

def register_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #validations
        if username =="" or password == "":
            return render(request, "register.html",{"error":"All fields are required"})
        
        if User.objects.filter(username=username).exists():
            return render(request, "register.html",{"error":"User already exists"})

        #creating user
        User.objects.create_user(username=username,password=password)
        return redirect('login')
    return render(request,'register.html')


def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username=username, password=password)
        if user is  None:
            return render(request,"login.html",{"error":"Invalid username or password"})
        login(request,user)
        return redirect ('home')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')