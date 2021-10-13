import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from flask_testing import LiveServerTestCase

from server import create_app


class TestBase(LiveServerTestCase):

    def create_app(self):
        app = create_app({"TESTING": True})
        app.config.update(
            LIVESERVER_PORT=8943
        )
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())  

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = self.driver.get(self.get_server_url() + "/index")
        time.sleep(2)
