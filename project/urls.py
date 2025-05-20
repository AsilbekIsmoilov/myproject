from django.urls import path

from project.views import *

urlpatterns = [
    path("",index,name="index"),
    path("list2/",list2,name="list2"),
    path('update/page/', update_page, name='update_page'),
    path("update/process/<str:action>/", update_process, name="update_process"),
]