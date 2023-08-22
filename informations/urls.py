from django.contrib import admin
from django.urls import path
# from informations import views
from .views import*

urlpatterns = [
      path('creation',CreateWorker.as_view(),name="creation"),
      path('updated',Update_Worker.as_view(),name="updated"),
      path('getdata',GetWorkerData.as_view(),name="getdata"),
      path('deldata',Delete_data.as_view(),name="deldata")
]