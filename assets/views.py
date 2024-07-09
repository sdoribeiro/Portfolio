from django.shortcuts import render

from .models import Asset, Trade

# Create your views here.
def index(request):

    a1 = Asset.objects.all()
    a2 = Trade.objects.all()

    for a in a1:
        print(a.id, a.ticker)

    for b in a2:
        print(b.id, b.ticker)

    return render(request, "assets/index.html", {
        "assets": Asset.objects.all(),
        "trades": Trade.objects.all(),
        
    })