import re
import time

import allure
import pytest
from selenium.webdriver.support.ui import Select

from GpsTrip.ui.pages.base_page import BasePage
from GpsTrip.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from GpsTrip.ui.pages.order.order import OrderPage
from GpsTrip.ui.pages.product.product_page import ProductPage
from tests.test_runners import TestRunnerWithTutor
from GpsTrip.ui.pages.login_modal.login_modal import LoginModal
from tests.test_runners import BaseTestRunner


class AuthorizedPageTestCase(TestRunnerWithTutor):


    @allure.step('Verify that a Student can find a tutor by name at the welcoming block')
    def test_add_product_to_cart_from_base_page_add_message(self):
        HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        BasePage(self.driver).get_discount_block().click()
        ProductPage(self.driver).get_product_add_to_cart_btn().click()
        message = ProductPage(self.driver).get_success_add_cart_mess().text
        HeaderUnauthorizedComponent(self.driver).get_cart_btn().click()
        HeaderUnauthorizedComponent(self.driver).get_del_btn().click()
        self.assertEqual("Товар добавлено до корзини\n×", message)

    # test the message that the number of item is increased in case of repeatable adding to cart
    @allure.step
    def test_add_product_to_cart_from_base_page_increased_count(self):
        HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        BasePage(self.driver).get_discount_block().click()
        ProductPage(self.driver).get_product_add_to_cart_btn().click()
        ProductPage(self.driver).get_product_add_to_cart_btn().click()
        message = ProductPage(self.driver).get_success_add_cart_mess().text
        HeaderUnauthorizedComponent(self.driver).get_cart_btn().click()
        HeaderUnauthorizedComponent(self.driver).get_del_btn().click()
        self.assertEqual("Кількість товару в корзині збільшена1\n×", message)

    def test_delete_product_from_header_cart(self):
        HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        BasePage(self.driver).get_discount_block().click()
        ProductPage(self.driver).get_product_add_to_cart_btn().click()
        HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        HeaderUnauthorizedComponent(self.driver).get_cart_btn().click()
        HeaderUnauthorizedComponent(self.driver).get_del_btn().click()
        time.sleep(2)
        text_del_message = HeaderUnauthorizedComponent(self.driver).get_del_message_txt().text
        self.assertEqual("Товар було видалено з корзини\n×", text_del_message)

    def test_add_favorite(self):
        HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        BasePage(self.driver).get_discount_block().click()
        ProductPage(self.driver).get_product_favorite_btn().click()
        # HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        HeaderUnauthorizedComponent(self.driver).get_favorite_btn_header().click()
        time.sleep(1)
        text_in_favorite = HeaderUnauthorizedComponent(self.driver).get_text_in_favorite().text
        HeaderUnauthorizedComponent(self.driver).get_del_favorite_btn().click()
        self.assertEqual("GPS ТРЕКЕР TK108", text_in_favorite)

    # check number of favorites

    def test_dell_favorite(self):
        HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        BasePage(self.driver).get_discount_block().click()
        ProductPage(self.driver).get_product_favorite_btn().click()
        HeaderUnauthorizedComponent(self.driver).get_favorite_btn_header().click()
        HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        HeaderUnauthorizedComponent(self.driver).get_favorite_btn_header().click()
        HeaderUnauthorizedComponent(self.driver).get_del_favorite_btn().click()
        text_del_message = HeaderUnauthorizedComponent(self.driver).get_del_message_txt()
        self.assertEqual("Товар було видалено з улюблених\n×", text_del_message.text)

    def test_number_favorite(self):
        HeaderUnauthorizedComponent(self.driver).get_favorite_btn_header().click()
        text_in_favorite = HeaderUnauthorizedComponent(self.driver).get_number_in_favorite()
        self.assertEqual("0", text_in_favorite.text)

    # Check if the price in cart is displayed correctly

    def test_add_product_to_cart_check_price(self):
        HeaderUnauthorizedComponent(self.driver).get_shop_btn().click()
        BasePage(self.driver).get_product_ele_shop().click()
        ProductPage(self.driver).get_product_add_to_cart_btn().click()
        text = ProductPage(self.driver).get_price_item().text
        match = re.search(r'\b(\d+)', text)
        price_item = int(match.group(1))
        HeaderUnauthorizedComponent(self.driver).get_cart_btn().click()
        HeaderUnauthorizedComponent(self.driver).get_order_btn().click()
        text2 = OrderPage(self.driver).get_sum_price().text
        match = re.search(r'\b(\d+)', text2)
        price_order = int(match.group(1))
        HeaderUnauthorizedComponent(self.driver).get_cart_btn().click()
        HeaderUnauthorizedComponent(self.driver).get_del_btn().click()
        self.assertEqual(price_item, price_order)

    def test_viewed(self):
        HeaderUnauthorizedComponent(self.driver).get_shop_btn().click()
        BasePage(self.driver).get_product_ele_shop().click()
        text_item = ProductPage(self.driver).get_item_name().text
        HeaderUnauthorizedComponent(self.driver).click_showroom_btn()
        text_viewed = BasePage(self.driver).get_viewed_item()
        self.assertEqual(text_item, text_viewed.text)

    def test_logout(self):
        HeaderUnauthorizedComponent(self.driver).get_logout_btn().click()
        text_account = HeaderUnauthorizedComponent(self.driver).get_authorisation_btn().text
        self.assertEqual(text_account, "Обліковий запис")


class UnauthorizedPageTestCase(BaseTestRunner):


    def test_login(self):
        (HeaderUnauthorizedComponent(self.driver).click_authorisation_btn())
        (LoginModal(self.driver).set_email("andriyav@hotmail.com"))
        (LoginModal(self.driver).set_password("components12"))
        (LoginModal(self.driver).click_login_button())
        text_logout_btn = HeaderUnauthorizedComponent(self.driver).get_text_logout_btn()
        self.assertEqual(text_logout_btn, "Вийти")

    def test_info_head(self):
        text_viewed = BasePage(self.driver).get_head_info_item().text
        self.assertEqual(text_viewed, "+38(096)1864719 andriyav@gmail.com Львів\nгрн. Обліковий запис")

    def test_search_category(self):
        select_element = BasePage(self.driver).get_category_search()
        select = Select(select_element)
        select.select_by_value('Автомобільний')
        auto_link = BasePage(self.driver).get_search_element().text
        self.assertEqual(auto_link, "GPS трекер TK103B")

    def test_about_us(self):
        text_about_us = BasePage(self.driver).get_about_us().text
        self.assertEqual(text_about_us, "Про нас")
