import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "My Flask website is live!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port
    app.run(host="0.0.0.0", port=port)       # Must use 0.0.0.0
