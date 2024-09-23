from flask import Flask
from os import getenv
from requests import get

import json

app = Flask(__name__)

@app.route('/')
def init_page():
  return """
    <DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <tite>FLASKAPP!</title>
    </head>
  """

@app.route('/health')
def page_health():
  return "HEALTHY", 200

if __name__ == '__main__':
  app().run(host='0.0.0.0')
