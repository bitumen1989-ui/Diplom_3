from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы страницы авторизации."""

    REGISTER_MAIN_HEADER = (By.XPATH, '//h2[text()="Вход"]')
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')