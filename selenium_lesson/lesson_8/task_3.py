import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cookie_manager import CookieManager

CARD_PRODUCT_LOCATOR = ('xpath', "//div[@class='img-wrapper']")
ADD_BASKET_LOCATOR = ('xpath', "//button[@title='Добавить в корзину']")
CART_BUTTON_LOCATOR = ('xpath', "//div[contains(@class,'tab-cart')]")
COUNT_PRODUCT_IN_CART_LOCATOR = ('xpath', "//span[contains(@class,'cart__counter')]")

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1200')
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)
cookie_manager = CookieManager(driver)

driver.get('https://www.mvideo.ru/')

# открыть карточку товара
open_card = wait.until(EC.element_to_be_clickable(CARD_PRODUCT_LOCATOR))
open_card.click()

# добавить товар в корзину
add_basket = wait.until(EC.element_to_be_clickable(ADD_BASKET_LOCATOR))
add_basket.click()
time.sleep(5)

# сохранение куки
cookie_manager.save()
# удаление куки
driver.delete_all_cookies()
driver.refresh()
# загрузки куки
cookie_manager.load()
driver.refresh()

# открытие корзины
cart_button = wait.until(EC.element_to_be_clickable(CART_BUTTON_LOCATOR))
cart_button.click()
time.sleep(5)

# проверка количества товара в корзине
count_product_in_cart = wait.until(EC.visibility_of_element_located(COUNT_PRODUCT_IN_CART_LOCATOR))
assert count_product_in_cart.text == "1"
