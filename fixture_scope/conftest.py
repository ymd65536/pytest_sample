# conftest.py
import pytest

@pytest.fixture(scope="session")
def global_config():
    data = {"function_setup_count": 0 , "module_setup_count": 0}
    return data

# pytest では、conftest.py に定義された fixture は自動的にテストモジュールから利用可能になります。
