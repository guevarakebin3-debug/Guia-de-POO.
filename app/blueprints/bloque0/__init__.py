from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar y registrar cada blueprint
    from app.blueprints.bloque0.routes import bloque0_bp
   
    app.register_blueprint(bloque0_bp, url_prefix="/bloque0")
    
    return app
