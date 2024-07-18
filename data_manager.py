import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customers_data = {}

    def get_destination_data(self):
        # Using the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self._prices_endpoint)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        # Updating the IATA code in the Google sheet for the preferred flights destination
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self._prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        # Getting registered customers emails from google sheet using Sheety API
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.customers_data = data["users"]
        return self.customers_data
