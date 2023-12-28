import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from GpsTrip.ui.pages.base_page import BasePage

PRODUCT_ADD_CART = (By.XPATH, '/html/body/div[2]/div/div/div[3]/div/form/div/button')
SUCCESS_ADD_CART_MESS = (By.XPATH, '/html/body/div[1]/div')
PRICE_ITEM = (By.CSS_SELECTOR, "body > div:nth-child(12) > div > div > div:nth-child(3) > div > div:nth-child(3) > h4")
TEXT_ITEM = (By.CSS_SELECTOR, "body > div:nth-child(12) > div > div > div:nth-child(3) > div > h2")
FAVORITE_BTN = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div/ul[1]/li/a")


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_add_to_cart_btn(self) -> WebElement:  # gpstrip
        return self.driver.find_element(*PRODUCT_ADD_CART)

    def get_success_add_cart_mess(self) -> WebElement:  # gpstrip
        return self.driver.find_element(*SUCCESS_ADD_CART_MESS)

    def get_price_item(self) -> WebElement:  # gpstrip
        return self.driver.find_element(*PRICE_ITEM)

    def get_item_name(self) -> WebElement:  # gpstrip
        return self.driver.find_element(*TEXT_ITEM)

    def get_product_favorite_btn(self) -> WebElement:  # gpstrip
        return self.driver.find_element(*FAVORITE_BTN)
