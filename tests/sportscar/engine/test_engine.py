from pytest import mark


@mark.smoke
@mark.engine
class EngineTests:

    def test_engine_functions_as_expected(self):
        assert True

    @mark.ui
    def test_ui_navigate_to_engine_page(self, chrome_browser):
        chrome_browser.get('https://en.wikipedia.org/wiki/Engine')