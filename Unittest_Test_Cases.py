from selenium import webdriver
import time
import unittest

class MyFirstTest(unittest.TestCase):
    def test_first_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_class > input[required]").send_keys("Eugenia")
        input2 = browser.find_element_by_css_selector(".second_class > input[required]").send_keys("Altunina")
        input3 = browser.find_element_by_css_selector(".third_class > input[required]").send_keys("test@email.com")
        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        txt = browser.find_element_by_tag_name("h1").text
        self.assertEqual((txt), 'Congratulations! You have successfully registered!', "Wrong input")
        browser.quit()

class MySecondTest(unittest.TestCase):
    def test_second_link(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_class > input[required]").send_keys("Eugenia")
        input2 = browser.find_element_by_css_selector(".second_class > input[required]").send_keys("Altunina")
        input3 = browser.find_element_by_css_selector(".third_class > input[required]").send_keys("test@email.com")
        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        txt = browser.find_element_by_tag_name("h1").text
        self.assertEqual((txt), 'Congratulations! You have successfully registered!', "Wrong input")
        browser.quit()


if __name__ == "__main__":
    unittest.main()






