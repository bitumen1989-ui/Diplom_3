import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePageObjects
from urls import URLs


class MainPageObjects(BasePageObjects):
    """Главная страница (конструктор)."""

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_main_page(self):
        self.wait_load_url(URLs.BASE_URL)

    @allure.step("Ожидание загрузки кнопки «Лента Заказов»")
    def wait_for_load_orders_list_text(self):
        self.wait_element_visability(MainPageLocators.BUTTON_ORDERS_LIST)

    @allure.step("Переход на страницу «Лента заказов»")
    def click_button_orders_list(self):
        self.click(MainPageLocators.BUTTON_ORDERS_LIST)

    @allure.step("Переход на страницу «Конструктор»")
    def click_button_constructor(self):
        self.click(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Клик по ингредиенту «Флюоресцентная булка R2-D3»")
    def click_ingredient_bun(self):
        self.click(MainPageLocators.INGREDIENT_BUN)

    @allure.step("Ожидание появления ингредиента на странице")
    def wait_for_load_ingredient_bun(self):
        self.wait_element_visability(MainPageLocators.INGREDIENT_BUN)
        return True

    @allure.step("Ожидание заголовка «Детали ингредиента»")
    def wait_for_load_ingredient_details_main_header(self):
        self.wait_element_visability(MainPageLocators.INGREDIENT_DETAILS_MAIN_HEADER)
        return True

    @allure.step("Ожидание кнопки закрытия модального окна")
    def wait_for_load_closing_element(self):
        self.wait_element_visability(
            MainPageLocators.CLOSE_BUTTON_INGREDIENT_DETAILS_WINDOW
        )

    @allure.step("Ожидание невидимости заголовка «Детали ингредиента»")
    def wait_for_invisibility_of_details_main_header(self):
        return self.wait_element_invisability(
            MainPageLocators.INGREDIENT_DETAILS_MAIN_HEADER
        )

    @allure.step("Закрытие модального окна с деталями ингредиента")
    def click_close_button_ingredient_details_window(self):
        self.click(MainPageLocators.CLOSE_BUTTON_INGREDIENT_DETAILS_WINDOW)

    @allure.step("Добавление булки в конструктор (drag-and-drop)")
    def add_ingredients_into_constructor(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_BUN,
            MainPageLocators.INGREDIENTS_CONSTRUCTOR,
        )

    @allure.step("Ожидание появления ингредиента в конструкторе")
    def wait_for_load_ingredient_in_constructor(self):
        self.wait_element_visability(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Получение значения счётчика ингредиента")
    def get_ingredient_counter(self) -> int:
        self.wait_element_visability(MainPageLocators.INGREDIENT_COUNTER)
        return int(self.find(MainPageLocators.INGREDIENT_COUNTER).text)

    @allure.step("Ожидание увеличения счётчика ингредиента")
    def wait_ingredient_counter_increase(self, old_value: int) -> int:
        return self.wait.until(
            lambda _: int(self.find(MainPageLocators.INGREDIENT_COUNTER).text) > old_value
            and int(self.find(MainPageLocators.INGREDIENT_COUNTER).text)
        )

    @allure.step("Ожидание появления номера заказа")
    def wait_for_load_order_identificator(self):
        self.wait_text_matches(MainPageLocators.ORDER_IDENTIFICATOR, r"^\d+")

    @allure.step("Получение номера заказа")
    def get_order_identificator(self) -> str:
        return self.find(MainPageLocators.ORDER_IDENTIFICATOR).text

    @allure.step("Клик по кнопке «Оформить заказ»")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Закрытие модального окна с номером заказа")
    def click_close_button_order_identificator_window(self):
        self.click_js(MainPageLocators.CLOSE_BUTTON_ORDER_IDENTIFICATOR)

    @allure.step("Ожидание завершения анимации загрузки")
    def wait_for_ending_animation_of_loading(self):
        return self.wait_element_invisability(MainPageLocators.LOADING_ANIMATION)

    @allure.step("Ожидание закрытия модального окна")
    def wait_for_closing_modal_window(self):
        return self.wait_element_invisability(MainPageLocators.MODAL_WINDOW)