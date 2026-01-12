import os
import pytest
from typing import Tuple, List

@pytest.fixture
def txt() -> str:
    """
    Docstring for txt
    
    :return: Description
    :return type: str
    """
    with open("numbers.txt", "w") as f:
        for n in [1,2,3,4,5]:
            f.write(f"{n}\n")
    yield "numbers.txt"
    os.remove("numbers.txt")

def load_numbers_sorted(file_path: str) -> list[int]:
    with open(file_path, "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    return sorted(numbers)

def test_load_numbers_sorted(txt):
    assert load_numbers_sorted(txt) == [1, 2, 3, 4, 5]

# arg fixture
@pytest.fixture
def hello() -> str:
    return "hello"

@pytest.fixture
def world(hello) -> List:
    return [hello, "world"]

def test_hello_world(world):
    assert world == ["hello", "world"]
