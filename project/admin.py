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
    ordering = ('name',)  # Сортировка по имени

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('name')

class ManagementAdmin(admin.ModelAdmin):
    list_display = ['title','pdf_file','created_at']


class ManagementAdmin112(admin.ModelAdmin):
    list_display = ['title','pdf_file','created_at']


class Schedule1000Admin(admin.ModelAdmin):
        list_display = ['title','pdf_file','created_at']

class Schedule1009Admin(admin.ModelAdmin):
        list_display = ['title','pdf_file','created_at']

class Schedule112Admin(admin.ModelAdmin):
        list_display = ['title','pdf_file','created_at']

class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'order']
    ordering = ['order']


admin.site.register(CallData, CallDataAdmin)
admin.site.register(ScoresForMonth,ScoresForMonthAdmin)

admin.site.register(Schedule1000,Schedule1000Admin)
admin.site.register(Schedule1009,Schedule1009Admin)
admin.site.register(Schedule112,Schedule112Admin)
admin.site.register(Management,ManagementAdmin)
admin.site.register(Management112,ManagementAdmin112)
admin.site.register(BackgroundImage,BackgroundImageAdmin)
