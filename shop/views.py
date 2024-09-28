from django.shortcuts import render
from .models import Phone

def index(request):
    phones = Phone.objects.all()
    return render(request, 'index.html', {'phones': phones})
