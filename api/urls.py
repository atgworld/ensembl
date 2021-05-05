# Contains all url patterns for api app

from django.urls import path
from .views import GeneSuggest

app_label = 'api'

urlpatterns = [
    path('gene_suggest', GeneSuggest.as_view(), name='gene_suggest')
]
