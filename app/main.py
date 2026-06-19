from fastapi import FastAPI
from app.hybrid import hybrid_recommendations
from app.retrieval import retrieve

app = FastAPI()

@app.get("/")
def health():
    return {
        "project":"SafeRecLLM",
        "status":"running"
    }

@app.get("/recommend")
def recommend(
    query: str
):

    recommendations = retrieve(query)

    return recommendations.to_dict(
        orient="records"
    )

@app.get("/recommend/user/{user_id}")
def recommend_user(user_id: int):

    return hybrid_recommendations(
        user_id
    ).to_dict(
        orient="records"
    )
