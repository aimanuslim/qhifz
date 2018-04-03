from rest_framework import serializers
from .models import Hifz

class HifzSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hifz
        fields = ('id', 'surah', 'ayat_number', 'last_refreshed', 'created', 'modified')
        read_only_fields = ('created', 'modified')