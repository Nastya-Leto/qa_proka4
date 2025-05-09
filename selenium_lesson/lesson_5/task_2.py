from os import getcwd
from selenium import webdriver
import time
import os

download_button_locator = ('xpath', "//a[contains(@href,'download')]")

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

preferences = {
    "download.default_directory": os.path.join(os.getcwd(), "downloads"),
    "safebrowsing.enabled": True,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(options=options)
driver.get('https://the-internet.herokuapp.com/download')

download_links = driver.find_elements(*download_button_locator)

for link in download_links:
    link.click()
    file_name = link.text
    time.sleep(3)

    if os.path.exists(os.path.join(getcwd(), 'downloads', file_name)):
        print(f'Файл успешно скачан: {file_name}')
    else:
        print(f'Файл не скачан: {file_name}')
