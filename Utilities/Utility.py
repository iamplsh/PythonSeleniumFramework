from selenium import webdriver
class Utility:
    driver = webdriver.Chrome()

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, pageObject):
        self.driver.find_element_by_xpath(pageObject)

