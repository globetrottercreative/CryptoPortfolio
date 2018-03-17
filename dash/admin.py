from django.contrib import admin
from dash.models import DailyPrice, SpotPrice, Crypto, Exchange, FiatCurrency

# Register your models here.
admin.site.register(DailyPrice)
admin.site.register(SpotPrice)
admin.site.register(Crypto)
admin.site.register(Exchange)
admin.site.register(FiatCurrency)