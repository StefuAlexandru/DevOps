from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def clock():
    now = datetime.now().strftime("%H:%M:%S")
    html = """
    <html>
      <head>
        <title>DevOps Clock</title>
        <meta http-equiv="refresh" content="1">
        <style>
          body { font-family: Arial; text-align: center; margin-top: 100px; }
          h1 { font-size: 50px; }
        </style>
      </head>
      <body>
        <h1>{{ time }}</h1>
        <p>Flask app running with Docker and CI/CD workflow</p>
      </body>
    </html>
    """
    return render_template_string(html, time=now)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
