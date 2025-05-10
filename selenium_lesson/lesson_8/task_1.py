from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(options=options)
driver.get('https://www.kufar.by/l')

new_cookie = {
    "name": "username",
    "value": "user123"
}

driver.add_cookie(new_cookie)
driver.refresh()

cookies = driver.get_cookies()
for cookie in cookies:
    if cookie.get('name') == new_cookie.get('name') and cookie.get('value') == new_cookie.get('value'):
        print('Новая cookie добавлена')
        break
else:
    print('Новая cookie не добавлена')
