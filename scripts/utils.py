from dotenv import load_dotenv
import requests
import os
from loguru import logger

load_dotenv()

class Utils:
    AUTH_URL = 'https://auth.lynxlinkage.com'
    FUGLE_URL = 'https://fugle.lynxlinkage.com'
    POSTREST_URL = 'https://postgrest.lynxlinkage.com'
    def __init__(self):
        self.session = requests.Session()
        payload = {
            "username": os.getenv("USERNAME"),
            "password": os.getenv("PASSWORD")
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.session.post(f"{Utils.AUTH_URL}/api/firstfactor", json=payload, headers=headers)
        if response.status_code == 200 and response.json().get("status") == "OK":
            logger.info("Login successful!")
        else:
            logger.error("Login failed!")
            raise Exception("Login failed!")
        
    def make_request(self, method, base_url, path, data=None, params=None, headers={}):
        endpoint = base_url + path
        headers = headers | {"Content-Type": "application/json"}
        logger.info(f"{method.upper()} request to: {endpoint}")

        # Determine the appropriate method to call
        request_method = getattr(self.session, method)
        logger.info(f"{method=}, {endpoint=}, {data=}, {params=}, {headers=}")
        response = request_method(endpoint, json=data, params=params, headers=headers)

        # Check for no content status
        if response.status_code == 204:
            logger.info(f"No content returned from: {endpoint}")
            return response.status_code, {}
        elif response.status_code < 200 or response.status_code > 299:
            logger.error(f"status code: {response.status_code}), method: {method.upper()}, endpoint: {endpoint}, data: {data}, params: {params}")
            return response.status_code, {}
        else:
            return response.status_code, response.json()
    
    # Wrapper methods
    def get(self, base_url, path, params=None, headers={}):
        return self.make_request('get', base_url, path, params=params, headers=headers)

    def post(self, base_url, path, data, headers={}):
        return self.make_request('post', base_url, path, data=data, headers=headers)

    def put(self, base_url, path, data, headers={}):
        return self.make_request('put', base_url, path, data=data, headers=headers)

    def delete(self, base_url, path, data=None, headers={}):
        return self.make_request('delete', base_url, path, data=data, headers=headers)


