from django.contrib import admin
from skeins.models import Colour, Component, Fibre, Manufacturer, Skein

class ColourAdmin(admin.ModelAdmin):
    pass

class FibreAdmin(admin.ModelAdmin):
    pass

class ComponentAdmin(admin.ModelAdmin):
    pass

class ManufacturerAdmin(admin.ModelAdmin):
    pass

class SkeinAdmin(admin.ModelAdmin):
    pass


admin.site.register(Colour, ColourAdmin)
admin.site.register(Fibre, FibreAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Skein, SkeinAdmin)
admin.site.register(Component, ComponentAdmin)