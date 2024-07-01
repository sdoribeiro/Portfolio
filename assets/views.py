from django.shortcuts import render

from .models import Asset, Trade

# Create your views here.
def index(request):
    return render(request, "assets/index.html", {
        "assets": Asset.objects.all(),
        "trades": Trade.objects.all(),
        
    })