import re

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePageObjects:
    """Базовый класс страницы с общими методами."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Поиск элемента: {locator}")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_element_visability(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание невидимости элемента: {locator}")
    def wait_element_invisability(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        self.wait_element_visability(locator)
        self.find(locator).click()

    @allure.step("Клик через JS по элементу: {locator}")
    def click_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Отправка текста '{text}' в элемент: {locator}")
    def send_text(self, locator, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание загрузки URL: {url}")
    def wait_load_url(self, url: str):
        self.wait.until(EC.url_to_be(url))

    @allure.step("Ожидание, что текст соответствует регулярке: {pattern}")
    def wait_text_matches(self, locator, pattern: str):
        self.wait.until(
            lambda _: bool(re.search(pattern, self.find(locator).text))
        )

    @allure.step("Drag-and-drop {source_locator} → {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        """Эмуляция HTML5 drag-and-drop через JS-события."""
        source = self.find(source_locator)
        target = self.find(target_locator)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            function createDragEvent(type, element) {
                const dataTransfer = new DataTransfer();
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                return element.dispatchEvent(event);
            }

            createDragEvent('dragstart', source);
            createDragEvent('drag', source);
            createDragEvent('dragenter', target);
            createDragEvent('dragover', target);
            createDragEvent('drop', target);
            createDragEvent('dragend', source);
        """, source, target)

    @allure.step("Получение текущего URL")
    def get_current_url(self) -> str:
        return self.driver.current_url