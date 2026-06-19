from app.collaborative import user_recommendations
from app.popularity import top_movies


def hybrid_recommendations(user_id):

    collab = user_recommendations(user_id)

    popular = top_movies(20)

    collab["source"] = "collaborative"

    popular["source"] = "popularity"

    combined = collab[
        ["title", "avg_rating", "rating_count", "source"]
    ]

    popular = popular[
        ["title", "avg_rating", "rating_count", "source"]
    ]

    final = combined.copy()

    for _, row in popular.iterrows():

        if row["title"] not in final["title"].values:

            final.loc[len(final)] = row

    return final.head(15)
