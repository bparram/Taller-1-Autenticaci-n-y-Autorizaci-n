from flask import Flask, jsonify, render_template
from models.bases_datos import Guarderia, Cuidador, Perros

def Ctrl_Bases(app):
    @app.route("/")
    def P_principal():
     return render_template("index.html")

    
    @app.route("/tiendas")
    def info_guarderias():
        guarderias = Guarderia.query.all()
        lista = [
            {
                "idGuarderia": guarderia.idGuarderia,
                "Nombre_Guarderia": guarderia.Nombre_Guarderia,
                "Direccion": guarderia.Direccion,
                "Telefono": guarderia.Telefono
            } 
            for guarderia in guarderias
        ]
        return render_template("tiendas.html", guarderias=guarderias)
    
    @app.route("/lassie")
    def info_lassie():
       
        lassie = Perros.query.filter(Perros.Nombre_Perro.ilike ('lassie%')).all()
        
        cantidad = len(lassie)
                
        return render_template("traer_perros.html", lassie=lassie, cantidad=cantidad)
    
    @app.route('/asignar_perros')
    def asignar_perros():
      cuidador_nuevo = Cuidador.query.filter(Cuidador.Nombre.ilike('Mario%')).first()

      small_dogs = Perros.query.filter(Perros.Peso < 3).all()
      for perro in small_dogs:
          perro.Id_Cuidador = cuidador_nuevo.idCuidador

      contar_perros_asignados = len(small_dogs)
      asignados =  [
            {
                "idPerro": perro.idPerros,
                "Nombre": perro.Nombre_Perro,
                "Raza": perro.Raza_Perro,
                "Edad": perro.Edad,
                "Peso": perro.Peso
            }
            for perro in small_dogs
        ]

      return render_template("perros_asignados.html", contar_perros_asignados = contar_perros_asignados, asignados = asignados)

    
    @app.route('/lista_perros')
    def listar_perros():
       lista = Perros.query.all()
       perros = [perro.to_dict() for perro in lista]
       return render_template('lista_perros.html',lista=perros)