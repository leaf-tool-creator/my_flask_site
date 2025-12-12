import os
from flask import Flask, render_template
import tools.tool1 as tool1  # import your tool module

app = Flask(__name__)

# Map tool names to their modules
tools_dict = {
    "tool1": tool1,
    # Add more tools here later
}

# Home page route
@app.route("/")
def home():
    return render_template("index.html", tools=tools_dict.keys())

# About page route
@app.route("/about")
def about():
    return render_template("about.html")

# Dynamic route for tools
@app.route("/tool/<tool_name>")
def tool(tool_name):
    if tool_name in tools_dict:
        module = tools_dict[tool_name]
        result = module.run()  # Call the tool's run() function
        return render_template("tool.html", tool_name=tool_name, result=result)
    else:
        return "Tool not found", 404

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
