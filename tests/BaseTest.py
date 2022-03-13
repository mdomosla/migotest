from lib.logger import whoami, Logger

log = Logger()

class BaseTest:

    @classmethod
    def setup_class(cls):
        whoami()
        log.logger('INFO', 'New test suite started')

    @classmethod
    def teardown_class(cls):
        whoami()
        log.logger('INFO', 'Test suite finished')
