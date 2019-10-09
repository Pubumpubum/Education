import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    browser.execute_script("window.scrollBy(0, 200);")
    robot = browser.find_element_by_id("robotCheckbox")
    robot.click()
    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()