from selenium import webdriver
import time

from selenium.common import NoSuchElementException

field_username_locator = ('xpath', "//input[@id='username']")
field_password_locator = ('xpath', "//input[@id='password']")
login_button_locator = ('xpath', "//i[normalize-space()='Login']")
banner_locator = ('xpath', "//div[text()[normalize-space()='You logged into a secure area!']]")

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')

field_username = driver.find_element(*field_username_locator)
field_username.clear()
field_username.send_keys('tomsmith')

field_password = driver.find_element(*field_password_locator)
field_password.clear()
field_password.send_keys('SuperSecretPassword!')

login_button = driver.find_element(*login_button_locator)
login_button.click()

banner = driver.find_element(*banner_locator)
assert banner.is_enabled()

time.sleep(3)
driver.quit()
