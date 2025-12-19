from flask import Flask, send_from_directory
from flask_cors import CORS
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
dist_dir = os.path.normpath(os.path.join(base_dir, "..", "frontend", "dist"))

app = Flask(__name__, static_folder=dist_dir, static_url_path="/")
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path: str):
    file_path = os.path.join(dist_dir, path)
    if path != "" and os.path.exists(file_path) and os.path.isfile(file_path):
        return send_from_directory(dist_dir, path)
    return send_from_directory(dist_dir, 'index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
