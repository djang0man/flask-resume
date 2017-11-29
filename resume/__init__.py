import os
import json

from flask import Flask, render_template

app = Flask(__name__)

config_path = os.environ.get("CONFIG_PATH", "resume.config.DevelopmentConfig")
app.config.from_object(config_path)

from . import api
from . import views

resume = json.loads(api.profile_get('stuartdkershaw').data)

@app.route("/")
@app.route("/jinja2")
def home():
    return render_template('components.html', resume=resume)
