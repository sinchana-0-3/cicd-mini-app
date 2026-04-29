
from flask import Flask

app = Flask(__name__)   # ✅ THIS LINE IS VERY IMPORTANT

@app.route("/")
def home():
    return "Hello CI/CD Pipeline!"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)