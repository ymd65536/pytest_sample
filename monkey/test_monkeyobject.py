import requests


class App:
    @staticmethod
    def get_json(url):
        """Takes a URL, and returns the JSON."""
        r = requests.get(url)
        return r.json()    

class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

def test_get_json(monkeypatch):
    def mock_get(*args):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = App.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"

# オブジェクトに対するモンキーパッチの例
# requests ライブラリの get メソッドをモンキーパッチして、常に特定のレスポンスを返すようにしています。
