import pandas as pd

from app.data_loader import load_data


def top_movies(n=10):

    movies, ratings = load_data()

    movie_stats = (
        ratings.groupby("movieId")
        .agg(
            rating_count=("rating", "count"),
            avg_rating=("rating", "mean")
        )
        .reset_index()
    )

    ranked = (
        movie_stats[
            movie_stats["rating_count"] >= 50
        ]
        .sort_values(
            by=["avg_rating", "rating_count"],
            ascending=False
        )
    )

    result = ranked.merge(
        movies,
        on="movieId"
    )

    return result[
        [
            "title",
            "avg_rating",
            "rating_count"
        ]
    ].head(n)
