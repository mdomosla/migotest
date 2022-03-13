import json
import base64
from lib.requests_manager import RequestManager
from lib.logger import Logger

log = Logger()


class MigoAPIClient(RequestManager):
    def __init__(self):
        self.user = "egg"
        self.password = "f00BarbAz!"
        self.url = "https://qa-interview-api.migo.money"

    def create_authorization_header(self, string):
        auth = str(base64.b64encode(bytes(string, 'utf-8')), 'ascii').strip()
        headers = {
            "Authorization": f"Basic {auth}"
        }
        return headers

    def get_token(self, custom_creds=False, login=None, passwd=None):
        if custom_creds:
            login_creds = f"{login}:{passwd}"
        else:
            login_creds = f"{self.user}:{self.password}"
        payload = {}
        headers = self.create_authorization_header(login_creds)
        token_url = f"{self.url}/token"
        log.logger("INFO", "Creating new access token")
        resp = self.post_request_with_headers(token_url, headers=headers, payload=payload)
        return resp["response"], resp["code"]

    def get_clients(self, token):
        payload = {}
        headers = {"X-API-KEY": token}
        clients_url = f"{self.url}/clients"
        log.logger("INFO", "Getting all clients")
        resp = self.get_request_with_headers(clients_url, headers=headers, payload=payload)
        return resp["response"], resp["code"]

    def get_client(self, token, client_id):
        payload = {}
        headers = {"X-API-KEY": token}
        client_url = f"{self.url}/client/{client_id}"
        log.logger("INFO", f"Getting info for client id {client_id}")
        resp = self.get_request_with_headers(client_url, headers=headers, payload=payload)
        return resp["response"], resp["code"]

    def add_client(self, token, client_first_name=None, client_last_name=None, client_phone=None, custom_payload=False,
                   payload=None):
        if custom_payload:
            payload = json.dumps(payload)
        else:
            payload = json.dumps(
                {
                    "firstName": client_first_name,
                    "lastName": client_last_name,
                    "phone": client_phone
                }
            )
        client_url = f"{self.url}/client"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            "X-API-KEY": token
        }
        log.logger("INFO", f"Adding client: {client_first_name}, {client_last_name}, {client_phone}")
        resp = self.post_request_with_headers(client_url, headers=headers, payload=payload)
        return resp["response"], resp["code"]

    def put_client(self, token, client_id, client_first_name=None, client_last_name=None, client_phone=None,
                   custom_payload=False, payload=None):
        client_url = f"{self.url}/client/{client_id}"
        if custom_payload:
            payload = json.dumps(payload)
        else:
            payload = json.dumps(
                {
                    "firstName": client_first_name,
                    "lastName": client_last_name,
                    "phone": client_phone
                }
            )
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            "X-API-KEY": token
        }
        log.logger("INFO", f"Editing data for client id: {client_id}, data: {client_first_name}, {client_last_name}, "
                           f"{client_phone}")
        resp = self.put_request_with_headers(client_url, headers=headers, payload=payload)
        return resp["response"], resp["code"]

    def delete_client(self, token, client_id):
        client_url = f"{self.url}/client/{client_id}"
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            "X-API-KEY": token
        }
        log.logger("INFO", f"Deleting client {client_id}")
        resp = self.delete_request_with_headers(client_url, headers=headers, payload=payload)
        return resp["response"], resp["code"]

    def clear_all_clients(self, token):
        clients = self.get_clients(token)[0]
        while len(clients["clients"]) > 0:
            self.delete_client(token, clients["clients"][0]["id"])
            clients = self.get_clients(token)[0]
