from selenium import webdriver
import pytest
import os

@pytest.fixture()
def setup():
    browser = 'chrome'
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('Launching Chrome')
    else:
        driver = webdriver.Firefox()
        print('Launching Firefox')
    return driver

# this will get the value from cli
# def pytest_adoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
