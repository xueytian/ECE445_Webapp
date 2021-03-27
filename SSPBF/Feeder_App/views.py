from django.shortcuts import render
from django.http import HttpResponse

from .models import image

def index(request):
    pic_list = image.objects.all()
    print("..................................")
    print(pic_list[0].image.url)
    print(pic_list[0].image.path)
    return render(request, 'pic.html', {'pic_list': pic_list})
