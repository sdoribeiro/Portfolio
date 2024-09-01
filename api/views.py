from django.shortcuts import render
from django.http import JsonResponse
from api.models import TotalViewsModel, MostWatchedVideos

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

def datatable_api(request):
    
    queryset= MostWatchedVideos.objects.all()

    dct = {
        "title": [],
        "published_date": [],
        "views_count": []
    }

    for item in queryset:
        dct["title"].append(item.title)
        dct["published_date"].append(item.published_date)
        dct["views_count"].append(item.views_count)

    return JsonResponse(dct)

