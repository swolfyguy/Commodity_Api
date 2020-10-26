from django.contrib import admin
from elements_app.models import Element, Commodity, Composition


# Register your models here.
class ElementAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class CommodityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "inventory", "price"]


class CompositionAdmin(admin.ModelAdmin):
    list_display = ["element_id", "commodity_id", "percentage"]


admin.site.register(Element, ElementAdmin)
admin.site.register(Commodity, CommodityAdmin)
admin.site.register(Composition, CompositionAdmin)
