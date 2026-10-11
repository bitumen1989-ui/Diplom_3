import allure

from pages.main_page import MainPageObjects
from pages.orders_list_page import OrdersListPageObjects


@allure.epic("UI-тестирование Stellar Burgers")
@allure.feature('Проверка раздела «Лента заказов»')
class TestOrdersListSection:

    @allure.story("Счётчики заказов")
    @allure.title('Счётчик «Выполнено за всё время» увеличивается при создании заказа')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_increasing_counter_for_all_time(self, driver_orders_list_page_authorized):
        driver = driver_orders_list_page_authorized[0]
        old_total = driver_orders_list_page_authorized[1]

        main_page = MainPageObjects(driver)
        orders_list_page = OrdersListPageObjects(driver)

        main_page.wait_for_load_main_page()
        main_page.wait_for_load_ingredient_bun()
        main_page.add_ingredients_into_constructor()
        main_page.wait_for_load_ingredient_in_constructor()

        main_page.click_order_button()
        main_page.wait_for_load_order_identificator()

        main_page.click_close_button_order_identificator_window()
        main_page.wait_for_ending_animation_of_loading()
        main_page.wait_for_closing_modal_window()

        main_page.click_button_orders_list()
        orders_list_page.wait_for_load_orders_list_page()
        orders_list_page.wait_for_load_orders_list_page_header()

        assert orders_list_page.wait_completed_orders_all_time_increase(old_total) > old_total

    @allure.story("Счётчики заказов")
    @allure.title('Счётчик «Выполнено за сегодня» увеличивается при создании заказа')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_increasing_counter_for_today(self, driver_orders_list_page_authorized):
        driver = driver_orders_list_page_authorized[0]
        old_today = driver_orders_list_page_authorized[2]

        main_page = MainPageObjects(driver)
        orders_list_page = OrdersListPageObjects(driver)

        main_page.wait_for_load_main_page()
        main_page.wait_for_load_ingredient_bun()
        main_page.add_ingredients_into_constructor()
        main_page.wait_for_load_ingredient_in_constructor()

        main_page.click_order_button()
        main_page.wait_for_load_order_identificator()

        main_page.click_close_button_order_identificator_window()
        main_page.wait_for_ending_animation_of_loading()
        main_page.wait_for_closing_modal_window()

        main_page.click_button_orders_list()
        orders_list_page.wait_for_load_orders_list_page()
        orders_list_page.wait_for_load_orders_list_page_header()

        assert orders_list_page.wait_completed_orders_today_increase(old_today) > old_today

    @allure.story("Заказы в работе")
    @allure.title('Номер заказа появляется в разделе «В работе»')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_number_appearance_in_orders_list_section(self, driver_orders_list_page_authorized):
        driver = driver_orders_list_page_authorized[0]

        main_page = MainPageObjects(driver)
        orders_list_page = OrdersListPageObjects(driver)

        main_page.wait_for_load_main_page()
        main_page.wait_for_load_ingredient_bun()
        main_page.add_ingredients_into_constructor()
        main_page.wait_for_load_ingredient_in_constructor()

        main_page.click_order_button()
        main_page.wait_for_load_order_identificator()

        main_page.click_close_button_order_identificator_window()
        main_page.wait_for_ending_animation_of_loading()
        main_page.wait_for_closing_modal_window()

        main_page.click_button_orders_list()
        orders_list_page.wait_for_load_orders_list_page()
        orders_list_page.wait_for_load_orders_list_page_header()

        assert orders_list_page.wait_any_order_in_progress()