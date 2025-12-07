import os
from flask import Flask
from dotenv import load_dotenv


load_dotenv()




def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
    SECRET_KEY=os.environ.get("SECRET_KEY", "dev_secret"),
    )


    from .routes import bp
    app.register_blueprint(bp)


    return app