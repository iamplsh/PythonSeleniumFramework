import pytest
from selenium import webdriver
from pageObjects.homePageObjects import homePageObjects
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGeneration

class Test_001_Login:


    hp = homePageObjects()
    baseURL = ReadConfig.getURL()
    logger = LogGeneration.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("*********Launching Browser*********")
        self.driver = setup
        self.logger.info("*********Launching {0}*********".format(self.baseURL))
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@class='button-1 login-button']").click()

        title = self.driver.find_element_by_xpath("//*[text()='Dashboard']").text

        self.driver.quit()

    def test_login_dashboard(self, setup):

        self.logger.info("*********Launching Browser*********")
        self.driver = setup
        self.logger.info("*********Launching {0}*********".format(self.baseURL))
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@class='button-1 login-button']").click()

        title = self.driver.find_element_by_xpath("//*[text()='Dashboard']").text

        self.driver.quit()






