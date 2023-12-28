import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from GpsTrip.ui.pages.base_page import BasePage

SUM_PRICE_TXT = (By.CSS_SELECTOR,
                 "body > form > div > div > div > div.col-md-5.order-details > div.order-summary > div:nth-child(4) > div:nth-child(2) > strong")


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_sum_price(self) -> WebElement:  # gpstrip
        return self.driver.find_element(*SUM_PRICE_TXT)
