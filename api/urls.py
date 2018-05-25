from django.conf.urls import url, include
from .views import CreateView, DetailsView

urlpatterns = [
    url(r'^hifz/$', CreateView.as_view(), name="create"),
    url(r'^hifz/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
]