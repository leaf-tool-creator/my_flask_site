import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page is live!"

@app.route("/tool/<tool_name>")
def tool(tool_name):
    return f"This is {tool_name}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)