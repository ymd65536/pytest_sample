import os
import pytest

## フィクスチャで共通のセットアップを行う
@pytest.fixture
def calculator():
    """計算を行うための共通セットアップ"""
    class Calculator:
        def __init__(self):
            self.history = []
        
        def add(self, a, b):
            result = a + b
            self.history.append(f"{a} + {b} = {result}")
            return result
    
    return Calculator()

## テストデータをフィクスチャとして定義
@pytest.fixture(scope="module")
def test_dataset():
    """テストケースのデータセットを返すフィクスチャ"""
    test_cases = {}
    for i in range(3):
        test_cases[f"generated_case_{i}"] = (
            {
                "a": i,
                "b": i * 2
            },
            {
                "result": i + (i * 2)
            }
        )
    return test_cases

## 方法1: パラメータ化されたフィクスチャを使う
@pytest.fixture(
    params=[
        ({"a": 0, "b": 0}, {"result": 0}),
        ({"a": 1, "b": 2}, {"result": 3}),
        ({"a": 2, "b": 4}, {"result": 6}),
    ],
    ids=["case_0", "case_1", "case_2"]
)
def parametrized_test_case(request):
    """パラメータ化されたテストケースフィクスチャ"""
    return request.param

def test_with_parametrized_fixture(calculator, parametrized_test_case):
    """パラメータ化されたフィクスチャとcalculatorフィクスチャを組み合わせたテスト"""
    print("")
    print(os.environ.get("PYTEST_CURRENT_TEST"))
    
    input_data, expected = parametrized_test_case
    a = input_data["a"]
    b = input_data["b"]
    
    # フィクスチャで提供されたcalculatorを使用
    result = calculator.add(a, b)
    
    # パラメータライズされた期待値で検証
    assert result == expected["result"]
    
    # フィクスチャの履歴機能も検証
    assert len(calculator.history) == 1


## 方法2: @pytest.mark.parametrizeとフィクスチャを組み合わせる
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ({"a": 0, "b": 0}, {"result": 0}),
        ({"a": 1, "b": 2}, {"result": 3}),
        ({"a": 2, "b": 4}, {"result": 6}),
    ],
    ids=["param_case_0", "param_case_1", "param_case_2"]
)
def test_parametrize_with_fixture(calculator, input_data, expected):
    """@pytest.mark.parametrizeとフィクスチャを組み合わせたテスト"""
    print("")
    print(os.environ.get("PYTEST_CURRENT_TEST"))
    
    a = input_data["a"]
    b = input_data["b"]
    
    # フィクスチャで提供されたcalculatorを使用
    result = calculator.add(a, b)
    
    # パラメータライズされた期待値で検証
    assert result == expected["result"]
    assert len(calculator.history) == 1


## 方法3: 複数のフィクスチャとパラメータライズを組み合わせる
@pytest.fixture(params=[10, 20, 30], ids=["offset_10", "offset_20", "offset_30"])
def offset(request):
    """オフセット値を提供するフィクスチャ"""
    return request.param

@pytest.mark.parametrize("multiplier", [1, 2, 3], ids=["x1", "x2", "x3"])
def test_multiple_fixtures_and_params(calculator, offset, multiplier):
    """複数のフィクスチャとパラメータを組み合わせたテスト（9つのテストケースが生成される）"""
    result = calculator.add(offset, multiplier)
    expected = offset + multiplier
    assert result == expected
