from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        
        return HttpResponse('Image Uploaded Successfully')

    return render(request, 'image_input_new.html')

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

def signup(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("/")
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    return redirect("/")


@login_required
def logout_user(request):
    logout(request)
    return redirect("/")

@login_required
def dashboard(request):
    context = {
        'data' : [
            {
                'heading' : 'Process Image',
                'content_min' : 'Explore advanced image processing techniques to enhance, analyze, and manipulate your digital images effectively',
                'image' : '/static/media/image_processing.jpg',
                'redirect_url' : '/dashboard',
                'content' : 'Dive into the world of advanced image processing with our tools. Enhance, analyze, and manipulate your digital images with ease. From basic photo editing to complex algorithmic processing, our platform offers a comprehensive suite of tools for professionals and hobbyists alike. Discover new ways to bring your images to life!'
            },
            {
                'heading' : 'Explore Google Earth',
                'content_min' : 'Leverage Google Earth integration for detailed geographical data and immersive mapping experiences.',
                'image' : 'https://source.unsplash.com/1600x900/?nature,water',
                'redirect_url' : '/google_earth',
                'content' : 'Utilize our Google Earth integration to access detailed geographical data and create immersive mapping experiences. This feature allows you to seamlessly incorporate real-world terrain, satellite imagery, and 3D buildings into your projects. Ideal for educators, researchers, and developers, it opens up a world of possibilities for geospatial analysis and visualization.'
            }
        ]
    }
    return render(request, 'dashboard.html' , context)