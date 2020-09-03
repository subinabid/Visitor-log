from django.shortcuts import render
from django.http import HttpResponse
from .forms import Visitors
from .models import ntpcusers

def visitors(request):
    return render(request, 'visitors.html' )

def visitors_add(request):
    if request.method == 'POST':
        form = Visitors(request.POST)
        form.save()
        form = Visitors()
        useradded = ntpcusers.objects.all()
        context = {'form':form, 'added':useradded }
        return render(request, 'visitors_add.html', context )
    else:
        form = Visitors()
        context = {'form':form }
        return render(request, 'visitors_add.html', context )