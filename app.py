from flask import Flask
from config import Config
from routes import main as main_blueprint
from models import db
from werkzeug.exceptions import RequestEntityTooLarge
from flask import jsonify

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Set maximum upload size to 100 MB
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB

    # Initialize the database and register routes
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(main_blueprint)

    # Handle large file uploads
    @app.errorhandler(RequestEntityTooLarge)
    def handle_file_too_large(e):
        return jsonify({"error": "File is too large. Max file size is 100 MB."}), 413

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
