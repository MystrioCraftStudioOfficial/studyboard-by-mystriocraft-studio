"""
Optional Python/Flask server for StudyBoard.
The website does NOT require Python when opened through VS Code Live Server.
Use this only if you specifically want to serve the static files with Python.
"""
from flask import Flask, send_from_directory
from pathlib import Path

ROOT = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=str(ROOT), static_url_path="")

@app.get("/")
def home():
    return send_from_directory(ROOT, "index.html")

if __name__ == "__main__":
    print("StudyBoard is available at http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
