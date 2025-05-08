import time
from selenium import webdriver

driver = webdriver.Chrome()

#Открыть любую страницу, например: vk.com.
driver.get('https://vk.com')

#Получить и вывести title в консоль.
print(driver.title)

#Открыть любую другую страницу, например: ya.ru.
driver.get('https://ya.ru')

#Получить и вывести title в консоль.
print(driver.title)

#Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
driver.back()
assert driver.title == 'ВКонтакте | Добро пожаловать'

#Сделать рефреш страницы.
driver.refresh()

#Получить и вывести URL-адрес текущей страницы.
first_url = driver.current_url
print(first_url)

#Вернуться "вперед" на страницу из пункта 4.
driver.forward()

#Убедиться, что URL-адрес изменился.
assert first_url not in driver.current_url

time.sleep(3)
