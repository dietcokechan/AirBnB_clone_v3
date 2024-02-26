#!/usr/bin/python3
"""app"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def get_status():
    return jsonify({'status': 'OK'})
