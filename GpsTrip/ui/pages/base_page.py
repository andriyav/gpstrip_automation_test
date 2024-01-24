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
HEAD_INFO = (By.ID, 'top-header')
SEARCH_CATEGORY = (By.NAME, "drop")
SEARCH_ELEMENT = (By.CSS_SELECTOR, "body > div.container > div > div > div > div:nth-child(1) > div > div > h3 > a")
ABOUT_TEXT = (By.LINK_TEXT, "Про нас")


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
        self.head_info_item = None
        self.category_search = None
        self.search_element = None
        self.about_us = None

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

    def get_head_info_item(self):  # gpstrip
        if not self.head_info_item:
            self.head_info_item = self.driver.find_element(*HEAD_INFO)
        return self.head_info_item

    def get_category_search(self):  # gpstrip
        if not self.category_search:
            self.category_search = self.driver.find_element(*SEARCH_CATEGORY)
        return self.category_search

    def get_search_element(self):  # gpstrip
        if not self.search_element:
            self.search_element = self.driver.find_element(*SEARCH_ELEMENT)
        return self.search_element

    def get_about_us(self):  # gpstrip
        if not self.about_us:
            self.about_us = self.driver.find_element(*ABOUT_TEXT)
        return self.about_us
