from django.contrib.auth.models import User
from rest_framework import permissions

from rest_framework import serializers
from .models import Hifz
from .permissions import IsOwnerOrReadOnly

class HifzSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    class Meta:
        model = Hifz
        fields = ('id', 'owner', 'surah', 'ayat_number', 'last_refreshed', 'created', 'modified')
        read_only_fields = ('created', 'modified')

class UserSerializer(serializers.ModelSerializer):
    hifz = serializers.PrimaryKeyRelatedField(many=True, queryset=Hifz.objects.all())


    class Meta:
        model = User
        fields = ('id', 'username', 'hifzs')


