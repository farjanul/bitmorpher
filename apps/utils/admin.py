from django.contrib import admin

from apps.utils.models import RequestLogModel


@admin.register(RequestLogModel)
class RequestLogModelAdmin(admin.ModelAdmin):
    pass

