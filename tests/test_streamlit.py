import pytest
from streamlit.testing import TestCase

class TestStreamlitApp(TestCase):

    def test_app(self):
        self.run_streamlit('app.py')
        assert self.find('Weather and Crypto Dashboard')