from selenium import webdriver
import time 

link = "https://yandex.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".input__box .input__input")
    input1.send_keys("Симфония сервис")
    button = browser.find_element_by_css_selector(".search2__button > button")
    button.click()

finally:
    time.sleep(15)
    browser.quit()