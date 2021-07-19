from django.shortcuts import render
from django.views import View
from .models import CustomOrder,Payment, Cal
from django.http import HttpResponse
# Create your views here.


def index(request):

#     return HttpResponse("Hello, world. You're at the polls index.")
    
#     urlpatterns = [
#     path('', views.index, name='index'),
#    ]
    posts = Payment.objects.all()

    context = {
        'posts': posts
    }
    if request.method == 'POST':
        #form = Top_List_Form(request.POST)
        return HttpResponse("Do something") # methods must return HttpResponse
    
        return render(request,'steps_count/index.html',{'top_list': top_list})

    return render(request, "homepage.html", context=context)
    urlpatterns = [
    path('', views.index, name='index'),
 ]

    

def addCustomerOrder(request):

    if request.method == "POST":
        
        title = request.POST.get("title")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        shisha= CustomOrder(title=title, name=name,phone=phone, email=email, address=address)
        shisha.save()
        return HttpResponse("Okay")
    else:
        return render (request, "homepage.html")