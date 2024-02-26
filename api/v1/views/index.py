#!/usr/bin/python3
"""app"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def get_status():
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def get_count():
    dict = {"amenities": 'Amenity',
                  "cities": 'City',
                  "places": 'Place',
                  "reviews": 'Review',
                  "states": 'State',
                  "users": 'User'}

    for i in dict.keys():
        dict[i] = storage.count(dict.get(i))
    return jsonify(dict)
