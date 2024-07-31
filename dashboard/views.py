from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"dashboard/dashboard.html", {
        
    })


def reports(request):
    return render(request,"dashboard/reports.html", {
        
    })