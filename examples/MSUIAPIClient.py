# -*- coding: utf-8 -*-

import requests
import urllib.parse

# Python3 API client library.
#
#
# SYNOPSIS:
#
# import MSUIAPIClient
#
#
# CREATION: Create a MSUIAPIClient object:
#
# api = MSUIAPIClient.MSUIAPIClient("http://server.example.com:port")
#
# LOGIN:
#
# success = api.login('username', 'password')
# if success:
#     print ("Login successful")
# else:
#     print ("Login failed...")
#
# REQUESTS:
#
# Do a GET request.  Example: Get a list of users,
# and limit output to 10 user, and sort on username 
#
# getusers = api.do_get('/xhr/user', {'sort[limit]': '10', 'sort[order]': 'username'})
#
# Do a POST request.  Example: Add a user named "foobar", 
# with role_id 4 (eg. End-user), to domain mydomain.name with password auth disabled
#
# adduser = api.do_post('/xhr/user', {'username' : 'foobar', 'role_id': 4, 'domain': 'mydomain.name', 'password': ''})
#
# Do a PATCH request.  Example: Update user id 123, 
# to get role_id: 3 (eg. Realm-admin)
#
# updateuser = api.do_patch('/xhr/user/_id/123', {'role_id' : 3})
#
# Do a DELETE request.  Example: Delete user id 123
#
# deleteuser = api.do_delete('/xhr/user/_id/123')
#
# LOGOUT:
#
# api.logout()

class MSUIAPIClient:
    """A simple client-side library for accessing the MSUI API"""

    def __init__(self, url):
        self.session = requests.Session()
        # Remove trailing slashes from url
        url = url.rstrip('/')
        self.url = url

    def login(self, USERNAME, PASSWORD):
        """Log in to the API."""
        result = self.session.post(self.url + '/xhr/login', json={'username': USERNAME, 'password': PASSWORD})
        if result.status_code == 200:
             return True
        else:
            raise Exception

    def logout(self):
        """Logout from the API."""
        result = self.session.get(self.url + '/xhr/logout')
        self.session.cookies = None
        if result.status_code == 204:
            return True
        else:
            raise Exception

    def do_get(self, rel_url, params=None):
        """Do a GET request against the API server."""
        full_url = self.url + rel_url

        # Add params
        if type(params) is dict:
            full_url += '?' + urllib.parse.urlencode(params)

        result = self.session.get(full_url)
        return result.json()

    def do_post(self, rel_url, post_data):
        """Do a POST request against the API server. post_data should be a dictionary."""
        #print(post_data)
        result = self.session.post(self.url + rel_url, json=post_data)
        if result.status_code == 200:
            return result.json()
        else:
            raise Exception

    def do_patch(self, rel_url, patch_data):
        """Do a PATCH request against the API server. patch_data should be a dictionary."""
        result = self.session.patch(self.url + rel_url, json=patch_data)
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

