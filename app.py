from flask import Flask, render_template
from dotenv import load_dotenv
from database.db import db
import os
from models.bases_datos import Guarderia,Cuidador,Perros
from models.usuario_db import Usuarios
from controllers.controlador_bases import Ctrl_Bases
from controllers.controller_user import controller_user, controller_inicio_sesion,controller_admin
from flask_login import LoginManager, login_user, login_required


load_dotenv()

app = Flask(__name__, template_folder="views")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

Ctrl_Bases(app)


login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

secret_key = os.urandom(24)
app.config["SECRET_KEY"] = secret_key

app.register_blueprint(controller_user)
app.register_blueprint(controller_inicio_sesion)
app.register_blueprint(controller_admin)

    
if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
