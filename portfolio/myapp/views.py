from django.http import HttpResponse
from django.shortcuts import render
from .models import ContactMessage

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'message': message
        }
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        print(data)

        return HttpResponse("Thank you! Your message has been sent.")

    return render(request, "contact.html")
