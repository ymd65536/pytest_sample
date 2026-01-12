import pytest


def add(a, b):
    return a + b

# OK: tuple ("a, b, expected")
# NG: str ("a, b, expected")

# OK: list [(1,2,3)]
# NG:  do not list (1,2,3)
@pytest.mark.parametrize(("a, b, expected"), [
    (1, 2, 3),
    (4, 5, 9),
    (10, 15, 25),
])
def test_parametrize1(a, b, expected):
    """
    Docstring for test_parametrize1
    
    :param a: Description
    :type a: Literal[1, 4, 10]
    :param b: Description
    :type b: Literal[2, 5, 15]
    :param expected: Description
    :type expected: Literal[3, 9, 25]
    """
    assert add(a, b) == expected, f"{a} + {b} = {expected}"
