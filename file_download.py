import math
from selenium import webdriver
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'bio.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname").send_keys("Eugenia")
    input2 = browser.find_element_by_name("lastname").send_keys("Altunina")
    input3 = browser.find_element_by_name("email").send_keys("test@email.com")
    attach = browser.find_element_by_name("file").send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

