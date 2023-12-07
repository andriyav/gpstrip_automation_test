import allure
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE = (By.XPATH, "./p")
CLOSE_BTN = (By.XPATH, "./button")
DESCRIPTION = (By.XPATH, "./div/p")
YES_BTN = (By.XPATH, "./div[2]/button[contains(text(), 'Yes')]")
NO_BTN = (By.XPATH, "./div[2]/button[contains(text(), 'No')]")


class PleaseConfirm(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._close_btn = None
        self._yes_btn = None
        self._no_btn = None

    @allure.step("Get title text")
    def get_title_text(self) -> str:
        return self.node.find_element(*TITLE).text

    @allure.step("Get close button")
    def get_close_button(self):
        if not self._close_btn:
            self._close_btn = self.node.find_element(*CLOSE_BTN)
        return self._close_btn

    @allure.step("Click on close button")
    def click_close(self):
        from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal
        self.get_close_button().click()
        return RegistrationModal(self.node.parent)

    @allure.step("Get description text")
    def get_description_text(self) -> str:
        return self.node.find_element(*DESCRIPTION).text

    @allure.step("Get 'Yes' button")
    def get_yes_btn(self):
        if not self._yes_btn:
            self._yes_btn = self.node.find_element(*YES_BTN)
            return self._yes_btn

    @allure.step("Click on 'Yes' button")
    def click_yes_btn(self):
        from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
        self.get_yes_btn().click()
        return HomePageGuest(self.node.parent)

    @allure.step("Get 'No' button")
    def get_no_btn(self):
        if not self._no_btn:
            self._no_btn = self.node.find_element(*NO_BTN)
            return self._no_btn

    @allure.step("Click on 'No' button")
    def click_no_btn(self):
        from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal
        self.get_no_btn().click()
        return RegistrationModal(self.node.parent)
