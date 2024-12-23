from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def load_user(user_id):
    return Usuario.query.get(int(user_id))

if usuario and check_password_hash(usuario.contrasena, contrasena):
    login_user(usuario)
    flash("Inicio de sesión exitoso!", "success")
    return redirect(url_for('rutas.index')) 

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'rutas.login'  

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    import rutas
    app.register_blueprint(rutas.bp)

    return app
