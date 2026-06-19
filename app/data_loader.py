import pandas as pd

MOVIES_PATH = "datasets/ml-latest-small/movies.csv"
RATINGS_PATH = "datasets/ml-latest-small/ratings.csv"

def load_data():

    movies = pd.read_csv(
        MOVIES_PATH
    )

    ratings = pd.read_csv(
        RATINGS_PATH
    )

    return movies, ratings
