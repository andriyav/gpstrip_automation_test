import unittest

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from GpsTrip.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from GpsTrip.ui.pages.login_modal.login_modal import LoginModal
from tests.value_provider import ValueProvider

IMPLICITLY_WAIT = 5


class BaseTestRunner(unittest.TestCase):

    def setUp(self):
        self._init_driver()

    def _init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--window-size=1920x1080')

        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--window-size=1920x1080')
        # chrome_options.add_argument('--window-size=1920x1080')
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # driver.set_window_size(1920, 1080)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.driver.get(ValueProvider.get_base_url())

    def _login(self, email: str, password: str):
        HeaderUnauthorizedComponent(self.driver).click_authorisation_btn()  # gpstrip
        LoginModal(self.driver).set_email("andriyav@hotmail.com")
        LoginModal(self.driver).set_password("components12")
        LoginModal(self.driver).click_login_button()

    def tearDown(self):
        self.driver.quit()


class TestRunnerWithStudent(BaseTestRunner):
    def setUp(self):
        self._init_driver()
        self._login(ValueProvider.get_student_email(),
                    ValueProvider.get_student_password())


class TestRunnerWithTutor(BaseTestRunner):
    def setUp(self):
        self._init_driver()
        self._login(ValueProvider.get_email(),
                    ValueProvider.get_password())
