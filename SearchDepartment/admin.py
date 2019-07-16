from django.contrib import admin
from .models import *


class RequestImageInline(admin.TabularInline):
    model = RequestImage
    extra = 1  # кол-во дополнительных рядов для добавления фото к заявке


class RequestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Request._meta.fields]
    inlines = [RequestImageInline]  # для добавления фотографий на страницу заявки в админке
    # (можно добавлять фото прямо из страницы заявки)

    class Meta:
        model = Request


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]

    class Meta:
        model = Department


class RequestImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RequestImage._meta.fields]

    class Meta:
        model = RequestImage


admin.site.register(Request, RequestAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(RequestImage, RequestImageAdmin)
