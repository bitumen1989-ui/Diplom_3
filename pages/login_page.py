import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePageObjects
from urls import URLs


class LoginPageObjects(BasePageObjects):
    """Страница авторизации."""

    @allure.step("Ожидание загрузки страницы авторизации")
    def wait_for_load_login_page(self):
        self.wait_load_url(URLs.LOGIN_URL)

    @allure.step("Заполнение формы авторизации")
    def fill_authorization_form(self, data: dict):
        self.send_text(LoginPageLocators.EMAIL_FIELD, data["EMAIL"])
        self.send_text(LoginPageLocators.PASSWORD_FIELD, data["PASSWORD"])

    @allure.step("Клик по кнопке «Войти»")
    def click_button_authorization(self):
        self.click(LoginPageLocators.BUTTON_LOGIN)