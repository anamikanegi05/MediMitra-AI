from flask import Flask, render_template, request
from modules.mcp_server import MCPServer
from database import get_chats, init_db

app = Flask(__name__)
mcp = MCPServer()

@app.route("/", methods=["GET", "POST"])
def home():
    suggestion = None

    if request.method == "POST":
        symptoms = request.form.get("symptoms")
        suggestion = mcp.process(symptoms)

    chats = get_chats()

    return render_template("index.html", suggestion=suggestion, chats=chats)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
