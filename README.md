# SafeRecLLM

Hybrid Recommendation System built using FastAPI, Collaborative Filtering, Semantic Retrieval, and MovieLens data.

## Overview

SafeRecLLM is a production-oriented recommendation system that combines multiple recommendation strategies to generate high-quality personalized recommendations.

The project demonstrates:

- Collaborative Filtering
- Popularity-Based Ranking
- Semantic Retrieval
- Hybrid Recommendation Pipelines
- FastAPI Deployment
- Docker Containerization
- GCP Deployment

---

## Architecture

User Request
      │
      ▼
FastAPI API
      │
      ▼
Hybrid Recommender
 ├── Collaborative Filtering
 ├── Popularity Ranking
 └── Semantic Retrieval
      │
      ▼
Filtered Recommendations
      │
      ▼
Explanations + Results

---

## Features

### Collaborative Filtering

Finds users with similar preferences and recommends highly-rated content from those users.

### Popularity Ranking

Ranks content using:

- Average Rating
- Rating Count
- Weighted Score

### Semantic Retrieval

Uses embedding-based retrieval to find content relevant to user interests.

### Hybrid Recommendation

Combines:

- Collaborative Filtering
- Popularity Ranking
- Semantic Search

to improve recommendation quality.

### Safety Layer

Applies filtering and validation before returning recommendations.

---

## Dataset

MovieLens Small Dataset

Statistics:

- 9,742 Movies
- 100,836 Ratings
- 610 Users

Source:

https://grouplens.org/datasets/movielens/

---

## Technology Stack

### Backend

- Python
- FastAPI

### Machine Learning

- Pandas
- NumPy
- Scikit-Learn
- Sentence Transformers
- FAISS

### Deployment

- Docker
- Google Cloud Platform

### Experiment Tracking

- MLflow

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "project": "SafeRecLLM",
  "status": "running"
}
```

### User Recommendations

```http
GET /recommend/user/{user_id}
```

Example:

```http
GET /recommend/user/1
```

---

## Example Output

```json
[
  {
    "title": "The Shawshank Redemption",
    "avg_rating": 4.42,
    "rating_count": 317,
    "source": "collaborative"
  }
]
```

---

## Local Setup

Clone repository:

```bash
git clone https://github.com/AgrimaBhatnagar/SafeRecLLM.git

cd SafeRecLLM
```

Create virtual environment:

```bash
python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run API:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## Docker

Build image:

```bash
docker build -t saferec .
```

Run container:

```bash
docker run -p 8000:8000 saferec
```

---

## Future Improvements

- Matrix Factorization (SVD)
- Real-Time User Embeddings
- Reinforcement Learning Ranking
- LLM-Based Explanations
- A/B Testing Framework
- Multi-Agent Recommendation Pipeline

---

## Project Status

Current Version: v1.0

Implemented:

- FastAPI Service
- Collaborative Filtering
- Popularity Ranking
- Hybrid Recommendation Engine
- Docker Support
- GCP Deployment

---

## Author

Agrima Bhatnagar

IIT Madras BS in Data Science and Applications

Interests:

- Machine Learning
- Recommendation Systems
- Generative AI
- Distributed Systems
- Applied AI Engineering
