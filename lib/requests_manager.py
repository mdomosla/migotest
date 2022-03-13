import requests
from json.decoder import JSONDecodeError


class RequestManager(object):

    @staticmethod
    def post_request_with_headers(url, headers, payload):
        r = requests.request("POST", url, data=payload, headers=headers)
        try:
            resp = {"response": r.json(), "code": r.status_code}
        except JSONDecodeError:
            resp = {"response": r.reason, "code": r.status_code}
        return resp

    @staticmethod
    def get_request_with_headers(url, headers, payload):
        r = requests.request("GET", url, data=payload, headers=headers)
        try:
            resp = {"response": r.json(), "code": r.status_code}
        except JSONDecodeError:
            resp = {"response": r.reason, "code": r.status_code}
        return resp

    @staticmethod
    def put_request_with_headers(url, headers, payload):
        r = requests.request("PUT", url, data=payload, headers=headers)
        try:
            resp = {"response": r.json(), "code": r.status_code}
        except JSONDecodeError:
            resp = {"response": r.reason, "code": r.status_code}
        return resp

    @staticmethod
    def delete_request_with_headers(url, headers, payload):
        r = requests.request("DELETE", url, data=payload, headers=headers)
        try:
            resp = {"response": r.json(), "code": r.status_code}
        except JSONDecodeError:
            resp = {"response": r.reason, "code": r.status_code}
        return resp
