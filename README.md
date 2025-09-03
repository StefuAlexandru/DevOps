# DevOps Simple Project

This is a simple web application written in Python using Flask, containerized with Docker, and automated with CI/CD using GitHub Actions. The application is deployed for free on Render.com.

## Technologies Used
- Python 3 + Flask
- Docker
- GitHub & GitHub Actions (CI/CD)
- Render.com (free deployment)

## Running Locally
1. Clone the repository:
```bash
git clone <REPO_URL>
cd <PROJECT_NAME>

2. Build the Docker image:

docker build -t flask-app .

3. Run the container with live code:

docker run -p 5000:5000 -v ${PWD}:/app flask-app

4. Open browser at:

http://localhost:5000

**CI/CD Workflow**

The GitHub Actions workflow runs automatically on every push to the main branch.

It builds the Docker image and can push it to Docker Hub.

Render.com detects changes and redeploys the application automatically.

**Cloud Deployment**

The application is live on Render.com:

https://<APP_NAME>.onrender.com

**DevOps Flow Diagram**
Developer → GitHub → CI/CD (GitHub Actions) → Render.com → Live Application


