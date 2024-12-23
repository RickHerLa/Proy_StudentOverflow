from flask import Blueprint
from . import db  

bp = Blueprint('rutas', __name__)

@bp.route('/preguntas', methods=['GET'])
def obtener_preguntas():
    preguntas = preguntas.query.all() 
    return render_template('preguntas.html', preguntas=preguntas)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')

        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and check_password_hash(usuario.contrasena, contrasena):
            flash("Inicio de sesión exitoso!", "success")
            return redirect(url_for('rutas.index')) 
        else:
            flash("Credenciales incorrectas. Intenta de nuevo.", "danger")
            return redirect(url_for('rutas.login')) 

    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    flash("Has cerrado sesión.", "info")
    return redirect(url_for('rutas.login'))