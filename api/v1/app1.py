#!/usr/bin/python3
"""Flask server (app that updates)
"""


from flask import Flask, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    '''Handles the 404 HTTP not found.'''

    return jsonify(error='Not found'), 404

@app.errorhandler(400)
def error_400(error):
    '''Handles the 400 HTTP bad request.'''
    message = 'Bad request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        message = error.description
    return jsonify(error=message), 400

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
