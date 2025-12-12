from flask import Flask, render_template
import tools.calculator as calculator
import tools.data_viewer as data_viewer

app = Flask(__name__)

# Map tool names to their modules
tools_dict = {
    "calculator": calculator,
    "data_viewer": data_viewer
}

@app.route("/")
def home():
    return render_template("index.html", tools=tools_dict.keys())

@app.route("/tool/<tool_name>")
def tool(tool_name):
    if tool_name in tools_dict:
        module = tools_dict[tool_name]
        result = module.run()
        return render_template("tool.html", tool_name=tool_name, result=result)
    else:
        return "Tool not found", 404

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
