import requests


class RequestManager(object):

    @staticmethod
    def post_request_with_headers(url, headers, payload):
        r = requests.request("POST", url, data=payload, headers=headers)
        resp = {"response": r.json(), "code": r.status_code}
        return resp

    @staticmethod
    def get_request_with_headers(url, headers, payload):
        r = requests.request("GET", url, data=payload, headers=headers)
        resp = {"response": r.json(), "code": r.status_code}
        return resp

    @staticmethod
    def put_request_with_headers(url, headers, payload):
        r = requests.request("PUT", url, data=payload, headers=headers)
        resp = {"response": r.json(), "code": r.status_code}
        return resp

    @staticmethod
    def delete_request_with_headers(url, headers, payload):
        r = requests.request("DELETE", url, data=payload, headers=headers)
        resp = {"response": r.json(), "code": r.status_code}
        return resp
