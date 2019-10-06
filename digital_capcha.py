import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    robot = browser.find_element_by_id("robotCheckbox")
    robot.click()
    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

