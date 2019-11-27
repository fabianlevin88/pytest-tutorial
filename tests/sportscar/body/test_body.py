from pytest import mark
from selenium import webdriver

@mark.smoke
@mark.body
class BodyTests:

    def test_body_functions_as_expected(self):
        assert True

    @mark.ui
    def test_ui_navigate_to_body_page(self):
        browser = webdriver.Chrome("C:\\Users\\Fabian\\PycharmProjects\\pytest-tutorial\\chromedriver")
        browser.get('http://www.motortrend.com')
