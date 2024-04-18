import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ODIwZGY0YTY0YWFiYWEyZTU2NjcxMjc3YTEzYjhhMCIsInN1YiI6IjY1ZWRkY2UwNzg1NzBlMDE4N2ZkMDNlNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P-EI7CIEeGZAIqNZa5ZsTNfMxNAadrhY1y4ykPZUgrA"

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
       "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_popular_movies():
    endpoint = f"https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movie_info(title, poster_api_path):
    return {
        "title": title,
        "poster_api_path": get_poster_url(poster_api_path, "w780")
    }


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


# def get_single_movie(movie_id):
#     endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


# def get_single_movie_cast(movie_id):
#     endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()["cast"]

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]


# def get_movies_list(list_type):
#     endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     response.raise_for_status()
#     return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def search(search_query):
    endpoint = f"https://api.themoviedb.org/3/search/movie?query={search_query}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']

def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']

# def get_movie_images(movie_id):
#     endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")
