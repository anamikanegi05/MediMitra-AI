from flask import Flask, render_template, request
from modules.mcp_server import MCPServer

app = Flask(__name__)
mcp = MCPServer()

@app.route("/", methods=["GET", "POST"])
def home():
    response = None

    if request.method == "POST":
        user_input = request.form.get("symptoms")
        response = mcp.process(user_input)

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
