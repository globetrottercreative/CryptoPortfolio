from django.contrib import admin
from dash.models import DailyPrice, SpotPrice, Crypto

# Register your models here.
admin.site.register(DailyPrice)
admin.site.register(SpotPrice)
admin.site.register(Crypto)