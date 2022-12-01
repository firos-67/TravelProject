from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team

# Create your views here.



def index(request):
    place_obj=Place.objects.all()
    team_obj=Team.objects.all()
    return render(request,'index.html',{'place':place_obj,'team':team_obj})