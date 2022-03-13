from tests.BaseTest import BaseTest
from lib.logger import Logger, whoami
from grappa import should
from lib.migoapi import MigoAPIClient
from lib.randoms import random_string, random_digits, random_chars_digits, get_date_without_space

log = Logger()


class TestApi(BaseTest):

    @classmethod
    def setup_class(cls):
        BaseTest().setup_class()

    def setup_method(self):
        whoami()
        self.testResult = False
        self.token = MigoAPIClient().get_token()[0]

    def test_01_add_client(self):
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        client_id = result[0]["id"]
        result[1] | should.be.equal.to(200)
        result = MigoAPIClient().get_client(self.token, client_id=client_id)
        result[1] | should.be.equal.to(200)
        result[0]["firstName"] | should.be.equal.to(client_first_name)
        result[0]["lastName"] | should.be.equal.to(client_last_name)
        result[0]["phone"] | should.be.equal.to(phone)
        result[0]["id"] | should.be.equal.to(client_id)
        self.testResult = True

    def teardown_method(self):
        whoami()

    @classmethod
    def teardown_class(cls):
        BaseTest().teardown_class()
