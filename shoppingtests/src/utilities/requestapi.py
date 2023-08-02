import requests
import os
import json
from requests_oauthlib import OAuth1
import logging as logger

from shoppingtests.src.configs.hosts_config import API_HOSTS
from shoppingtests.src.utilities.credentialUtilities import CredentialUtilities

class RequestApi(object):
    def __init__(self):

        # self.env = os.environ.get("ENV", "test")
        wc_credentials = CredentialUtilities.get_api_keys()
        self.auth = OAuth1(wc_credentials["wc_key"], wc_credentials["wc_secret"])
        self.base_url = API_HOSTS['test']



    # def assert_status_code(self, status_code):
    #     self.status_code = status_code
    #    assert self.status_code == self.expected_status_code, f'Bad response code '

    def post(self, endpoint, headers=None, payload=None, expected_status_code=201):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.rs_json = rs_api.json()
        self.status_code = rs_api.status_code
        assert self.status_code == expected_status_code, "Bad response code"

        logger.debug(f'POST API response: {rs_api.json()}')
        return self.rs_json

    def get(self, endpoint, headers=None, payload=None, expected_status_code=201):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.get(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.rs_json = rs_api.json()
        logger.debug(f'GET API response: {rs_api.json()}')
        return self.rs_json
