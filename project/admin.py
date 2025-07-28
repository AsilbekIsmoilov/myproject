from django.contrib import admin
from .models import *



class CallDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'bl', 'group', 'mark','month')
    search_fields = ('name',)
    ordering = ('name',)


class ScoresForMonthAdmin(admin.ModelAdmin):
    list_display = ('name', 'operator', 'id','mark','month')  # Добавить другие поля, если необходимо
    search_fields = ('name',)  # Поиск по имени
    list_filter = ('operator',)  # Фильтрация по оператору
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

