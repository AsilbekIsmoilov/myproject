from django.urls import path

from project.views import *

urlpatterns = [
    path("",index,name="index"),
    path("list2/",list2,name="list2"),
    path('update/page/', update_page, name='update_page'),
    path("update/process/<str:action>/", update_process, name="update_process"),
    path('delete-media-folder/', delete_media_folder, name='delete_media_folder'),
    path('delete-calldata/', delete_calldata, name='delete_calldata'),
    path('update/page/secret/page',delete_db,name='delete_db'),
    path('management/',management,name="management"),
    path('updates/', adds_view, name='adds'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('latest-schedule/<str:code>/', latest_schedule_redirect, name='latest_schedule'),
]
