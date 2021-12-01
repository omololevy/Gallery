from django.shortcuts import render,redirect
from .models import Image
from .forms import UploadForm
from django.db.models import Q
from django.db.models.base import ObjectDoesNotExist 
from django.http  import HttpResponse,Http404

def home(request):
    pictures = Image.objects.all()
    ctx = {'pictures':pictures}
    return render(request,'pictures/home.html',ctx)

def upload_picture(request):
 
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save()
            image.save()
           
            return redirect('/')
    else:
        form = UploadForm()
    ctx = {
        'form':form
    }
    
    return render(request,'pictures/upload_picture.html',ctx)

def filter_location(request,location_id):
    try:
        locations = {'1':"nairobi",'2':"mombasa",'3':"kisumu",'4':"nakuru"}   
    
        filtered_pictures = Image.objects.filter(location__name__icontains=locations.get(str(location_id))) 
        message = f"{locations.get(location_id)}"
    except  ObjectDoesNotExist:
         raise Http404()
    return render(request,'pictures/filter_location.html',{"message":message,"pictures": filtered_pictures})
    
    
def query_image(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    images = Image.objects.filter(
        Q(category__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        ) 
    message = f"{q}"
    return render(request, 'pictures/search.html',{"message":message,"pictures": images})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_pictures = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'pictures/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'pictures/search.html',{"message":message})
  
