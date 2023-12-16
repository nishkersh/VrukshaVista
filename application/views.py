from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage

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
