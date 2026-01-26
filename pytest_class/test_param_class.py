import pytest

class TestParametrizedClass:
    """
    TestParametrizedClass の Docstring
    """
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        print("\n")
        print("=== session setup ===")
        yield
        print("=== session teardown ===")

    @pytest.mark.parametrize("input_value, expected", [
        (1, 2),
        (2, 3),
        (3, 4),
    ])
    def test_double(self, input_value, expected):
        """
        Test that input_value incremented by 1 equals expected
        """
        print(f"Testing with input_value={input_value}, expected={expected}")
        assert input_value + 1 == expected

    def teardown_class(self):
        print("=== Class teardown ===")

# 実行結果
# === session setup ===
# Testing with input_value=1, expected=2
# .Testing with input_value=2, expected=3
# .Testing with input_value=3, expected=4
# .=== Class teardown ===
# === session teardown ===

## session > class > module > function の順番
