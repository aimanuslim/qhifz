from django.db import models
from django.conf import settings
from json import load
from pydash import pluck
import datetime
from dateutil import parser

# Create your models here.
class Hifz(models.Model):
    with open('api/data/surahs.json', 'r', encoding='utf8') as f:
        surah_data = load(f)
        surah_array = surah_data['data']
    surah_array = tuple(zip(pluck(surah_array, 'number'), pluck(surah_array, 'englishName')))

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    ayat_number = models.IntegerField()
    surah = models.IntegerField()
    last_refreshed = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __init__(self, surah, ayat_number, last_refreshed=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.surah = surah - 1
        self.ayat_number = ayat_number
        if not last_refreshed:
            self.last_refreshed = datetime.datetime.now()
        else: self.last_refreshed = parser.parse(last_refreshed)

    def getSurahNameString(self):
        return self.surah_array[self.surah][1]

    def getLastRefreshed(self):
        if (type(self.last_refreshed) != datetime.datetime): raise TypeError()
        return self.last_refreshed

    def setLastRefreshed(self, time):
        if (type(time) != datetime.datetime): raise TypeError()
        self.last_refreshed = time
