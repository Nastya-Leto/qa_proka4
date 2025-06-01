from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
action  = ActionChains(driver)
driver.get('https://seiyria.com/bootstrap-slider/')

slider_block_locator = ('xpath', "//div[@id='example-2']/div")
slider_first_locator = ('xpath',"(//div[@id='example-2']/div//div[@role='slider'])[1]")
slider_second_locator = ('xpath',"(//div[@id='example-2']/div//div[@role='slider'])[2]")


slider_element = driver.find_element(*slider_block_locator)
action.scroll_to_element(slider_element).perform()
time.sleep(5)

# def move_slider(current_position_attribute: str, endpoint: int, step: int | float, slider: WebElement):
#     current_position = int(slider.get_attribute(current_position_attribute))
#     if endpoint < current_position:
#         offset = int((current_position - endpoint) / step)
#         slider.send_keys(Keys.ARROW_LEFT * offset)
#     elif endpoint > current_position:
#         offset = int((endpoint - current_position) / step)
#         slider.send_keys(Keys.ARROW_RIGHT * offset)
#
# def set_range(
#         first_slider: WebElement,
#         second_slider: WebElement,
#         target_positions: list, # [100, 200]
#         current_position_attribute: str,
#         step: int | float
# ):
#     move_slider(current_position_attribute, target_positions[0], step, first_slider)
#     move_slider(current_position_attribute, target_positions[1], step, second_slider)
#
# time.sleep(3)
# set_range(
#     slider_1,
#     slider_2,
#     [200, 700],
#     "aria-valuenow",
#     1
# )
# time.sleep(3)
#
