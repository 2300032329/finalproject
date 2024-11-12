from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail  # For sending emails
from .models import ContactUs  # Corrected to match the model name

# Create your views here.
def home(request):
    return HttpResponse("This is KLU project with CSE app")

def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login1.html')

def logout(request):
    return render(request, 'logout.html')

def contactpagecall(request):
    return render(request, 'contact.html')

def contactlogic(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        comment = request.POST.get('comment', '')

        if firstname and lastname and email and comment:
            # Save the form data to the database
            data = ContactUs(firstname=firstname, lastname=lastname, email=email, comments=comment)
            data.save()

            # Send a thank-you email
            subject = 'Thank You for your valuable Feedback'
            send_mail(
                subject,
                comment,
                'bpujitha1104@gmail.com',  # Your sender email
                [email],
                fail_silently=False,
            )
            return HttpResponse("<h1><center>Thank you for your feedback</center></h1>")
        else:
            return HttpResponse("<h1>Error: All fields are required</h1>")
    else:
        return HttpResponse("<h1>Error: Invalid request method</h1>")
