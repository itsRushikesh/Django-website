from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        "variable1": "rushi",
        "variable2": "bobade"


    }

    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Services page")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,
                          contact=contact, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Query has been submitted")

    return render(request, 'contact.html')
    # return HttpResponse("This Contact page")


def checkout(request):
    return render(request, 'checkout.html')
