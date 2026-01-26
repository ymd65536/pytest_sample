import pytest

def add(a, b):
    return a + b


case_data = [
    {"a": 1, "b": 2, "expected": 3},
    {"a": 4, "b": 5, "expected": 9},
    {"a": 10, "b": 15, "expected": 25}
]


@pytest.mark.parametrize(
    "test_case", case_data
)
def test_add_json_parametrize(test_case):
    """
    Docstring for tes_add_json_parametrize

    :param case: Test case data
    :type case: Dict[str, int]
    """
    a = test_case["a"]
    b = test_case["b"]
    expected = test_case["expected"]
    print(f"Testing add({a}, {b}) == {expected}")
    assert add(a, b) == expected, f"{a} + {b} = {expected}"

# parametrize を使うと同じテスト関数が複数回実行される
# テストケースの数を増やしてテストを拡充したい場合に便利
# 便利な反面、引数の数が多くなると可読性が下がる
