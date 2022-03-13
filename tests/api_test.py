from tests.BaseTest import BaseTest
from lib.logger import whoami
from grappa import should
from lib.migoapi import MigoAPIClient
from lib.randoms import random_string, random_digits, random_chars_digits, get_date_without_space



class TestApi(BaseTest):

    @classmethod
    def setup_class(cls):
        BaseTest().setup_class()
        token = MigoAPIClient().get_token()[0]["key"]
        MigoAPIClient().clear_all_clients(token)

    def setup_method(self):
        whoami()
        self.testResult = False
        self.token = MigoAPIClient().get_token()[0]["key"]

    def test_01_add_client(self):
        whoami()
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

    def test_02_edit_client_first_name(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        new_client_first_name = random_string(10)
        result = MigoAPIClient().put_client(self.token, client_id, new_client_first_name, client_last_name,
                                            phone)
        result[1] | should.be.equal.to(200)
        result = MigoAPIClient().get_client(self.token, client_id=client_id)
        result[1] | should.be.equal.to(200)
        result[0]["firstName"] | should.be.equal.to(new_client_first_name)
        result[0]["lastName"] | should.be.equal.to(client_last_name)
        result[0]["phone"] | should.be.equal.to(phone)
        result[0]["id"] | should.be.equal.to(client_id)
        self.testResult = True

    def test_03_edit_client_last_name(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        new_client_last_name = random_string(10)
        result = MigoAPIClient().put_client(self.token, client_id, client_first_name, new_client_last_name,
                                            phone)
        result[1] | should.be.equal.to(200)
        result = MigoAPIClient().get_client(self.token, client_id=client_id)
        result[1] | should.be.equal.to(200)
        result[0]["firstName"] | should.be.equal.to(client_first_name)
        result[0]["lastName"] | should.be.equal.to(new_client_last_name)
        result[0]["phone"] | should.be.equal.to(phone)
        result[0]["id"] | should.be.equal.to(client_id)
        self.testResult = True

    def test_04_edit_client_phone(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        new_phone = random_digits(5)
        result = MigoAPIClient().put_client(self.token, client_id, client_first_name, client_last_name,
                                            new_phone)
        result[1] | should.be.equal.to(200)
        result = MigoAPIClient().get_client(self.token, client_id=client_id)
        result[1] | should.be.equal.to(200)
        result[0]["firstName"] | should.be.equal.to(client_first_name)
        result[0]["lastName"] | should.be.equal.to(client_last_name)
        result[0]["phone"] | should.be.equal.to(new_phone)
        result[0]["id"] | should.be.equal.to(client_id)
        self.testResult = True

    def test_05_add_client_max_chars(self):
        whoami()
        client_first_name = random_string(50)
        client_last_name = random_string(50)
        phone = random_digits(50)
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

    def test_06_add_client_above_max_chars(self):
        whoami()
        client_first_name = random_string(51)
        client_last_name = random_string(51)
        phone = random_digits(51)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        client_id = result[0]["id"]
        result[1] | should.be.equal.to(200)
        result = MigoAPIClient().get_client(self.token, client_id=client_id)
        result[1] | should.be.equal.to(200)
        len(result[0]["firstName"]) | should.be.equal.to(50)
        len(result[0]["lastName"]) | should.be.equal.to(50)
        len(result[0]["phone"]) | should.be.equal.to(50)
        self.testResult = True

    def test_07_add_10_clients(self):
        MigoAPIClient().clear_all_clients(self.token)
        for _ in range(10):
            client_first_name = random_string(10)
            client_last_name = random_string(10)
            phone = random_digits(5)
            result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        len(MigoAPIClient().get_clients(self.token)[0]["clients"]) | should.be.equal.to(50)
        self.testResult = True

    def test_08_delete_client(self):
        whoami()
        client_first_name = random_string(51)
        client_last_name = random_string(51)
        phone = random_digits(51)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        client_id = result[0]["id"]
        result = MigoAPIClient().delete_client(self.token, client_id=client_id)
        result[1] | should.be.equal.to(200)
        result[0]["message"] | should.contain("client deleted")
        result = MigoAPIClient().get_client(self.token, client_id=client_id)
        result[1] | should.be.equal.to(404)
        result[0]["message"] | should.contain("client not found")
        self.testResult = True

    def test_09_add_client_no_name_data(self):
        whoami()
        client_first_name = ""
        client_last_name = ""
        phone = ""
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        result[0]["message"] | should.contain("firstName is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_10_add_client_no_last_name_data(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = ""
        phone = ""
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        result[0]["message"] | should.contain("lastName is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_11_add_client_no_phone_data(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = ""
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        result[1] | should.be.equal.to(400)
        result[0]["message"] | should.contain("phone is required")
        self.testResult = True

    def test_12_add_client_integer_data(self):
        whoami()
        client_first_name = int(get_date_without_space())
        client_last_name = int(get_date_without_space())
        phone = int(get_date_without_space())
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_13_edit_client_integer_data(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        new_client_first_name = int(get_date_without_space())
        new_client_last_name = int(get_date_without_space())
        new_phone = int(get_date_without_space())
        result = MigoAPIClient().put_client(self.token, client_id, new_client_first_name, new_client_last_name,
                                            new_phone)
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_14_edit_client_no_first_name_data(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        new_client_first_name = ""
        new_client_last_name = random_string(10)
        new_phone = random_digits(10)
        result = MigoAPIClient().put_client(self.token, client_id, new_client_first_name, new_client_last_name,
                                            new_phone)
        result[0]["message"] | should.contain("firstName is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_15_edit_client_no_last_name_data(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        new_client_first_name = random_string(10)
        new_client_last_name = ""
        new_phone = random_digits(10)
        result = MigoAPIClient().put_client(self.token, client_id, new_client_first_name, new_client_last_name,
                                            new_phone)
        result[0]["message"] | should.contain("lastName is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_16_edit_client_no_phone_data(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        new_client_first_name = random_string(10)
        new_client_last_name = random_string(10)
        new_phone = ""
        result = MigoAPIClient().put_client(self.token, client_id, new_client_first_name, new_client_last_name,
                                            new_phone)
        result[0]["message"] | should.contain("phone is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_17_get_token_invalid_creds(self):
        whoami()
        username = "username"
        passwd = "password"
        result = MigoAPIClient().get_token(custom_creds=True, login=username, passwd=passwd)
        result[0]["message"] | should.contain("invalid username or password")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_18_add_client_invalid_token(self):
        whoami()
        client_first_name = random_string(51)
        client_last_name = random_string(51)
        phone = random_digits(51)
        token = random_chars_digits(10)
        result = MigoAPIClient().add_client(token, client_first_name, client_last_name, phone)
        result[0]["message"] | should.contain("invalid or missing api key")
        result[1] | should.be.equal.to(403)
        self.testResult = True

    def test_19_edit_client_invalid_token(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        token = random_chars_digits(10)
        result = MigoAPIClient().put_client(token, client_id, client_first_name, client_last_name,
                                            phone)
        result[0]["message"] | should.contain("invalid or missing api key")
        result[1] | should.be.equal.to(403)
        self.testResult = True

    def test_20_delete_client_invalid_token(self):
        whoami()
        client_first_name = random_string(11)
        client_last_name = random_string(11)
        phone = random_digits(11)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        client_id = result[0]["id"]
        token = random_string(10)
        result = MigoAPIClient().delete_client(token, client_id=client_id)
        result[0]["message"] | should.contain("invalid or missing api key")
        result[1] | should.be.equal.to(403)
        self.testResult = True

    def test_21_add_client_wrong_body(self):
        whoami()
        wrong_payload = {
                    "test": "wrong",
                    "wrong": "wrong",
                    "payload": "wrong"
                }
        result = MigoAPIClient().add_client(self.token, custom_payload=True, payload=wrong_payload)
        result[0]["message"] | should.contain("firstName is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_22_add_client_wrong_body_proper_first_name(self):
        whoami()
        wrong_payload = {
                    "firstName": "wrong",
                    "wrong": "wrong",
                    "payload": "wrong"
                }
        result = MigoAPIClient().add_client(self.token, custom_payload=True, payload=wrong_payload)
        result[0]["message"] | should.contain("lastName is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_23_add_client_wrong_body_proper_names(self):
        whoami()
        wrong_payload = {
                    "firstName": "wrong",
                    "lastName": "wrong",
                    "payload": "wrong"
                }
        result = MigoAPIClient().add_client(self.token, custom_payload=True, payload=wrong_payload)
        result[0]["message"] | should.contain("phone is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_24_edit_client_wrong_body(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        wrong_payload = {
            "test": "wrong",
            "wrong": "wrong",
            "payload": "wrong"
        }
        result = MigoAPIClient().put_client(self.token, client_id, custom_payload=True, payload=wrong_payload)
        result[0]["message"] | should.contain("firstName is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_25_edit_client_wrong_body_proper_first_name(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        wrong_payload = {
            "firstName": "wrong",
            "wrong": "wrong",
            "payload": "wrong"
        }
        result = MigoAPIClient().put_client(self.token, client_id, custom_payload=True, payload=wrong_payload)
        result[0]["message"] | should.contain("lastName is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_26_edit_client_wrong_body_proper_names(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)[0]
        client_id = result["id"]
        wrong_payload = {
            "firstName": "wrong",
            "lastName": "wrong",
            "payload": "wrong"
        }
        result = MigoAPIClient().put_client(self.token, client_id, custom_payload=True, payload=wrong_payload)
        result[0]["message"] | should.contain("phone is required")
        result[1] | should.be.equal.to(400)
        self.testResult = True

    def test_27_delete_client_wrong_id(self):
        whoami()
        client_id = "definitely_wrong_id"
        result = MigoAPIClient().delete_client(self.token, client_id=client_id)
        result[0]["message"] | should.contain("client not found")
        result[1] | should.be.equal.to(404)
        self.testResult = True

    def test_28_get_client_wrong_id(self):
        whoami()
        client_id = "definitely_wrong_id"
        result = MigoAPIClient().get_client(self.token, client_id=client_id)
        result[0]["message"] | should.contain("client not found")
        result[1] | should.be.equal.to(404)
        self.testResult = True

    def test_29_edit_client_wrong_id(self):
        whoami()
        client_id = "definitely_wrong_id"
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().put_client(self.token, client_id, client_first_name, client_last_name,
                                            phone)
        result[0]["message"] | should.contain("client not found")
        result[1] | should.be.equal.to(404)
        self.testResult = True

    def test_30_get_client_wrong_token(self):
        whoami()
        client_first_name = random_string(10)
        client_last_name = random_string(10)
        phone = random_digits(5)
        result = MigoAPIClient().add_client(self.token, client_first_name, client_last_name, phone)
        client_id = result[0]["id"]
        token = random_string(10)
        result = MigoAPIClient().get_client(token, client_id=client_id)
        result[0]["message"] | should.contain("invalid or missing api key")
        result[1] | should.be.equal.to(403)
        self.testResult = True

    def test_31_get_clients_wrong_token(self):
        whoami()
        token = random_string(10)
        result = MigoAPIClient().get_clients(token)
        result[0]["message"] | should.contain("invalid or missing api key")
        result[1] | should.be.equal.to(403)
        self.testResult = True

    def teardown_method(self):
        whoami()

    @classmethod
    def teardown_class(cls):
        BaseTest().teardown_class()
