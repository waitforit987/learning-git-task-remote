
from random import Random
from datetime import datetime


class Movie:
    def __init__(self, title, year_of_production, genre, number_of_plays):
        self.title = title
        self.year_of_production = year_of_production
        self.genre = genre
        self.number_of_plays = number_of_plays

    def __str__(self):
        return f"{self.title} ({self.year_of_production})"

    def play(self):
        return self.number_of_plays + 1


class Series(Movie):
    def __init__(self, title, year_of_production, genre, number_of_plays, number_of_season, number_of_episode):
        super().__init__(title, year_of_production, genre, number_of_plays)
        self.number_of_season = number_of_season
        self.number_of_episode = number_of_episode

    def __str__(self):
        return f"{self.title} {self.number_of_season}{self.number_of_episode}"


list_of_movies_and_series = []


#
def adding_all_season_of_series(title, year_of_production, genre, number_of_plays, number_of_season,
                                number_of_episode_to_add):
    for episode in range(1, number_of_episode_to_add + 1):
        series = Series(title, year_of_production, genre, number_of_plays, f"S{number_of_season:02d}",
                        f"E{episode:02d}")
        list_of_movies_and_series.append(series)
    return list_of_movies_and_series


def adding_movies(title, year_of_production, genre, number_of_plays):
    movie = Movie(title, year_of_production, genre, number_of_plays)
    list_of_movies_and_series.append(movie)

def get_movies(list_of_films):
    list_of_movies = []
    for element in list_of_films:
        if isinstance(element, Movie) and not isinstance(element, Series):
            list_of_movies.append(element)
    sorted_movies = sorted(list_of_movies, key=lambda movie: movie.title)
    return sorted_movies


def get_series(list_of_serials):
    list_of_series = []
    for element in list_of_serials:
        if isinstance(element, Series):
            list_of_series.append(element)
    sorted_series = sorted(list_of_series, key=lambda serial: serial.title)
    return sorted_series


def search():
    choice = input("Enter movie or series ").lower()
    for element in list_of_movies_and_series:
        if element.title.lower() == choice:
            print(f"You find {element.title}")
            break
    else:
        print("Movie or series doesn't exist")


random_list = []
random = Random()


def generate_views():
    random_element = random.choice(list_of_movies_and_series)
    list_of_movies_and_series.remove(random_element)
    random_list.append(random_element)
    random_element.number_of_plays = random.randint(1, 100)
    return random_list


def run_generate_views():
    for i in range(10):
        generate_views()
    return generate_views()


def top_titles():
    current_date = datetime.now().strftime("%d.%m.%Y")
    content_type = input("Choose type ").lower()
    if content_type == "movies":
        list_of_movies = get_movies(run_generate_views())
        sorted_by_number_of_plays = sorted(list_of_movies, key=lambda result: result.number_of_plays)
        list_of_top_title_movies = sorted_by_number_of_plays[0:3]
        list_of_top_title_movies.reverse()
        print(f"Most popular movies of the day {current_date}")
        for element in list_of_top_title_movies:
            print(element)
    if content_type == "series":
        list_of_series = get_series(run_generate_views())
        sorted_by_number_of_plays = sorted(list_of_series, key=lambda result: result.number_of_plays)
        list_of_top_title_series = sorted_by_number_of_plays[0:3]
        list_of_top_title_series.reverse()
        print(f"Most popular series of the day {current_date}")
        for element in list_of_top_title_series:
            print(element)
    if content_type == "all":
        movie_and_series_list = run_generate_views()
        sorted_by_number_of_plays = sorted(movie_and_series_list, key=lambda result: result.number_of_plays)
        all_list_of_top_title = sorted_by_number_of_plays[0:3]
        all_list_of_top_title.reverse()
        print(f"Most popular movies and series of the day {current_date}")
        for element in all_list_of_top_title:
            print(element)

def get_total_episodes(series):
    print(f"Total episodes for {series.title}: {series.number_of_episode}")

def displaying_get_total_episodes(list_of_episodes):
    for series in list_of_episodes:
        if isinstance(series, Series):
            get_total_episodes(series)
        else:
            print(f"Skipping {series} as it's not an instance of Series")

def main_program():
    print("Movies database")
    adding_movies("Forrest Gump", "1994", "Drama", 0)
    adding_movies("Good Will Hunting", "1997", "Drama", 0)
    adding_movies("Departed", "2006", "Action", 0)
    adding_movies("Gladiator", "2000", "Drama", 0)
    adding_movies("Beautiful Mind", "2001", "Drama", 0)
    adding_movies("Dangerous Minds", "1995", "Drama", 0)
    adding_movies("Inception", "2010", "Science-fiction", 0)
    adding_movies("Interstellar", "2014", "Science-fiction", 0)
    adding_movies("Donnie Darko", "2001", "Psycho", 0)
    adding_movies("Notebook", "2004", "Romance", 0)
    adding_movies("Iron Man", "2008", "Science-fiction", 0)
    adding_movies("Avengers", "2012", "Science-fiction", 0)
    adding_movies("Thor", "2011", "Science-fiction", 0)
    adding_movies("Spider-Man", "2002", "Science-fiction", 0)
    adding_movies("Batman", "2005", "Science-fiction", 0)
    adding_all_season_of_series("How i met your mother", "2005", "Comedy", 0, 5, 15)
    top_titles()


if __name__ == "__main__":
    main_program()
