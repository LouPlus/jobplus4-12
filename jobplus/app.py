from flask import Flask
from jobplus.config import configs

app = Flask(__name__)

@app.route('/')
def index():
    return 'good evening'

def create_app(config):
    app.config.from_object(configs.get(config))

    return app
