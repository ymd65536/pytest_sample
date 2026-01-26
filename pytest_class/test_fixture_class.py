import pytest

class TestWithFixture:
    """
    TestWithFixture の Docstring
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        self.value = 10
        print("Setup complete")
        yield
        print("Teardown complete")
        print("Teardown actions executed")
    
    def test_value_is_ten(self):
        """
        Test that self.value is initialized to 10
        """
        assert self.value == 10
    
    def test_value_increment(self):
        """
        Test that self.value can be incremented
        """
        self.value += 5
        assert self.value == 15
