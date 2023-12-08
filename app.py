from flask import Flask, jsonify
from decouple import config

from routes.api_call import obtener_endpoint

#Iniciar instancia Flask
app = Flask(__name__)

app.route('/api/obtener_endpoint', methods =['POST'])(obtener_endpoint)

port = config('PORT')


def ruta_base():
    response = "La API esta respondiendo correctamente en el puerto " + port
    # print("----------------------------")
    # print(response)
    # print("----------------------------")
    mensaje = {"mensaje": response}
    return jsonify(mensaje)

app.route('/',methods=['GET'])(ruta_base)

#Inicializar server
if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=port, debug=True)
