from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_class > input[required]")
    input1.send_keys("Eugenia")
    input2 = browser.find_element_by_css_selector(".second_class > input[required]")
    input2.send_keys("Altunina")
    input3 = browser.find_element_by_css_selector(".third_class > input[required]")
    input3.send_keys("test@email.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
