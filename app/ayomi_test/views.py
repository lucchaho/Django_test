from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from ayomi_test.models import User_ayomi

def index(request):
    template = loader.get_template('login/login.html')
    return HttpResponse(template.render(request=request))

def profil(request):
    template = loader.get_template('login/login.html')
    users = User_ayomi.objects.all()
    context = {}
    if request.method == 'POST':
        newEmail = request.POST.get('newEmail')
        email = request.POST.get('email')
        password = request.POST.get('password')

        for user in users:
            if user.email == email and user.password == password:
                if newEmail is not None:
                    user.email = newEmail
                    user.save()
                context["isLogin"] = True
                context["email"] = user.email
                context["password"] = user.password
    else:
        context["isLogin"] = False

    template = loader.get_template('profil/profil.html')
    return HttpResponse(template.render(context, request=request))

def register(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = User_ayomi(email=email, password=password)
        try:
            user.save()
            context["isRegistered"] = True
        except ValueError:
            print(ValueError)
            context["isRegistered"] = False         
    template = loader.get_template('register/register.html')
    return HttpResponse(template.render(context, request=request))



