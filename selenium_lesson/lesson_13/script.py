from selenium_lesson.lesson_13.table_handler import TableHandler
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
table_handler = TableHandler

wait = WebDriverWait(driver, 15, poll_frequency=1)

FIELD_LOGIN_LOCATOR = ('xpath', "//label[text()='Логин']/following-sibling::div/input")
FIELD_PASSWORD_LOCATOR = ('xpath', "//label[text()='Пароль']/following-sibling::div/input")
LOGIN_BUTTON_LOCATOR = ('xpath', "//div[text()='Войти']")

driver.get('https://test-tm-app.dev.ts')

field_login = wait.until(EC.visibility_of_element_located(FIELD_LOGIN_LOCATOR))
field_login.send_keys('admin')

field_password = wait.until(EC.visibility_of_element_located(FIELD_PASSWORD_LOCATOR))
field_password.send_keys('pass')

login_button = wait.until(EC.visibility_of_element_located(LOGIN_BUTTON_LOCATOR))
login_button.click()
driver.get("https://test-tm-app.dev.ts/ais/file-exchange?tabId=SENT")
