from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import requests
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def upload_image(request):
    # if request.method == 'POST' and request.FILES['image']:
    #     image = request.FILES['image']
    #     fs = FileSystemStorage()
    #     filename = fs.save(image.name, image)
    #     uploaded_file_url = fs.url(filename)
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        
        return HttpResponse(request, uploaded_file_url)

    return render(request, 'image_input.html')

def google_earth(request):
    return render(request, 'google_earth.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.info(request, 'Incorrect login ID or password. Please try again.')
        return redirect('/dashboard')
    return redirect("/")