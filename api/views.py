from django.shortcuts import render
from rest_framework import generics

from .serializers import HifzSerializer
from .models import Hifz

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = Hifz.objects.all()
    serializer_class = HifzSerializer

    def create_performance(self,serializer):
        # save the POST data when user creates a new hifz
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Hifz.objects.all()
    serializer_class = HifzSerializer