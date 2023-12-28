import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from GpsTrip.ui.pages.header.header_component import HeaderComponent
from GpsTrip.ui.pages.login_modal.login_modal import LoginModal

AUTH_BTN = (By.XPATH, "//*[@id='top-header']/div/ul[2]/li[2]/a")
SHOWROOM_BTN = (By.XPATH, "//*[@id='responsive-nav']/ul/li[1]/a")
CART = (By.XPATH, "//*[@id='header']/div/div/div[3]/div/div/div[2]/a/i")
DELETE_BTN = (By.XPATH, "//*[@id='header']/div/div/div[3]/div/div/div[2]/div/div[1]/div/a[2]/i")
DEL_MESSAGE = (By.XPATH, "/html/body/div[1]")
FAVORITE = (By.XPATH, "//*[@id='header']/div/div/div[3]/div/div/div[1]/a/i")
TEXT_IN_FAVORITE = (By.CSS_SELECTOR,
                    "#header > div > div > div.cart-manu > div > div > div.dropdown.open > div > div.cart-list > div > div.product-body > h3 > a")
DEL_FAVORITE_BTN = (By.XPATH, "//*[@id='header']/div/div/div[3]/div/div/div[1]/div/div[1]/div/a/i")
FAVORITE_NUMBER = (By.XPATH, "//*[@id='header']/div/div/div[3]/div/div/div[1]/a/div")
SHOP_BTN = (By.XPATH, "//*[@id='responsive-nav']/ul/li[2]/a")
ORDER_BTN = (By.XPATH, "//*[@id='header']/div/div/div[3]/div/div/div[2]/div/div[3]/a[2]")
LOGOUT_BTN = (By.XPATH, "//*[@id='top-header']/div/ul[2]/li[2]/a[2]")


class HeaderUnauthorizedComponent(HeaderComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_authorisation_btn(self) -> WebElement:
        return self.node.find_element(*AUTH_BTN)

    def click_authorisation_btn(self) -> LoginModal:
        self.get_authorisation_btn().click()
        return LoginModal(self.node)

    def get_logout_btn(self) -> WebElement:
        return self.node.find_element(*LOGOUT_BTN)

    def get_text_logout_btn(self) -> str:
        return self.node.find_element(*LOGOUT_BTN).text

    def get_showroom_btn(self) -> WebElement:
        return self.node.find_element(*SHOWROOM_BTN)

    def click_showroom_btn(self):
        return self.node.find_element(*SHOWROOM_BTN).click()

    def get_cart_btn(self) -> WebElement:
        return self.node.find_element(*CART)

    def get_del_btn(self) -> WebElement:
        return self.node.find_element(*DELETE_BTN)

    def get_del_message_txt(self) -> WebElement:
        return self.node.find_element(*DEL_MESSAGE)

    def get_favorite_btn_header(self) -> WebElement:
        return self.node.find_element(*FAVORITE)

    def get_text_in_favorite(self) -> WebElement:
        return self.node.find_element(*TEXT_IN_FAVORITE)

    def get_del_favorite_btn(self) -> WebElement:
        return self.node.find_element(*DEL_FAVORITE_BTN)

    def get_number_in_favorite(self) -> WebElement:
        return self.node.find_element(*FAVORITE_NUMBER)

    def get_shop_btn(self) -> WebElement:
        return self.node.find_element(*SHOP_BTN)

    def get_order_btn(self) -> WebElement:
        return self.node.find_element(*ORDER_BTN)
