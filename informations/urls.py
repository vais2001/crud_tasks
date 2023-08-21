from django.contrib import admin
from django.urls import path
from informations import views

urlpatterns = [
      path('creation',views.creation,name="creation"),
      path('updated',views.update_worker,name="updated"),
      path('getdata',views.get_data,name="getdata"),
      path('deldata',views.delete_data,name="deldata")
]