from pytest import mark
from selenium import webdriver


@mark.entertainment
class EntertainmentTests:

    def test_entertainment_functions_as_expected(self):
        assert True

    @mark.ui
    def test_ui_navigate_to_entertainment_page(self):
        browser = webdriver.Chrome("./chromedriver")
        browser.get('https://www.siriusxm.com')