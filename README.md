# Assignment: DevOps Pipeline for a Book Inventory App

## Objective
Your assignment is to build out the DevOps CI/CD pipeline and containerization strategy for this Python Book Inventory application.
---

## Assignment Details

### 1. Docker Requirements
You must write a `Dockerfile` with the following requirements:
- Use a **multi-stage build** to optimize the image size.
- Incorporate basic **Docker security features**:
  - Use a minimal base image 
  - Create and run the container as a **non-root user**
  - Install dependencies in the build stage only, copy artifacts to the runtime stage
- **Do not run tests inside the Dockerfile.** Tests are handled exclusively by the Jenkins pipeline.

### 2. Jenkins Pipeline Requirements
You must write a `Jenkinsfile` for the CI/CD pipeline. The pipeline must include:

- Usage of the `environment` block to define variables (image name, tag, port, container name, registry URL).
- The following stages:
  - **SCM Pull** — Checkout the source code from your **private GitHub repository** using stored credentials.
  - **Test** — Install dependencies and run the application tests.
  - **Build Docker Image** — Build the multi-stage Docker image.
  - **Push to Registry** — Tag and push the image to your **private Docker registry** using stored credentials.
  - **Deploy** — Pull the image from the private registry and run the container.
  - **Smoke Test** — Verify the deployment by sending curl requests to all 3 application endpoints.
  - **Cleanup** — Stop and remove the container, prune dangling images, and clean the workspace.

### 3. Jenkins Plugin Requirements
The following Jenkins plugins must be installed before running the pipeline:
- Git Plugin
- Credentials Plugin
- Credentials Binding Plugin
- Docker Pipeline Plugin
- Pipeline Plugin
- Workspace Cleanup Plugin
- ShiningPanda Plugin
- JUnit Plugin

### 4. Jenkins Credentials Setup
Before running the pipeline, add the following credentials in **Jenkins → Manage Jenkins → Credentials**:
- `github-credentials`
- `docker-registry-credentials`

### 5. Deployment Expected Output
Your smoke test stage should verify all 3 application endpoints and show their output:

- `http://localhost:5000/` — HTML dashboard listing all books with availability status
- `http://localhost:5000/health` — JSON response with service status, uptime, and book counts
- `http://localhost:5000/api/books` — JSON list of all books with full details

Expected `/health` response:
```json
{
  "status": "healthy",
  "uptime_seconds": 3,
  "total_books": 5,
  "available_books": 3,
  "timestamp": "2024-01-01T00:00:00+00:00"
}
```

Expected `/api/books` response:
```json
{
  "count": 5,
  "books": [
    { "id": 1, "title": "The Pragmatic Programmer", "author": "David Thomas", "genre": "Technology", "year": 1999, "available": true },
    ...
  ]
}
```

---

## Repository Structure
```
pip-ass/
├── app.py              # Flask application with 3 endpoints
├── requirements.txt    # Python dependencies
├── test_app.py         # Application tests
├── Dockerfile          # Multi-stage Docker build
└── Jenkinsfile         # CI/CD pipeline definition
```

---

## Submission
Please submit:
1. The URL to your **private GitHub repository** containing `app.py`, `requirements.txt`, `Dockerfile`, `test_app.py`, and `Jenkinsfile`.
2. Screenshots of the **Jenkins credentials** configured (GitHub and Docker registry).
3. Screenshots of a **successful Jenkins pipeline run** showing all stages green.
4. Screenshots of the **3 endpoint outputs** from the smoke test stage console log.
