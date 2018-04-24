from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Materials)
admin.site.register(ProductionRate)
admin.site.register(Manufacturer)
admin.site.register(ProductRep)
admin.site.register(SalesRep)
admin.site.register(ContractorRep)
admin.site.register(Distributor)
admin.site.register(Contractor)
admin.site.register(Architect)
admin.site.register(Equipment)
admin.site.register(LaborRate)