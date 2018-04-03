from django.conf.urls import url, include
from .views import CreateView

urlpatterns = [
    url(r'^hifz/$', CreateView.as_view(), name="create"),

]