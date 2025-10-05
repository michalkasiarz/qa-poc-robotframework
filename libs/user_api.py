# libs/user_api.py

import requests

class UserAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_user_by_id(self, user_id):
        url = f"{self.BASE_URL}/users/{user_id}"
        return requests.get(url)

    def get_all_users(self):
        return requests.get(f"{self.BASE_URL}/users")

    def create_user(self, payload):
        return requests.post(f"{self.BASE_URL}/users", json=payload)

    def delete_user(self, user_id):
        return requests.delete(f"{self.BASE_URL}/users/{user_id}")


# Module-level instance and wrapper functions so Robot Framework can import
# the module and expose these functions as keywords. Robot treats module-level
# functions as keywords (underscores -> spaces), but not class methods.
_api = UserAPI()

def get_user_by_id(user_id):
    return _api.get_user_by_id(user_id)

def get_user_json_by_id(user_id):
    resp = _api.get_user_by_id(user_id)
    return resp.json()

def get_all_users():
    return _api.get_all_users()

def create_user(payload):
    return _api.create_user(payload)

def delete_user(user_id):
    return _api.delete_user(user_id)
