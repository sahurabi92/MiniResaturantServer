from flask import Flask
import werkzeug

from .apis import init_api
from .models import mongodb, api

werkzeug.cached_property = werkzeug.utils.cached_property
app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'RestDB'
# app.config["MONGO_URI"] = "mongodb://localhost:27017/RestDB"

app.config['MONGODB_SETTINGS'] = {
    'db': 'RestDB',
    'host': 'localhost',
    'port': 27017
}


def create_app():
    mongodb.init_app(app)
    api.init_app(app)
    init_api(api)

    with app.app_context():
        from .models import Table, Menu, Orders
    return app
