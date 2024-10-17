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
    
    def get(self, bath_url, path, params=None):
        endpoint = bath_url + path
        logger.info(f"Fetching data from: {endpoint}")
        response = self.session.get(endpoint, params=params)
        return response.status_code, response.json()
    
    def post(self, bath_url, path, data):
        endpoint = bath_url + path
        logger.info(f"Create data to: {endpoint}")
        response = self.session.post(endpoint, json=data)
        return response.status_code, response.json()
    
    def put(self, bath_url, path, data):
        endpoint = bath_url + path
        logger.info(f"Update data to: {endpoint}")
        response = self.session.put(endpoint, json=data)
        return response.status_code, response.json()
    
    def delete(self, bath_url, path):
        endpoint = bath_url + path
        logger.info(f"Delete data from: {endpoint}")
        response = self.session.delete(endpoint)
        return response.status_code, response.json()

    
