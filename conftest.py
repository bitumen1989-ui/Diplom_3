import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from authorization_data import Data
from pages.login_page import LoginPageObjects
from pages.main_page import MainPageObjects
from pages.orders_list_page import OrdersListPageObjects
from urls import URLs


API_URL = "https://stellarburgers.education-services.ru/api"


def _create_user() -> dict:
    """Создаёт уникального пользователя через API."""
    import random
    email = f"test_{random.randint(10000, 99999)}@yandex.ru"
    password = "password123"
    name = "TestUser"

    payload = {"email": email, "password": password, "name": name}
    requests.post(f"{API_URL}/auth/register", json=payload)

    return payload


def _delete_user(email: str, password: str) -> None:
    """Удаляет пользователя через API."""
    login_response = requests.post(
        f"{API_URL}/auth/login",
        json={"email": email, "password": password},
    )
    if login_response.status_code == 200:
        token = login_response.json()["accessToken"]
        requests.delete(f"{API_URL}/auth/user", headers={"Authorization": token})


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    """Параметризованный драйвер Chrome / Firefox."""
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def test_user():
    """Создаёт пользователя через API и удаляет после теста."""
    user = _create_user()
    yield user
    _delete_user(user["email"], user["password"])


@pytest.fixture(scope="function")
def driver_main_page(driver):
    """Открывает главную страницу."""
    driver.get(URLs.BASE_URL)
    MainPageObjects(driver).wait_for_load_main_page()
    return driver


@pytest.fixture(scope="function")
def driver_orders_list_page(driver):
    """Открывает страницу «Лента заказов»."""
    driver.get(URLs.ORDERS_LIST_URL)
    OrdersListPageObjects(driver).wait_for_load_orders_list_page()
    return driver


@pytest.fixture(scope="function")
def driver_login_page(driver):
    """Открывает страницу авторизации."""
    driver.get(URLs.LOGIN_URL)
    LoginPageObjects(driver).wait_for_load_login_page()
    return driver


@pytest.fixture(scope="function")
def driver_orders_list_page_authorized(driver, test_user):
    """
    Логинит пользователя через UI и возвращает кортеж:
    (driver, счётчик «за всё время», счётчик «за сегодня»).
    """
    Data.DATA_SET["EMAIL"] = test_user["email"]
    Data.DATA_SET["PASSWORD"] = test_user["password"]
    Data.DATA_SET["NAME"] = test_user["name"]

    login_page = LoginPageObjects(driver)
    main_page = MainPageObjects(driver)
    orders_list_page = OrdersListPageObjects(driver)

    driver.get(URLs.LOGIN_URL)
    login_page.wait_for_load_login_page()
    login_page.fill_authorization_form(Data.DATA_SET)
    login_page.click_button_authorization()

    main_page.wait_for_load_main_page()
    main_page.wait_for_load_ingredient_bun()

    main_page.click_button_orders_list()
    orders_list_page.wait_for_load_orders_list_page()
    orders_list_page.wait_for_load_orders_list_page_header()

    old_total = orders_list_page.get_completed_orders_all_time()
    old_today = orders_list_page.get_completed_orders_today()

    orders_list_page.click_button_constructor()
    main_page.wait_for_load_main_page()

    return driver, old_total, old_today