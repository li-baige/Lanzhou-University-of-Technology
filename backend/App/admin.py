from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Article)
admin.site.register(Boundary)
admin.site.register(City)
admin.site.register(Track)
admin.site.register(VillageStatus)
admin.site.register(VillageData)
admin.site.register(Community)