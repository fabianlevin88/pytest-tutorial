from pytest import mark


@mark.entertainment
class EntertainmentTests:

    def test_entertainment_functions_as_expected(self):
        assert True

    @mark.ui
    def test_ui_navigate_to_entertainment_page(self, chrome_browser):
        chrome_browser.get('https://www.siriusxm.com')