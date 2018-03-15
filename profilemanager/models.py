from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Core Website User Data Model
class UserProfile(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    local_currency = models.CharField(max_length=4, default='NZD')

    def __str__(self):
        return self.base_user.username

#Create UserProfile on any Django:User create event
def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = UserProfile.objects.create(django_user=kwargs['instance'])
post_save.connect(create_profile, sender=User)

class Crypto(models.Model):
    name = models.CharField(max_length=50, default='', unique=True)
    code = models.CharField(max_length=4, default='', unique=True)
    code_alt = models.CharField(max_length=4, default='', unique=True)

'''
"CreatedTimestampUtc ":UTC timestamp of when the data was generated,
"HistorySummaryItems":[ List of hourly summary blocks
{  
    "AverageSecondaryCurrencyPrice": Average traded price during hour
    "ClosingSecondaryCurrencyPrice": Last traded price in hour
    "StartTimestampUtc": UTC Start time of hour        
    "EndTimestampUtc": UTC End time of hour
    "HighestSecondaryCurrencyPrice": Highest traded price during hour
    "LowestSecondaryCurrencyPrice": Lowest traded price during hour
    "NumberOfTrades":Number of trades executed during hour
    "OpeningSecondaryCurrencyPrice": Opening traded price at start of hour
    "PrimaryCurrencyVolume": Volume of primary currency trade during hour
    "SecondaryCurrencyVolume": Volume of secondary currency traded during hour
}],
"NumberOfHoursInThePastToRetrieve": Number of past hours being returned,
"PrimaryCurrencyCode": The primary currency being shown
"SecondaryCurrencyCode": The secondary currency being used for pricing
'''
class DailyOHLCV(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, blank=True)
    currency = models.CharField(max_length=4, default='')
    avg_price = models.FloatField(default=0)
    day_start = models.DateTimeField()
    day_end = models.DateTimeField()
    source_api = models.CharField(max_length=50, default='', unique=True)
    source_data = models.CharField(max_length=50, default='', unique=True)
    open_value = models.FloatField(default=0)
    high_value = models.FloatField(default=0)
    low_value = models.FloatField(default=0)
    close_value = models.FloatField(default=0)
    volume = models.FloatField(default=0)


'''
"CreatedTimestampUtc ": UTC timestamp of when the market summary was generated
"CurrentHighestBidPrice": Current highest bid on order book
"CurrentLowestOfferPrice": Current lowest offer on order book
"DayAvgPrice": Weighted average traded price over last 24 hours
"DayHighestPrice": Highest traded price over last 24 hours
"DayLowestPrice": Lowest traded price over last 24 hours
"DayVolumeXbt": Volume of primary currency traded in last 24 hours
"DayVolumeXbtInSecondaryCurrrency": Volume of primary currency traded in last 24 hours for chosen secondary currency
"LastPrice": Last traded price
"PrimaryCurrencyCode": The primary currency being summarised
"SecondaryCurrencyCode": The secondary currency being used for pricing
'''
class SpotPrice(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, blank=True)
    currency = models.CharField(max_length=4, default='')
    timestamp = models.DateTimeField()
    source_api = models.CharField(max_length=50, default='', unique=True)
    source_data = models.CharField(max_length=50, default='', unique=True)
    avg_day = models.FloatField(default=0)
    high_day = models.FloatField(default=0)
    low_day = models.FloatField(default=0)
    vol_crypto = models.FloatField(default=0)
    vol_currency = models.FloatField(default=0)
    last_price = models.FloatField(default=0)


#Multi-Crypto Wallet Data Model
class Wallet(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    ethereum = models.FloatField(default=0)
    bitcoin = models.FloatField(default=0)
    bitcoincash = models.FloatField(default=0)

#Create Wallet on any UserProfile create event
def create_wallet(sender, **kwargs):
    if kwargs['created']:
        wallet = Wallet.objects.create(user_id=kwargs['instance'])
post_save.connect(create_wallet, sender=UserProfile)