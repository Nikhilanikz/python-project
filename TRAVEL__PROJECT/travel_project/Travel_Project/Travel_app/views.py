from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, meetTeam


# Create your views here.


def demo(request):
    obj = Place.objects.all()
    tem = meetTeam.objects.all()
    return render(request, "index.html", {'result': obj, 'res': tem})

# def team(request):
#     tem = Team.objects.all()
#     return render(request, "index.html", {'res': tem})
