import os  
from django.contrib import admin
from .models import *
from django.utils.html import format_html
from urllib.parse import quote  


class CallDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photo_preview', 'bl', 'group', 'mark','month')
    search_fields = ('name',)
    ordering = ('name',)
    def get_photo_preview(self, obj):
        if obj.photo:
            filename = os.path.basename(obj.photo.name)
            url = f"/secure-photo/{quote(filename)}"
            return format_html(f'<img src="{url}" style="max-height:100px;"/>')
        return "-"
    
    get_photo_preview.short_description = "Фото"

class ScoresForMonthAdmin(admin.ModelAdmin):
    list_display = ('name', 'operator', 'id','mark','month') 
    search_fields = ('name',)  
    list_filter = ('operator',)
    ordering = ('name',)  

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('name')

class ManagementAdmin(admin.ModelAdmin):
    list_display = ['title','pdf_file','created_at']


class ScheduleAdmin(admin.ModelAdmin):
        list_display = ['code','title','pdf_file','created_at']

class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'order']
    ordering = ['order']


class RecordsAdmin(admin.ModelAdmin):
     list_display = ['operator','record','call_code','created_at']

admin.site.register(CallData, CallDataAdmin)
admin.site.register(ScoresForMonth,ScoresForMonthAdmin)

admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Management,ManagementAdmin)
admin.site.register(BackgroundImage,BackgroundImageAdmin)
admin.site.register(Records,RecordsAdmin)

