import pytest

# conftest.pyからインポートしたグローバル設定を使用

# 関数スコープ：テストごとに毎回実行される
@pytest.fixture(scope="function")
def function_fixture(global_config):
    global_config["function_setup_count"] += 1
    yield global_config["function_setup_count"]

# モジュールスコープ：モジュール全体で1回だけ実行される
@pytest.fixture(scope="module")
def module_fixture(global_config):
    global_config["module_setup_count"] += 1
    yield global_config["module_setup_count"]

def test_one(function_fixture, module_fixture):
    print(f"\nFunction fixture setup count: {function_fixture}")
    assert 1 == function_fixture  # 1回目
    print(f"Module fixture setup count: {module_fixture}")
    assert 1 == module_fixture    # 1回目

def test_two(function_fixture, module_fixture):
    print(f"\nFunction fixture setup count: {function_fixture}")
    assert 2 == function_fixture  # 2回目！
    print(f"Module fixture setup count: {module_fixture}")
    assert 1 == module_fixture    # まだ1回目！

def test_three(function_fixture, module_fixture):
    print(f"\nFunction fixture setup count: {function_fixture}")
    assert 3 == function_fixture  # 3回目！
    print(f"Module fixture setup count: {module_fixture}")
    assert 1 == module_fixture    # まだ1回目！
