from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы (конструктора)."""

    # Кнопки навигации
    BUTTON_ORDERS_LIST = (By.XPATH, '//a/p[text()="Лента Заказов"]')
    BUTTON_CONSTRUCTOR = (By.XPATH, '//a/p[text()="Конструктор"]')

    # Ингредиент — булка
    INGREDIENT_BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')

    # Заголовок модального окна с деталями ингредиента
    INGREDIENT_DETAILS_MAIN_HEADER = (
        By.XPATH,
        '//h2[text()="Детали ингредиента"]',
    )

    # Кнопка закрытия модального окна
    CLOSE_BUTTON_INGREDIENT_DETAILS_WINDOW = (
        By.XPATH,
        '//button[contains(@class, "Modal_modal__close")]',
    )

    # Конструктор (куда перетаскивается ингредиент)
    INGREDIENTS_CONSTRUCTOR = (
        By.XPATH,
        '//ul[contains(@class, "BurgerConstructor_basket__list")]',
    )

    # Счётчик добавленного ингредиента
    INGREDIENT_COUNTER = (
        By.XPATH,
        '//p[contains(@class, "counter_counter__num")]',
    )

    # Номер заказа в модальном окне после оформления
    ORDER_IDENTIFICATOR = (
        By.XPATH,
        '//h2[contains(@class, "Modal_modal__title_shadow")]',
    )

    # Кнопка закрытия модального окна с номером заказа
    CLOSE_BUTTON_ORDER_IDENTIFICATOR = (
        By.XPATH,
        '//button[contains(@class, "Modal_modal__close")]',
    )

    # Кнопка «Оформить заказ»
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Анимация загрузки (мешает кликам)
    LOADING_ANIMATION = (By.XPATH, '//img[@alt="loading animation"]')

    # Модальное окно целиком (для ожидания закрытия)
    MODAL_WINDOW = (
        By.XPATH,
        '//div[@class="Modal_modal_overlay__x2ZCr"]',
    )