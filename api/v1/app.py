#!/usr/bin/python3
"""app"""
from flask import Flask
from models import storage
from os import getenv
from api.v1.views import app_views


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def close():
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", default="0.0.0.0")
    port = getenv("HBNB_API_PORT", default=5000)
    app.run(host=host, port=int(port), threaded=True)
