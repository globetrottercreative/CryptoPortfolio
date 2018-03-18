from django.contrib import admin
from dash.models import HourlyPrice, SpotPrice, Crypto, Exchange, FiatCurrency

# Register your models here.
admin.site.register(HourlyPrice)
admin.site.register(SpotPrice)
admin.site.register(Crypto)
admin.site.register(Exchange)
admin.site.register(FiatCurrency)