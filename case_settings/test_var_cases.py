import os
import pytest

case_settings = {
    "sample_case_1":(
        {
            "a": 1,
            "b": 2
        },
        {
            "result": 3
        }
    ),
    "sample_case_2":(
        {
            "a": -1,
            "b": 1
        },
        {
            "result": 0
        }
    )
}

## 変数に合わせてパラメータ化する方法

@pytest.mark.parametrize(
    "input_data, expected",
    list(case_settings.values()),
    ids=list(case_settings.keys())
)
def test_sample_case(input_data, expected):
    print("")
    print(os.environ.get("PYTEST_CURRENT_TEST"))
    a = input_data["a"]
    b = input_data["b"]
    result = a + b
    assert result == expected["result"]
