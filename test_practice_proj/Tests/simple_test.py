import pytest
import unittest
from Utils.application import Application


class TestAndroidSimple():

    @pytest.fixture(scope='function')
    def app(self, request):
        app = Application()

        def fin():
            app.complete()

        request.addfinalizer(fin)

        return app

    def test_launch_app_test(self, app):

        assert 3 == 1
