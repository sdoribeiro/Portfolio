from django.shortcuts import render
from django.http import JsonResponse
from api.models import TotalViewsModel

# Create your views here.

def totalViews(request):

    queryset = TotalViewsModel.objects.all()

    dct = {
        "labels": [],
        "data": []
    }

    for item in queryset:
        dct["labels"].append(item.label)
        dct["data"].append(item.views)

    return JsonResponse(dct)
