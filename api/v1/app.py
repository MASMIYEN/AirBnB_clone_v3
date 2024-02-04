#!/usr/bin/python3
"""Endpoint (route) will be to return the status of your API"""
import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close(cntxt):
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404


if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_PORT"):
    port = int(os.getenv("HBNB_API_PORT"))
else:
    port = 5000

if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
