from django.contrib.auth.models import User

from rest_framework import authentication, permissions, viewsets
from rest_framework import generics # this is for the user views


from .serializers import HifzSerializer, UserSerializer
from .models import Hifz


class HifzViewSet(viewsets.ModelViewSet):
    queryset = Hifz.objects.all()
    serializer_class = HifzSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer