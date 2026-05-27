from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar y registrar cada blueprint
    from app.blueprints.bloque2.routes import bloque2_bp
   
    app.register_blueprint(bloque2_bp, url_prefix="/bloque2")
    
    return app
