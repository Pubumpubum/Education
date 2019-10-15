import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('all_links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_get_answer(browser, all_links):
    link = f"https://stepik.org/lesson/{all_links}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_class_name("textarea").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(1)
    txt = browser.find_element_by_class_name("smart-hints__hint").text
    print(txt)
    assert "Correct" in txt, "Mistake"
