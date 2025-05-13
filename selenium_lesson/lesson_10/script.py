import time
from selenium import webdriver

HYPERSKILL_LOCATOR = ('xpath', "//span[normalize-space()='Reset password']")
AVITO_LOCATOR = ('xpath', "//div[@data-marker='header-navigation']")
OZON_LOCATOR = ('xpath', "//img[@alt='Ozon']")

options = webdriver.ChromeOptions()

options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# открытие вкладок
driver = webdriver.Chrome(options=options)
driver.switch_to.new_window('tab')
driver.switch_to.new_window('tab')

# получение списка табов
windows_list = driver.window_handles

# переход по ссылкам в табах
driver.switch_to.window(windows_list[0])
driver.get('https://hyperskill.org/login')

driver.switch_to.window(windows_list[1])
driver.get('https://www.avito.ru/')

driver.switch_to.window(windows_list[2])
driver.get('https://www.ozon.ru/')

time.sleep(3)

# Вывести в терминал title каждой страницы
for window in windows_list:
    driver.switch_to.window(window)
    print(driver.title)

# Кликнуть на любую кнопку или ссылку на каждой странице
for index in range(len(windows_list)):
    driver.switch_to.window(windows_list[index])
    if index == 0:
        driver.find_element(*HYPERSKILL_LOCATOR).click()
    elif index == 1:
        driver.find_element(*AVITO_LOCATOR).click()
    elif index == 2:
        driver.find_element(*OZON_LOCATOR).click()
