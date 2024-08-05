from django.urls import path
from . import views

urlpatterns = [
    path('total-views', views.totalViews, name = "api-total-views"),
    path('datatable-api', views.datatable_api, name = "api-datatable-api")

]

                        