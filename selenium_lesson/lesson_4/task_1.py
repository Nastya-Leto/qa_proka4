import time
from selenium import webdriver

field_full_name_locator = ('xpath', "//input[@id='userName']")
field_email_locator = ('xpath', "//input[@id='userEmail']")
field_current_address_locator = ('xpath', "//textarea[@id='currentAddress']")
field_permanent_address_locator = ('xpath', "//textarea[@id='permanentAddress']")

driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')

field_full_name = driver.find_element(*field_full_name_locator)
field_full_name.clear()
field_full_name.send_keys('Котик Котович')
assert field_full_name.get_attribute('value') == 'Котик Котович'

field_email = driver.find_element(*field_email_locator)
field_email.clear()
field_email.send_keys('kot@mail.ru')
assert field_email.get_attribute('value') == 'kot@mail.ru'

field_current_address = driver.find_element(*field_current_address_locator)
field_current_address.clear()
field_current_address.send_keys('Samara')
assert field_current_address.get_attribute('value') == 'Samara'

field_permanent_address = driver.find_element(*field_permanent_address_locator)
field_permanent_address.clear()
field_permanent_address.send_keys('Moscow')
assert field_permanent_address.get_attribute('value') == 'Moscow'

time.sleep(3)
driver.quit()
