from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
driver.get('https://www.kufar.by/l')

new_cookie = {
    "name": "username",
    "value": "user123"
}

driver.add_cookie(new_cookie)
driver.refresh()

driver.delete_cookie('username')
driver.refresh()

cookies = driver.get_cookies()

for cookie in cookies:
    if 'username' in cookie.get('name'):
        print('Cookie "username" не была удалена')
else:
    print('Cookie "username" была удалена')
