from selenium.webdriver.common.by import By


class OrdersListPageLocators:
    """Локаторы страницы «Лента заказов»."""

    # Заголовок страницы
    ORDERS_LIST_MAIN_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')

    # Кнопка «Конструктор» (переход обратно)
    BUTTON_CONSTRUCTOR = (By.XPATH, '//a/p[text()="Конструктор"]')

    # Счётчики заказов
    COMPLETED_ORDERS_FOR_ALL_TIME = (
        By.XPATH,
        "(//p[contains(@class, 'OrderFeed_number')])[1]",
    )
    COMPLETED_ORDERS_FOR_TODAY = (
        By.XPATH,
        "(//p[contains(@class, 'OrderFeed_number')])[2]",
    )

    # Номера заказов в разделе «В работе»
    ORDER_IDENTIFICATOR = (
        By.XPATH,
        '//ul[contains(@class, "OrderFeed_orderListReady")]/li',
    )