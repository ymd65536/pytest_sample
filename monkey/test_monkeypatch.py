from pathlib import Path


class SampleClass:
    def method(self):
        return "original"

def get_sample_instance():
    return SampleClass().method()

def test_sample_method(monkeypatch):
    def mock_method(self):
        return "mocked"

    monkeypatch.setattr(SampleClass, "method", mock_method)
    result = get_sample_instance()
    print(result)
    assert result == "mocked"

def getssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"

def test_getssh(monkeypatch):
    def mockreturn():
        return Path("/yamada")

    monkeypatch.setattr(Path, "home", mockreturn)
    x = getssh()
    print(x)
    assert x == Path("/yamada/.ssh")

# monkeypatch を使ってクラスメソッドや関数の動作を一時的に変更するテストコードの例です。
# attribute の置き換えや関数の戻り値の変更を行い、期待される動作を検証しています。
