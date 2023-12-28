import random
from selenium.webdriver.common.by import By

DISCOUNT_BLOCK = (By.XPATH, "//*[@id='hot-deal']/div/div/div/div/form/div[1]")
DISCOUNT_BLOCK_BTN = (By.XPATH, "//*[@id='hot-deal']/div/div/div/div/form/div[1]/lp/a")
FAVORITE_BTN = (By.XPATH, "//*[@id='tab2']/div[1]/div/div/div[9]/div[1]/form/div[2]/button")
PRODUCT_SHOP = (By.XPATH, "//*[@id='responsive-nav']/ul/li[2]/a")
BTN_PROD_SHOP = (
    By.CSS_SELECTOR, f'#store > div > div:nth-child([{random.randint(1, 9)}]) > div > div.add-to-cart > form > button')
PRODUCT_ELEMENT_SHOP = (By.CSS_SELECTOR, f'#store > div > div:nth-child({random.randint(1, 9)}) > div > a')
VIEWED_ITEM = (By.XPATH, "//*[@id='tab1']/div[1]/div/div/div/div[1]/h3/a[2]")


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.header = None
        self.discount_block = None
        self.discount_block_btn = None
        self.favorite_btn = None
        self.product_btn_shop = None
        self.product_ele_shop = None
        self.viewed_item = None

    def get_discount_block(self):  # gpstrip
        if not self.discount_block:
            self.discount_block = self.driver.find_element(*DISCOUNT_BLOCK)
        return self.discount_block

    def get_discount_block_btn(self):  # gpstrip
        if not self.discount_block_btn:
            self.discount_block_btn = self.driver.find_element(*DISCOUNT_BLOCK_BTN)
        return self.discount_block_btn

    def get_favorite_btn(self):  # gpstrip
        if not self.favorite_btn:
            self.driver.implicitly_wait(10)
            self.favorite_btn = self.driver.find_element(*FAVORITE_BTN)
        return self.favorite_btn

    def get_product_ele_shop(self):  # gpstrip
        if not self.product_ele_shop:
            self.product_ele_shop = self.driver.find_element(*PRODUCT_ELEMENT_SHOP)
        return self.product_ele_shop

    def get_product_btn_shop(self):  # gpstrip
        if not self.product_btn_shop:
            self.product_btn_shop = self.driver.find_element(*BTN_PROD_SHOP)
        return self.product_btn_shop

    def get_viewed_item(self):  # gpstrip
        if not self.viewed_item:
            self.viewed_item = self.driver.find_element(*VIEWED_ITEM)
        return self.viewed_item
