# -*- coding: utf-8 -*-

import requests
import urllib.parse

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Python3 API client library.
#
#
# SYNOPSIS:
#
# import HalonAPIClient
#
#
# CREATION: Create a HalonAPIClient object:
#
# api = HalonAPIClient.HalonAPIClient("https://server.example.com:port/api/version")
#
# REQUESTS:
#
# Do a GET request.  Example: Get
#
# api.do_get('/...', {'param1': 'xxx', 'param2': 'yyy'})
#
# Do a POST request.  Example: Add
#
# api.do_post('/...', {'data1' : 'foo', 'data2': 'bar'})
#
# Do a PUT request.  Example: Update
#
# api.do_put('/...', {'data1' : int})
#
# Do a DELETE request.  Example: Delete 
#
# api.do_delete('/...')


class HalonAPIClient:
    """A simple client-side library for accessing the Halon API"""

    def __init__(self, url):
        self.session = requests.Session()
        # Remove trailing slashes from url
        url = url.rstrip('/')
        self.url = url

    def login(self, USERNAME, PASSWORD):
        """Log in to the API."""
        result = self.session.get(self.url, auth=(USERNAME, PASSWORD), verify=True)
        if result.status_code == 200:
             return True
        else:
            raise Exception

    def do_get(self, rel_url, USERNAME, PASSWORD, params=None):
        """Do a GET request against the API server."""
        full_url = self.url + rel_url

        # Add params
        if type(params) is dict:
            full_url += '?' + urllib.parse.urlencode(params)

        result = self.session.get(full_url, auth=(USERNAME, PASSWORD), timeout=10)
        return result

    def do_post(self, rel_url, post_data):
        """Do a POST request against the API server. post_data should be a dictionary."""
        result = self.session.post(self.url + rel_url, json=post_data)
        if result.status_code == 200:
            return result.json()
        else:
            raise Exception

    def do_put(self, rel_url, put_data):
        """Do a PUT request against the API server. patch_data should be a dictionary."""
        result = self.session.put(self.url + rel_url, json=put_data)
        if result.status_code == 204:
            return True
        else:
            raise Exception

    def do_delete(self, rel_url):
        """Do a DELETE request against the API server. """
        result = self.session.delete(self.url + rel_url)
        if result.status_code == 204:
            return True
        else:
            raise Exception

