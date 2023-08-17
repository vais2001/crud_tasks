from django.contrib import admin
from django.urls import path
from informations import views

urlpatterns = [
    # path('get_number/<int:pk>',views.get_number,name='get_number'),
      path('creation',views.creation,name="creation"),
    #   path('updated',views.updated,name="updated"),
    #   path('getdata',views.get_data,name="getdata")
]