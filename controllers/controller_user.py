from flask import Flask, Blueprint, render_template,request,redirect,url_for,flash
from models.usuario_db import Usuarios
from flask_login import LoginManager,login_user,login_required


controller_user = Blueprint('Usuarios',__name__)

@controller_user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        
        user = Usuarios.query.filter_by(username=username).first()

        if user and user.password == password: 
            login_user(user)
            if user.admin == True:
                flash('Inicio de sesión exitoso como administrador', 'success')
                return redirect(url_for('pagina_principal.inicio_admin'))
            else:
                flash('Inicio de sesión exitoso', 'success')
                return redirect(url_for('dashboard.inicio'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

controller_inicio_sesion = Blueprint('dashboard',__name__)

@controller_inicio_sesion.route('/dashboard')
@login_required
def inicio():
    return render_template('inicio_sesion.html')

controller_admin = Blueprint('pagina_principal',__name__)

@controller_admin.route('/p_principal')
def inicio_admin():
    return render_template('p_principal.html')