import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from locators.orders_list_page_locators import OrdersListPageLocators
from pages.base_page import BasePageObjects
from urls import URLs


class OrdersListPageObjects(BasePageObjects):
    """Страница «Лента заказов»."""

    @allure.step("Ожидание загрузки страницы «Лента заказов»")
    def wait_for_load_orders_list_page(self):
        self.wait_load_url(URLs.ORDERS_LIST_URL)

    @allure.step("Ожидание заголовка страницы «Лента заказов»")
    def wait_for_load_orders_list_page_header(self):
        self.wait_element_visability(OrdersListPageLocators.ORDERS_LIST_MAIN_HEADER)

    @allure.step("Переход на страницу «Конструктор»")
    def click_button_constructor(self):
        self.click(OrdersListPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Получение счётчика «Выполнено за всё время»")
    def get_completed_orders_all_time(self) -> int:
        self.wait_element_visability(
            OrdersListPageLocators.COMPLETED_ORDERS_FOR_ALL_TIME
        )
        return int(
            self.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_ALL_TIME).text
        )

    @allure.step("Получение счётчика «Выполнено за сегодня»")
    def get_completed_orders_today(self) -> int:
        self.wait_element_visability(
            OrdersListPageLocators.COMPLETED_ORDERS_FOR_TODAY
        )
        return int(
            self.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_TODAY).text
        )

    @allure.step("Ожидание увеличения счётчика «Выполнено за всё время»")
    def wait_completed_orders_all_time_increase(self, old_value: int) -> int:
        return self.wait.until(
            lambda _: int(
                self.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_ALL_TIME).text
            ) > old_value
            and int(
                self.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_ALL_TIME).text
            )
        )

    @allure.step("Ожидание увеличения счётчика «Выполнено за сегодня»")
    def wait_completed_orders_today_increase(self, old_value: int) -> int:
        return self.wait.until(
            lambda _: int(
                self.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_TODAY).text
            ) > old_value
            and int(
                self.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_TODAY).text
            )
        )

    @allure.step("Ожидание появления хотя бы одного заказа в разделе «В работе»")
    def wait_any_order_in_progress(self, timeout: int = 30) -> list:
        """
        Ожидает, что в разделе «В работе» появится хотя бы один заказ.
        Раздел показывает только первые заказы из очереди, поэтому
        конкретный номер может быть не виден — проверяем непустоту списка.
        """
        wait = WebDriverWait(self.driver, timeout)

        def non_empty_list(driver):
            elements = driver.find_elements(
                *OrdersListPageLocators.ORDER_IDENTIFICATOR
            )
            return [el.text for el in elements if el.text] or False

        try:
            return wait.until(non_empty_list)
        except TimeoutException:
            raise AssertionError(
                "В разделе «В работе» не появилось ни одного заказа за "
                f"{timeout} секунд"
            )