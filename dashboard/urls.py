from django.urls import path
from . import views

urlpatterns = [
    path("reports",views.reports, name="dashboard-reports"),
    path("",views.index, name="dashboard-index")
]