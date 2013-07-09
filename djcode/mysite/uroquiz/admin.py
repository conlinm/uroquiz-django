from django.contrib import admin
from uroquiz.models import Uroquiz


class UroquizAdmin(admin.ModelAdmin):
    list_display = ('number', 'question')

admin.site.register(Uroquiz)

