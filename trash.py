import pytest
from selenium import webdriver
import time
import math

answer = str(math.log(int(time.time())))
link = "https://stepik.org/lesson/236899/step/1"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element_by_class_name("textarea").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()

finally:
    time.sleep(50)
    browser.quit()