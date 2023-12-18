from flask import Flask

def create_app(test_config=None):
    """Create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev') # change this later to load from config file where secret is not exposed

    @app.route('/hello')
    def hello():
        """Hello world route for initial testing"""
        return "Hello World!"
    
    return app
