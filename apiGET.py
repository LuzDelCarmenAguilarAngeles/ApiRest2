from flask import Flask, request

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir la ruta y los métodos GET, POST, PUT, DELETE
@app.route('/saludo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludo():
    if request.method == 'GET':
        return "¡Hola! Bienvenido a la API. (GET)"
    elif request.method == 'POST':
        return "Has enviado una solicitud POST. (POST)"
    elif request.method == 'PUT':
        return "Has enviado una solicitud PUT. (PUT)"
    elif request.method == 'DELETE':
        return "Has enviado una solicitud DELETE. (DELETE)"
    else:
        return "Método no permitido", 405

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
