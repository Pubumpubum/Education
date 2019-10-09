import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    answer = str(int(x) + int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(answer)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

