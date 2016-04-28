# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
from requests.auth import HTTPBasicAuth


class AwesomebikesClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'http://localhost:8000/api/'
    resource_mapping = {'bikes': {'resource': 'bikes/'}}

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(AwesomebikesClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = HTTPBasicAuth(
            api_params.get('user'), api_params.get('password'))

        return params

Awesomebikes = generate_wrapper_from_adapter(AwesomebikesClientAdapter)
