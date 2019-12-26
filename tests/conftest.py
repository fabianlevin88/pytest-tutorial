from pytest import fixture
from selenium import webdriver
from config import Config

# function -> one webdriver instace per test case (function)
# Session -> one webdriver for every test
@fixture(scope='session')
def chrome_browser():
    return webdriver.Chrome("./chromedriver")


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    return Config(env)


def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="Environment to run tests against")