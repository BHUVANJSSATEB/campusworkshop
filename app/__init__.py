"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaao0rhp8u791gvfr8g-a.oregon-postgres.render.com",
        database="todo_k0dk",
        user="todo_k0dk_user",
        password="dakLa7OyVeDOdYiuk3SUSZC9qV0HRZPa")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
