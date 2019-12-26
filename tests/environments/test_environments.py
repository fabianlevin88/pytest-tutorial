from pytest import mark

class EnvironmentsTests:

    @mark.env
    def test_environment_is_qa(self, app_config):
        base_url = app_config.base_url
        port = app_config.app_port
        assert base_url == 'https://myqa-env.com'
        assert port == 80

    @mark.env
    def test_environment_is_dev(self, app_config):
        base_url = app_config.base_url
        port = app_config.app_port
        assert base_url == 'https://mydev-env.com'
        assert port == 8080

    @mark.env
    def test_environment_is_staging(self, app_config):
        base_url = app_config.base_url
        port = app_config.app_port
        assert base_url == 'staging'