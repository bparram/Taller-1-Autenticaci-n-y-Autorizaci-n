from database.db import db

class Guarderia(db.Model):
    __tablename__ = 'guarderias'
    idGuarderia = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    Nombre_Guarderia = db.Column(db.String(120), nullable=False)
    Direccion = db.Column(db.String(100), nullable=True)
    Telefono = db.Column(db.Integer, nullable=True)  

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    idCuidador = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    Nombre = db.Column(db.String(120), nullable=False)
    Telefono = db.Column(db.String(100), nullable=True)
    Id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.idGuarderia'), nullable=True)  

class Perros(db.Model):
    __tablename__ = 'perros'
    idPerros = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    Nombre_Perro = db.Column(db.String(120), nullable=False)
    Raza_Perro = db.Column(db.String(120), nullable=False)
    Edad = db.Column(db.Integer, nullable=True)  
    Peso = db.Column(db.Float, nullable=False)
    Id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.idGuarderia'), nullable=True)  
    Id_Cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.idCuidador'), nullable=True)  

    def __repr__(self):
        return f"<Perros {self.idPerros}>"

    def to_dict(self):
        return {
            "idPerros": self.idPerros,
            "Nombre_Perro": self.Nombre_Perro,
            "Raza_Perro": self.Raza_Perro,
            "Edad": self.Edad,
            "Peso": self.Peso
        }

