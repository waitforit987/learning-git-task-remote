from unittest.mock import Mock
from main import app
import pytest


@pytest.mark.parametrize('list_type', (
    ('popular', 'now_playing', "top_rated", "upcoming", 'favorites')
))
def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    print("TEST")


    with app.test_client() as client:
      response = client.get('/')
      print(response)
      assert response.status_code == 200
      assert (f'movies/{list_type}') 