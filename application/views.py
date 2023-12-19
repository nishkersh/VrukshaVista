from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Google_Captured_Image
import datetime
from io import BytesIO
from django.core.files.images import ImageFile

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

def google_earth_old(request):
    return render(request, 'google_earth_old.html')


def map_data(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lng')
    zoom = request.GET.get('zoom')
     
    try:
        response = requests.get('https://maps.googleapis.com/maps/api/staticmap?scale=2&center='+lat+','+lon+'&zoom='+zoom+'&size=2000x2000&maptype=satellite&key=AIzaSyBWqUl-HlAe-bbl_jNiFdrFu5gEcLe7Bes')
        if response.status_code == 200:
            temp_img = BytesIO(response.content)
            image = ImageFile(temp_img)

            # Save image to /uploaded_images/google/ folder with a timestamp
            fs = FileSystemStorage()
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = fs.save(f"google_images/{lon},{lat},{zoom}_{timestamp}.jpg", image)
            uploaded_file_url = fs.url(filename)

            return HttpResponse(uploaded_file_url)
        else:
            return HttpResponse("Failed to fetch image from Google Maps", status=500)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)




# def map_data(request):
#     if request.method == 'POST':
#         lat = request.POST.get('lat')
#         lon = request.POST.get('lon')
#         zoom = request.POST.get('zoom')

#         # https://maps.googleapis.com/maps/api/staticmap?scale=2&center=30.7580,76.7685&zoom=20&size=2000x2000&maptype=satellite&key=AIzaSyBWqUl-HlAe-bbl_jNiFdrFu5gEcLe7Bes

#         image = requests.get('https://maps.googleapis.com/maps/api/staticmap?scale=2&center='+lat+','+lon+'&zoom='+zoom+'&size=2000x2000&maptype=satellite&key=AIzaSyBWqUl-HlAe-bbl_jNiFdrFu5gEcLe7Bes')

#         if lat and lon and zoom and image:
#             Google_Captured_Image.objects.create(lat=lat, lon=lon, zoom=zoom,image = image, user=request.user)
#             return redirect('/google_earth')
        
#         else:
#             return HttpResponse('Please enter all the fields')
        
#     return HttpResponse('Wrong Request')


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