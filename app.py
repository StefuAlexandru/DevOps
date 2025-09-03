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
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #89f7fe, #66a6ff);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          }
          .clock-container {
            text-align: center;
            background: rgba(255, 255, 255, 0.2);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(0, 0, 0, 0.2);
          }
          h1 {
            font-size: 80px;
            margin: 0;
            color: #fff;
          }
          p {
            font-size: 20px;
            color: #fff;
          }
        </style>
      </head>
      <body>
        <div class="clock-container">
          <h1>{{ time }}</h1>
          <p>Flask app running with Docker and CI/CD workflow</p>
        </div>
      </body>
    </html>
    """
    return render_template_string(html, time=now)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
