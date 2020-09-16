from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from datetime import datetime
import datetime as dt
from .forms import NTPCVisitors, ExternalVisitors, Meeting
from .models import ntpcuser, externaluser, meeting, visitor
#############################################################################################

######################### Visitors ################################################
def visitors(request):
    context = {
        'NoOfVisitors':visitor.objects.count(),
        'NoOfNtpcVisitors':ntpcuser.objects.count(),
        'NoOfExternalVisitors':externaluser.objects.count(),
    }
    return render(request, 'visitors.html', context )

######################### Visitors - add NTPC visitor ##############################
def visitors_add_internal(request):
    if request.method == 'POST':
        form = NTPCVisitors(request.POST)
        useradded = form.save()
        v = visitor(ntpcuser = useradded, source = "NTPC")
        v.save()

        form = NTPCVisitors()
        context = {'form':form, 'added':useradded }
        return render(request, 'visitors_add.html', context )
        # replace with return redirect, message 
    else:
        form = NTPCVisitors()
        context = {'form':form }
        return render(request, 'visitors_add.html', context )

######################### Visitors - add External visitor ##########################
def visitors_add_external(request):
    if request.method == 'POST':
        form = ExternalVisitors(request.POST)
        useradded = form.save()
        v = visitor(externaluser = useradded, source = "Ext")
        v.save()

        form = ExternalVisitors()
        context = {'form':form, 'added':useradded }
        return render(request, 'visitors_add.html', context )
        # replace with return redirect + message 
    else:
        form = ExternalVisitors()
        context = {'form':form }
        return render(request, 'visitors_add.html', context )

######################### Visitors - List - Internal ###############################    
def visitors_list_internal(request):
    context = {
        'visitorList':ntpcuser.objects.all(),
        'source':"NTPC"
    }
    return render(request, 'visitors_list.html', context )

######################### Visitors - List - external ###############################    
def visitors_list_external(request):
    context = {
        'visitorList':externaluser.objects.all(),
        'source':"Ext"
    }
    return render(request, 'visitors_list.html', context )

######################### Visitors - Edit ########################################## 
def visitors_edit(request,int):
    context = {'NTPCUserList':ntpcuser.objects.all()}
    return render(request, 'visitors_list.html', context )

######################### Meetings ##############################
def meetings(request):
    context = {
        'meetings':meeting.objects.filter(timein__date = dt.date.today()).select_related('visitor').annotate(source = F('visitor__source'))
    }
    return render(request, 'meetings.html', context )

def meetings_add(request):
    if request.method == 'POST':
        form = Meeting(request.POST)
        meeting_added = form.save()
        form = Meeting(initial={'timein':datetime.now, 'timeout':datetime.now})
        context = {'form':form, 'added':meeting_added  }
        return render(request, 'meetings_add.html', context )
    else:
        form = Meeting(initial={'timein':datetime.now, 'timeout':datetime.now})
        context = {'form':form }
        return render(request, 'meetings_add.html', context )
