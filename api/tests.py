from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory

from .views import GeneSuggest
# Create your tests here.


def setUp():
    factory = APIRequestFactory()
    url = '/gene_suggest'
    view = GeneSuggest.as_view()

    return factory, url, view


def test_valid_params():
    valid_params = [{
        'query': 'brc',
        'species': 'homo_sapiens',
        'limit': '10'
    },
        {
        'query': 'brc',
        'species': 'gorilla_gorilla',
        'limit': '20'
    },
        {
        'query': 'brc',
        'species': 'chelonoidis_abingdonii',
        'limit': '20'
    }]

    factory, url, view = setUp()

    for params in valid_params:
        request = factory.get(url, params)
        response = view(request)

        assert response.status_code == 200
        assert isinstance(response.data, list)


def test_invalid_params():
    invalid_params = [{
        'query': 'brc',
        'species': 'homo_sapiens'
    },
        {
        'query': 'brc'
    }]

    factory, url, view = setUp()

    for params in invalid_params:
        request = factory.get(url, params)
        response = view(request)

        assert response.status_code == 400
        assert isinstance(response.data, dict)


test_valid_params()
test_invalid_params()
