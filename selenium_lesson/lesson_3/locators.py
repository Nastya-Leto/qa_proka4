import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://hyperskill.org/tracks')

time.sleep(3)

title = driver.find_element('xpath','//title')
sign_in_button = driver.find_element('xpath', '//header//button[@data-component-name="Primitive"]')
sign_in_button2 = driver.find_element('xpath',"(//button[@data-component-name='Primitive'])[1]")
start_for_free_button = driver.find_element('xpath','//span[normalize-space()="Start for free"]')
categories = driver.find_element('xpath','//div[contains(@class,"categories")]')
python_developer_card = driver.find_element('xpath',"//h5[text()='Python Developer']")
load_more_button = driver.find_element('xpath','(//span[@class="w-full"])[3]')
load_more_button2 = driver.find_element("xpath", "//button/span[contains(normalize-space(), 'Load more')]")
google_play_button = driver.find_element('xpath','//a[@click-event-target="google-play"]/img[@alt="Get it on Google Play"]')
go_developer_button = driver.find_element('xpath','//div[contains(@class,"flex-wrap")]//h5[contains(text(),"Go")]')
pricing_button = driver.find_element('xpath',"//header[@id='header']//a[normalize-space()='Pricing']")
pricing_button2 = driver.find_element('xpath',"//a[@class='nav-link' and normalize-space()='Pricing']")
for_business = driver.find_element('xpath',"//a[@rel='noopener']")
for_business1 = driver.find_element('xpath',"//li[@click-event-target='join_as_organization']")
instagram_button = driver.find_element('xpath',"//a[@click-event-part='footer' and @click-event-target='Instagram']")
reddit_button = driver.find_element('xpath',"//a[@click-event-target='Reddit']")
reddit_button2 = driver.find_element('xpath',"//a[contains(@class,'opacity') and @aria-label='Hyperskill on Reddit']")
reddit_button3 = driver.find_element('xpath',"(//a[contains(@class,'opacity')])[1]")
about_button = driver.find_element('xpath',"//a[@click-event-part='footer' and text()='About']")
python_developer_button = driver.find_element('xpath',"//div[@class='card-body']//h5[text()='Python Developer']")
header = driver.find_element('xpath',"//h1[@id='courses']")
header2 = driver.find_element('xpath',"//h1[normalize-space()='What do you want to learn today?']")
header3 = driver.find_element('xpath',"//section/h1")
most_popular_button = driver.find_element('xpath', '//a[@click-event-context=\'{"title":"most_popular"}\']')
most_popular_button2 = driver.find_element('xpath',"//a[@href='/courses?category=27']")
python_button = driver.find_element('xpath',"//footer[@data-component-name='TheFooter']//a[@click-event-target='Python']")
python_button2 = driver.find_element('xpath','//a[@target="_self" and text()="Python"]')
full_catalog_button = driver.find_element('xpath','//section/a[@click-event-target="full_catalog"]')
icon = driver.find_element('xpath',"(//*[local-name()='svg' and @fill='none' and @data-component-name='alt-logo-icon-hyperskill'])[1]")
block_footer = driver.find_element('xpath',"(//div[descendant::span[text()='Languages']])[6]")
block_footer2 = driver.find_element('xpath',"//span[text()='Languages']/ancestor::div[1]")





