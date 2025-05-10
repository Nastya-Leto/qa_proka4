from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

disappear_text_locator = ('xpath', "//div[@id='deletesuccess']")
displayed_text_locator = ('xpath', "//div[@id='delayedText']")
enabled_button_locator = ('xpath', "//input[@id='timerButton']")
disabled_button_locator = ('xpath', "//button[@id='myBtn']")
try_it_button_locator = ('xpath', "//button[text()='Try it']")

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)
driver.get('https://omayo.blogspot.com/')

# 1 Дождаться исчезновения текста
disappear_text = wait.until(EC.invisibility_of_element_located(disappear_text_locator), "disappear_text_locator")

# 2 Дождаться появления текста на странице
displayed_text = wait.until(EC.visibility_of_element_located(displayed_text_locator), 'displayed_text_locator')

# 3 Дождаться состояния enabled
enabled_button = wait.until(EC.element_to_be_clickable(enabled_button_locator), 'enabled_button_locator')

# 4 После клика дождаться состояния disabled
wait.until(EC.visibility_of_element_located(disabled_button_locator), 'disabled_button_locator')
try_it_button = wait.until(EC.visibility_of_element_located(try_it_button_locator))
try_it_button.click()
time.sleep(5)
wait.until(lambda _: driver.find_element(*disabled_button_locator).get_attribute('disabled'))
