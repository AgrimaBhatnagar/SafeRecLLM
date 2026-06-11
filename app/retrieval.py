import pandas as pd
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

movies = pd.read_csv(
    "app/data/movies.csv"
)

embeddings = model.encode(
    movies["description"].tolist()
)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    np.array(embeddings).astype("float32")
)

def retrieve(query, k=5):

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    return movies.iloc[
        indices[0]
    ][["title","description"]]
