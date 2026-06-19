# SafeRecLLM

Hybrid Recommendation System built using FastAPI, Collaborative Filtering, Popularity Ranking, Docker, Kubernetes, and MovieLens data.

---

## Overview

SafeRecLLM is a production-oriented recommendation platform that combines multiple recommendation strategies to generate personalized movie recommendations.

The project demonstrates:

- Collaborative Filtering
- Popularity-Based Ranking
- Hybrid Recommendation Systems
- FastAPI Backend Development
- Docker Containerization
- Kubernetes Deployment
- Google Cloud Platform Deployment
- Query Tracking and Monitoring Foundations

---

## Architecture

```text
User Request
      │
      ▼
FastAPI API
      │
      ▼
Hybrid Recommendation Engine
 ├── Collaborative Filtering
 ├── Popularity Ranking
 ├── Safety Layer
 └── Explanation Layer
      │
      ▼
Recommendation Results
      │
      ▼
Docker Container
      │
      ▼
Kubernetes Deployment
      │
      ▼
Service Exposure
```

---

## Features

### Collaborative Filtering

Identifies users with similar interests and recommends highly-rated content based on collective preferences.

### Popularity Ranking

Ranks movies using:

- Average Rating
- Rating Count
- Weighted Scoring

### Hybrid Recommendation

Combines:

- Collaborative Filtering
- Popularity-Based Ranking

to improve recommendation quality and robustness.

### Safety Layer

Filters recommendation outputs before serving results.

### Explainability

Provides explanations describing why a recommendation was selected.

### Tracking

Tracks recommendation requests and system usage for future monitoring and analytics.

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

### Data Processing

- Pandas
- NumPy

### Recommendation Systems

- Collaborative Filtering
- Popularity-Based Ranking
- Hybrid Recommendation Engine

### Infrastructure

- Docker
- Kubernetes
- Google Cloud Platform (GCP)

### Experiment Tracking

- MLflow

### Version Control

- Git
- GitHub

---

## Project Structure

```text
SafeRecLLM/
│
├── app/
│   ├── main.py
│   ├── collaborative.py
│   ├── popularity.py
│   ├── hybrid.py
│   ├── retrieval.py
│   ├── safety.py
│   ├── explain.py
│   ├── feedback.py
│   ├── tracking.py
│   └── data_loader.py
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response

```json
{
  "project": "SafeRecLLM",
  "status": "running"
}
```

---

### User Recommendations

```http
GET /recommend/user/{user_id}
```

Example

```http
GET /recommend/user/1
```

Example Response

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

## Local Development

Clone the repository:

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

Run the application:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Test:

```bash
curl http://localhost:8000/
```

---

## Docker

Build Docker image:

```bash
docker build -t saferec .
```

Run Docker container:

```bash
docker run -p 8000:8000 saferec
```

Verify:

```bash
curl http://localhost:8000/
```

---

## Kubernetes

Create Deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Create Service:

```bash
kubectl apply -f k8s/service.yaml
```

Verify deployment:

```bash
kubectl get deployments
```

Verify pods:

```bash
kubectl get pods
```

Verify services:

```bash
kubectl get svc
```

---

## Screenshots

### Kubernetes Deployment

<img width="717" height="85" alt="Screenshot 2026-06-19 141445" src="https://github.com/user-attachments/assets/82060709-a6a1-4cb2-b78d-5d9f53d2b019" />

### Running Pods

<img width="681" height="108" alt="Screenshot 2026-06-19 141504" src="https://github.com/user-attachments/assets/fdec4701-48e2-4628-bf51-d44ac0a81c9c" />

### Docker Container

<img width="1877" height="170" alt="image" src="https://github.com/user-attachments/assets/647094f3-cddd-454f-8c94-14489cbf5934" />

### API Response

<img width="1896" height="208" alt="image" src="https://github.com/user-attachments/assets/8d6fbc27-42b9-4f8c-8723-ed25d1d34cfe" />

---

## Key Learnings

- Recommendation System Design
- Collaborative Filtering
- Ranking Algorithms
- API Development with FastAPI
- Docker Containerization
- Kubernetes Deployments and Services
- Cloud Infrastructure Basics
- GitHub Workflow and Version Control

---

## Future Improvements

- Matrix Factorization (SVD)
- Neural Collaborative Filtering
- Embedding-Based Retrieval
- FAISS Semantic Search
- Reinforcement Learning Ranking
- Real-Time User Profiles
- Prometheus Monitoring
- Grafana Dashboards
- CI/CD Pipelines with GitHub Actions

---

## Resume Highlights

- Built a hybrid recommendation platform using FastAPI and MovieLens data.
- Implemented collaborative filtering and popularity-based ranking algorithms.
- Containerized services using Docker.
- Deployed recommendation services using Kubernetes Deployments and Services.
- Managed cloud infrastructure on Google Cloud Platform.
- Developed modular recommendation pipelines with safety and explainability components.

---

## Author

**Agrima Bhatnagar**

IIT Madras — BS in Data Science and Applications

Interests:

- Machine Learning
- Recommendation Systems
- Generative AI
- MLOps
- Distributed Systems
- Applied AI Engineering

GitHub: https://github.com/AgrimaBhatnagar
