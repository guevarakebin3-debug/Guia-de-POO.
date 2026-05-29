from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # Ruta principal con las tarjetas
    @app.route("/")
    def index():
        return render_template("index.html")

    # Importar y registrar blueprints
    from app.blueprints.bloque0.routes import bloque0_bp
    from app.blueprints.bloque1.routes import bloque1_bp
    from app.blueprints.bloque2.routes import bloque2_bp

    app.register_blueprint(bloque0_bp, url_prefix="/bloque0")
    app.register_blueprint(bloque1_bp, url_prefix="/bloque1")
    app.register_blueprint(bloque2_bp, url_prefix="/bloque2")
   
    from app.blueprints.bloque3.routes import bloque3_bp
    app.register_blueprint(bloque3_bp, url_prefix="/bloque3")
    
    from app.blueprints.bloque4.routes import bloque4_bp
    app.register_blueprint(bloque4_bp, url_prefix="/bloque4")

    from app.blueprints.bloque5.routes import bloque5_bp
    app.register_blueprint(bloque5_bp, url_prefix="/bloque5")

    from app.blueprints.bloque6.routes import bloque6_bp
    app.register_blueprint(bloque6_bp, url_prefix="/bloque6")
    
    from app.blueprints.bloque7.routes import bloque7_bp
    app.register_blueprint(bloque7_bp, url_prefix="/bloque7")

    from app.blueprints.bloque8.routes import bloque8_bp
    app.register_blueprint(bloque8_bp, url_prefix="/bloque8")

    from app.blueprints.bloque9.routes import bloque9_bp
    app.register_blueprint(bloque9_bp, url_prefix="/bloque9")

    from app.blueprints.bloque10.routes import bloque10_bp
    app.register_blueprint(bloque10_bp, url_prefix="/bloque10")

    from app.blueprints.bloque11.routes import bloque11_bp
    app.register_blueprint(bloque11_bp, url_prefix="/bloque11")

    from app.blueprints.bloque12.routes import bloque12_bp
    app.register_blueprint(bloque12_bp, url_prefix="/bloque12")

    from app.blueprints.bloque13.routes import bloque13_bp
    app.register_blueprint(bloque13_bp, url_prefix="/bloque13")

    from app.blueprints.bloque14.routes import bloque14_bp
    app.register_blueprint(bloque14_bp, url_prefix="/bloque14")

    from app.blueprints.bloque15.routes import bloque15_bp
    app.register_blueprint(bloque15_bp, url_prefix="/bloque15")

    from app.blueprints.bloque16.routes import bloque16_bp
    app.register_blueprint(bloque16_bp, url_prefix="/bloque16")

    from app.blueprints.bloque17.routes import bloque17_bp
    app.register_blueprint(bloque17_bp, url_prefix="/bloque17")

    from app.blueprints.bloque18.routes import bloque18_bp
    app.register_blueprint(bloque18_bp, url_prefix="/bloque18")

    from app.blueprints.bloque19.routes import bloque19_bp
    app.register_blueprint(bloque19_bp, url_prefix="/bloque19")
    
    from app.blueprints.bloque20.routes import bloque20_bp
    app.register_blueprint(bloque20_bp, url_prefix="/bloque20")

    from app.blueprints.bloque21.routes import bloque21_bp
    app.register_blueprint(bloque21_bp, url_prefix="/bloque21")


    return app

