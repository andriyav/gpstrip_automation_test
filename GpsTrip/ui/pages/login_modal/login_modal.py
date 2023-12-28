import allure
from selenium.webdriver.common.by import By
from time import sleep


from GpsTrip.ui.elements.input import Input
from GpsTrip.ui.elements.input import PasswordInput
from GpsTrip.ui.elements.button import Button
from GpsTrip.ui.pages.base_component import BaseComponent

EMAIL_INPUT = (By.XPATH, '//*[@id="login-username"]') #gpstrip
PASSWORD_INPUT = (By.XPATH, '//*[@id="login-pwd"]')  #gpstrip
LOGIN_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/form/div/button")


class LoginModal(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._email_input = None
        self._password_input = None
        self._login_button = None


    def get_email_input(self):
        node = self.node.find_element(*EMAIL_INPUT)
        self._email_input = Input(node)
        return self._email_input


    def set_email(self, email: str):
        self.get_email_input().set_text(email)
        return self


    def get_password_input(self):
        if not self._password_input:
            node = self.node.find_element(*PASSWORD_INPUT)
            self._password_input = PasswordInput(node)
        return self._password_input


    def set_password(self, password: str):
        self.get_password_input().set_text(password)
        return self


    def get_login_button(self):
        node = self.node.find_element(*LOGIN_BUTTON)
        self._login_button = Button(node)
        return self._login_button


    def click_login_button(self):
        sleep(0.1)
        self.get_login_button().click_button()
        sleep(1)



