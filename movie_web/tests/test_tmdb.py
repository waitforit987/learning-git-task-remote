import tmdb_client
from unittest.mock import Mock
from main import app
import pytest

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = "w342"
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url
    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None

def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2

def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
    mock_single_movie = 'Movie 1'
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    single_movie = tmdb_client.get_single_movie(movie_id=823464)
    assert single_movie == mock_single_movie


def test_get_movie_images(monkeypatch):
    mock_movie_images = 'Movie_images'
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie_images
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie_images = tmdb_client.get_movie_images(movie_id=999)
    assert movie_images == mock_movie_images

def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = {
        "cast": [
            {"name": "Actor 1"},
        ]
    }
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie_single_cast = tmdb_client.get_single_movie_cast(movie_id="100")
    assert movie_single_cast == mock_single_movie_cast["cast"]


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









