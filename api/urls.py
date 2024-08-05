from django.urls import path
from . import views

urlpatterns = [
    path('total-views', views.totalViews, name = "api-total-views"),
     path('datatable-api', views.datatable_api, name = "api-datatable-api")
=======
    path('datatable-api', views.datatable_api, name = "api-datatable-api")
>>>>>>> c727bb4b8717577cb1bc0b3a29120b69f35f2b31
]

                        