from django.shortcuts import render,HttpResponse
def home(request):
    return HttpResponse("This is klu project with ECE app")
def base(request):
    return render(request,'base.html')
def login(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')
def photo(request):
    return render(request,'photo.html')
def homepage(request):
    return render(request,'homepage.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'UserRegisterPage.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'homepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'UserRegisterPage.html')
    else:
        return render(request, 'UserRegister.html')