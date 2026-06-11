from fastapi import FastAPI

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

