import pandas as pd

from app.data_loader import load_data


def user_recommendations(user_id):

    movies, ratings = load_data()

    user_movies = ratings[
        ratings["userId"] == user_id
    ]["movieId"]

    similar_users = ratings[
        ratings["movieId"].isin(user_movies)
    ]["userId"].unique()

    recommendations = ratings[
        ratings["userId"].isin(similar_users)
    ]

    scores = (
        recommendations
        .groupby("movieId")
        .agg(
            avg_rating=("rating", "mean"),
            rating_count=("rating", "count")
        )
        .reset_index()
    )

    scores["weighted_score"] = (
        scores["avg_rating"] *
        scores["rating_count"]
    )

    scores = scores[
        scores["rating_count"] >= 20
    ]

    scores = scores.sort_values(
        by="weighted_score",
        ascending=False
    )

    return scores.merge(
        movies,
        on="movieId"
    ).head(10)
