import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://demoqa.com/selectable')


SELECT_ELEMENT_ONE_LOCATOR = ('xpath', "//li[text()='One']")
SELECT_ELEMENT_SIX_LOCATOR = ('xpath', "//li[text()='Six']")
TAB_GRID_ELEMENT =('xpath',"//a[@id='demo-tab-grid']")

#Открытие таба Grid
tab_grid = driver.find_element(*TAB_GRID_ELEMENT)
tab_grid.click()

select_element_one = driver.find_element(*SELECT_ELEMENT_ONE_LOCATOR)
select_element_six = driver.find_element(*SELECT_ELEMENT_SIX_LOCATOR)

#Проверка, что элемент не выбран
assert 'active' not in select_element_one.get_attribute('class')
assert 'active' not in select_element_six.get_attribute('class')

#Выбор элемента
select_element_one.click()
select_element_six.click()

#Проверка, что элемент не выбран
assert 'active' in select_element_one.get_attribute('class')
assert 'active' in select_element_six.get_attribute('class')

#Снятие выбора элемента
select_element_one.click()
select_element_six.click()

#Проверка, что элемент не выбран
assert 'active' not in select_element_one.get_attribute('class')
assert 'active' not in select_element_six.get_attribute('class')


time.sleep(3)
