import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
wikipedia_icon = driver.find_element("class name","wikipedia-icon")
wikipedia_input_field = driver.find_element("id","Wikipedia1_wikipedia-search-input")
wikipedia_field_button = driver.find_element("css selector",".wikipedia-search-button")
button_element = driver.find_element("tag name", "button")

time.sleep(3)
driver.quit()
