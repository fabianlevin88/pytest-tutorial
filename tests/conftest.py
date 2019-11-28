from pytest import fixture
from selenium import webdriver

# function -> one webdriver instace per test case (function)
# Session -> one webdriver for every test
@fixture(scope='session')
def chrome_browser():
    return webdriver.Chrome("./chromedriver")
