
from django.contrib import admin
from .models import Manufacturer, Product, DigitalProductPassport, Importer, Dealer, EnvironmentalData

admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(DigitalProductPassport)
admin.site.register(Importer)
admin.site.register(Dealer)
admin.site.register(EnvironmentalData)
