from django.shortcuts import render
from .models import ContactData


def contact_view(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        company = request.POST.get('company')
        salary = request.POST.get('salary')
        location = request.POST.get('location')

        ContactData(
            fname = fname,
            lname = lname,
            email = email,
            company = company,
            salary = salary,
            location = location,

        ).save()

        return render(request, 'contact.html')

    else:
        return render(request,'contact.html')
