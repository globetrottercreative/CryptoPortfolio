from django.db import models

# Cryptocurrency Data Model
class Crypto(models.Model):
    name = models.CharField(max_length=50, default='', unique=True)
    code = models.CharField(max_length=4, default='', unique=True)
    code_alt = models.CharField(max_length=4, default='', unique=True, blank=True)
    def __str__(self):
        return self.name

# Cryptocurrency Arverages Data Model
class CryptoAverage(models.Model):
    fiat = models.CharField(max_length=50, default='')
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, blank=True)
    cmc_marketcap = models.CharField(max_length=50, default='', blank=True)
    cmc_rank = models.CharField(max_length=50, default='', blank=True)
    cmc_pct_change24 = models.CharField(max_length=50, default='', blank=True)
    cmc_pct_change7d = models.CharField(max_length=50, default='', blank=True)
    cmc_total_sply = models.CharField(max_length=50, default='', blank=True) 
    cmc_avg_price = models.CharField(max_length=50, default='', blank=True) 
    def __str__(self):
        return self.name

# Fiat Currency Data Model
class FiatCurrency(models.Model):
    name = models.CharField(max_length=50, default='', unique=True)
    code = models.CharField(max_length=4, default='', unique=True)
    code_alt = models.CharField(max_length=4, default='', unique=True, blank=True)
    def __str__(self):
        return self.name

# Daily Crytocurrency Data Point Data Model
class HourlyPrice(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, blank=True)
    currency = models.CharField(max_length=4, default='')
    avg_price = models.CharField(max_length=50, default='')
    day_start = models.DateTimeField()
    day_end = models.DateTimeField()
    source_api = models.CharField(max_length=50, default='')
    source_data = models.CharField(max_length=50, default='')
    open_value = models.CharField(max_length=50, default='')
    high_value = models.CharField(max_length=50, default='')
    low_value = models.CharField(max_length=50, default='')
    close_value = models.CharField(max_length=50, default='')
    volume = models.CharField(max_length=50, default='')

# Snapshot Crytocurrency Data Point Data Model
class SpotPrice(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, blank=True)
    currency = models.CharField(max_length=4, default='')
    timestamp = models.DateTimeField()
    source_api = models.CharField(max_length=50, default='')
    source_data = models.CharField(max_length=50, default='')
    avg_day = models.CharField(max_length=50, default='')
    high_day = models.CharField(max_length=50, default='')
    low_day = models.CharField(max_length=50, default='')
    vol_crypto = models.CharField(max_length=50, default='')
    vol_currency = models.CharField(max_length=50, default='')
    last_price = models.CharField(max_length=50, default='')
    def __str__(self):
        return str(self.timestamp)

#Exchange Data Model
class Exchange(models.Model):
    name = models.CharField(max_length=100, default='')
    website_url = models.CharField(max_length=100, default='')
    country_origin = models.CharField(max_length=100, default='')
    idkey = models.CharField(max_length=4, default='cccc')
    api_url = models.CharField(max_length=100, default='')
    api_key = models.CharField(max_length=100, default='', blank=True)
    api_secret = models.CharField(max_length=100, default='', blank=True)
    def __str__(self):
        return self.name