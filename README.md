## Distributed Multi-Agent Retrieval & Reasoning Platform

A modular LLM engineering platform designed for building scalable AI systems with modern machine learning and cloud-native architectures.

The project focuses on creating production-oriented LLM infrastructure including model serving, retrieval pipelines, agent orchestration, observability, and distributed deployment.

```bash
docker compose -f docker/docker-compose.yml up --build

# Run Redis
docker run -d -p 6379:6379 redis

# Run Postgres
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=password postgres

# Deploy Kubernetes:
kubectl apply -f k8s/

# Get public endpoint:
kubectl get services
```

