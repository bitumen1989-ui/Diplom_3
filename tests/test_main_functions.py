import allure

from pages.main_page import MainPageObjects
from pages.orders_list_page import OrdersListPageObjects
from urls import URLs


@allure.epic("UI-тестирование Stellar Burgers")
@allure.feature("Проверка основной функциональности")
class TestMainFunctions:

    @allure.story("Навигация")
    @allure.title("Переход по клику на «Лента заказов»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transition_to_orders_list_page(self, driver_main_page):
        main_page = MainPageObjects(driver_main_page)
        orders_list_page = OrdersListPageObjects(driver_main_page)

        main_page.wait_for_load_orders_list_text()
        main_page.click_button_orders_list()
        orders_list_page.wait_for_load_orders_list_page()

        assert orders_list_page.get_current_url() == URLs.ORDERS_LIST_URL

    @allure.story("Навигация")
    @allure.title("Переход по клику на «Конструктор»")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transition_to_main_page(self, driver_orders_list_page):
        orders_list_page = OrdersListPageObjects(driver_orders_list_page)
        main_page = MainPageObjects(driver_orders_list_page)

        orders_list_page.click_button_constructor()
        main_page.wait_for_load_main_page()

        assert orders_list_page.get_current_url() == URLs.BASE_URL

    @allure.story("Детали ингредиента")
    @allure.title("Клик по ингредиенту открывает всплывающее окно")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_details_window_appearance(self, driver_main_page):
        main_page = MainPageObjects(driver_main_page)

        main_page.click_ingredient_bun()
        assert main_page.wait_for_load_ingredient_details_main_header()

    @allure.story("Детали ингредиента")
    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_details_window_closing(self, driver_main_page):
        main_page = MainPageObjects(driver_main_page)

        main_page.click_ingredient_bun()
        main_page.wait_for_load_ingredient_details_main_header()
        main_page.wait_for_load_closing_element()
        main_page.click_close_button_ingredient_details_window()

        assert main_page.wait_for_invisibility_of_details_main_header()

    @allure.story("Счётчик ингредиента")
    @allure.title("Счётчик ингредиента увеличивается при добавлении")
    @allure.severity(allure.severity_level.NORMAL)
    def test_increasing_the_counter_of_ingredients(self, driver_main_page):
        main_page = MainPageObjects(driver_main_page)

        main_page.wait_for_load_ingredient_bun()
        old_counter = main_page.get_ingredient_counter()

        main_page.add_ingredients_into_constructor()
        new_counter = main_page.wait_ingredient_counter_increase(old_counter)

        # Булка в конструкторе учитывается как верх и низ,
        # поэтому счётчик увеличивается минимум на 1.
        assert new_counter > old_counter