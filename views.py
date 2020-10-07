from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contactList(request):
    contacts=Contact.objects.all()
    return render(request, "contactList.html", {'contacts':contacts})


def contactNew(request):
    form = ContactForm
    return render(request, "contactNew.html", {'form': form})
