from flask import Flask, jsonify, request
import requests

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# URL base de tu MockAPI
MOCK_API_URL = "https://66ecd6b22b6cf2b89c5f711e.mockapi.io/IoTCarStatus"

# Endpoint para manejar GET, POST, PUT, DELETE con ID opcional
@app.route('/saludo', methods=['GET', 'POST'])
@app.route('/saludo/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludo(id=None):
    if request.method == 'GET':
        if id:
            # Obtener un registro específico por ID desde MockAPI
            response = requests.get(f"{MOCK_API_URL}/{id}")
            if response.status_code == 200:
                return jsonify({"message": f"Registro con ID {id} encontrado.", "data": response.json()})
            else:
                return jsonify({"error": f"No se pudo encontrar el registro con ID {id}."}), response.status_code
        else:
            # Obtener todos los registros si no se proporciona un ID
            response = requests.get(MOCK_API_URL)
            if response.status_code == 200:
                return jsonify({"message": "Lista de usuarios obtenida.", "data": response.json()})
            else:
                return jsonify({"error": "Error al conectar con MockAPI"}), response.status_code

    elif request.method == 'POST':
        # Crear un nuevo registro
        payload = request.json  # Datos enviados en la solicitud POST
        response = requests.post(MOCK_API_URL, json=payload)
        if response.status_code == 201:
            return jsonify({"message": "Nuevo registro creado.", "data": response.json()})
        else:
            return jsonify({"error": "Error al crear el registro en MockAPI."}), response.status_code

    elif request.method == 'PUT':
        if id:
            # Actualizar un registro específico por ID
            payload = request.json  # Datos para actualizar
            response = requests.put(f"{MOCK_API_URL}/{id}", json=payload)
            if response.status_code == 200:
                return jsonify({"message": f"Registro con ID {id} actualizado.", "data": response.json()})
            else:
                return jsonify({"error": f"No se pudo actualizar el registro con ID {id}."}), response.status_code
        else:
            return jsonify({"error": "ID es requerido para actualizar el registro."}), 400

    elif request.method == 'DELETE':
        if id:
            # Eliminar un registro específico por ID
            response = requests.delete(f"{MOCK_API_URL}/{id}")
            if response.status_code == 200:
                return jsonify({"message": f"Registro con ID {id} eliminado."})
            else:
                return jsonify({"error": f"No se pudo eliminar el registro con ID {id}."}), response.status_code
        else:
            return jsonify({"error": "ID es requerido para eliminar el registro."}), 400

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
