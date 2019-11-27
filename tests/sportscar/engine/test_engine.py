from pytest import mark
from selenium import webdriver


@mark.smoke
@mark.engine
class EngineTests:

    def test_engine_functions_as_expected(self):
        assert True

    @mark.ui
    def test_ui_navigate_to_engine_page(self):
        browser = webdriver.Chrome("./chromedriver")
        browser.get('https://en.wikipedia.org/wiki/Engine')