from pytest import mark

@mark.smoke
@mark.body
class BodyTests:

    def test_body_functions_as_expected(self):
        assert True

    @mark.ui
    def test_ui_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get('http://www.motortrend.com')
