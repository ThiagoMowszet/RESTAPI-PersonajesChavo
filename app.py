from flask import Flask, jsonify, request

app = Flask(__name__)
  

from personajes import personajes

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})


@app.route('/personajes', methods=['GET'])
def getPersonajes():
    return jsonify({"personajes": personajes, "message": "Lista de Personajes"})



@app.route('/personajes', methods=['POST'])
def addPersonaje():
    new_personaje = {
        "Nombre": request.json['Nombre'],
        "Edad": request.json['Edad'],
        "NumeroVecindad": request.json['NumeroVecindad']
    }   
    personajes.append(new_personaje)
    return jsonify({"mesage": "Producto agregado satisfactoriamente", "personjes": personajes})


@app.route('/personajes/<string:personaje_name>', methods=['PUT'])
def editPersonaje(personaje_name):
   personajeFound = [personaje for personaje in personajes if personaje['Nombre'] == personaje_name]
   if (len(personajeFound) > 0):
       personajeFound[0]['Nombre'] = request.json['Nombre']
       personajeFound[0]['Edad'] = request.json['Edad']
       personajeFound[0]['NumeroVecindad'] = request.json['NumeroVecindad']
       return jsonify({
           "message": "Producto actualizado",
           "personaje": personajeFound[0]
       })
   return jsonify({"message": "Producto no encontrado"})


@app.route('/personajes/<string:personaje_name>')
def getPersonaje(personaje_name):
    personajeFound = [personaje for personaje in personajes if personaje['Nombre'] == personaje_name]
    if (len(personajeFound) > 0):
        return jsonify({"personaje": personajeFound[0]})
    return jsonify({"message": "Personaje no encontrado"})




@app.route('/personajes/<string:personaje_name>', methods=['DELETE'])
def deletePersonaje(personaje_name):
    personajeFound = [personaje for personaje in personajes if personaje['Nombre'] == personaje_name]
    if len(personajeFound) > 0:
        personajes.remove(personajeFound[0])
        return jsonify({
            "message": "Producto eliminado",
            "personaje": personajes
        })
    return jsonify({"message": "Personaje no encontrado"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)