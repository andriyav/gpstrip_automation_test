from selenium.webdriver import Keys
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from GpsTrip.ui.pages.base_component import BaseComponent

LIST_ITEMS = (By.XPATH, '/html/body/div[1]/div/header/div/ul')
LOGO = (By.XPATH, "/html/body/div[1]/div/header/div/a")
NAVIGATE_ELEMENTS = (By.XPATH, "/html/body/div[1]/div/header/div/ul/li")


class HeaderComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._navigate_elements = []

    def get_logo(self) -> WebElement:
        return self.node.find_element(*LOGO)

    def click_logo(self):
        self.get_logo().click()
