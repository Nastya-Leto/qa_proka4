from selenium import webdriver
import time
import os

upload_button_locator = ('xpath', "//input[@id='uploadFile']")

driver = webdriver.Chrome()
driver.get('https://demoqa.com/upload-download')

upload_button = driver.find_element(*upload_button_locator)
path_image = os.path.join(os.getcwd(), 'upload_file', 'image.jpg')

upload_button.send_keys(path_image)
time.sleep(5)
