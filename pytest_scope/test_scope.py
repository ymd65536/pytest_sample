import pytest

class TestExample:
    """
    TestExample の Docstring
    """
    @pytest.fixture(scope="function", autouse=True)
    def function_scope(self):
        print("\n")
        print("=== function setup ===")
        yield
        print("=== function teardown ===")
    
    @pytest.fixture(scope="module", autouse=True)
    def module_scope(self):
        print("=== module setup ===")
        yield
        print("=== module teardown ===")

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

    @pytest.fixture(scope="module", autouse=True)
    def teardown_class(self):
        print("=== module setup ===")
        yield
        print("=== module teardown ===")

# 注意事項: teardown_class で終了時に実行されるコードを定義していますが
# 実行時にはteardown_classがモジュールスコープのフィクスチャとして扱われるため
# テストの開始時にも実行されます。

# このコードでは"module_scope"という表示が2回出力されることに注意してください。
