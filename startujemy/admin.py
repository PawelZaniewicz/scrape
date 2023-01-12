from django.contrib import admin
from .models import Plant, Mpk, Manager

# Register your models here.

class PlantAdmin(admin.ModelAdmin):
    list_display = ["id", "plant_name", "mpk", "manager_wmb"]
    search_fields = ["plant_name"]
    list_filter = ["manager_wmb"]


class MpkAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]


admin.site.register(Plant, PlantAdmin)
admin.site.register(Mpk, MpkAdmin)
admin.site.register(Manager)

