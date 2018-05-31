from django.db import models
from django.conf import settings
from json import load
from pydash import pluck
import datetime
# from dateutil import parser

# Create your models here.
class Hifz(models.Model):
    with open('api/data/surahs.json', 'r', encoding='utf8') as f:
        surah_data = load(f)
        surah_array = surah_data['data']
    surah_array = tuple(zip(pluck(surah_array, 'number'), pluck(surah_array, 'englishName')))

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='hifz', on_delete=models.CASCADE)
    ayat_number = models.IntegerField()
    surah = models.IntegerField()
    last_refreshed = models.DateField(default=datetime.date.today)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



    def getSurahNameString(self):
        return self.surah_array[self.surah - 1][1]

    def getLastRefreshed(self):
        if (type(self.last_refreshed) != datetime.date): raise TypeError()
        return self.last_refreshed

    def setLastRefreshed(self, time):
        if (type(time) != datetime.date): raise TypeError()
        self.last_refreshed = time

