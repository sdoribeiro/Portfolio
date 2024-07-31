from django.urls import path
from . import views

urlpatterns = [
    path('total-views', views.totalViews, name = "api-total-views")
]

                        