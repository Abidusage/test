from django.contrib import admin
from .models import Ressource
admin.site.site_header='kasage adminstration'

class RessourceAdmin(admin.ModelAdmin):
    list_display = ('formation', 'langue', 'description', 'liens')
# Register your models here.
admin.site.register(Ressource,RessourceAdmin)
# admin.site.unregister(Group)
