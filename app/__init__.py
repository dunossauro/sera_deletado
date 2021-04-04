from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'hello', 200

    return app
