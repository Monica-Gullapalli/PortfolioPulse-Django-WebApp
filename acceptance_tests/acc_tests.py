from django.test import TestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

class AcceptanceTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            cls.selenium = webdriver.Chrome()
        except WebDriverException as e:
            raise Exception(f"Error initializing WebDriver: {e}")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.base_url = "http://127.0.0.1:8000"

    def tearDown(self):
        # No need to quit the WebDriver here if we're doing it in tearDownClass.
        super().tearDown()

    def test_user_signup(self):
        self.selenium.get(f"{self.base_url}/usignup/")
        # Your user signup test code here

    def test_user_login(self):
        self.selenium.get(f"{self.base_url}/ulogin/")
        # Your user login test code here

    def test_user_logout(self):
        self.selenium.get(f"{self.base_url}/ulogout/")
        # Your user logout test code here
