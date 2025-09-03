from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "DevOps Project: CI/CD, Docker, Render Deployment"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


