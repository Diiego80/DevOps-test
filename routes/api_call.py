from flask import jsonify
import requests
from decouple import config

def obtener_endpoint():
    try:
        
        print("Inicio de servicio")
        url = "https://dn8mlk7hdujby.cloudfront.net/interview/insurance/58"
        #print("URL:", url)

        response_endpoint = requests.get(url)

        response_text = response_endpoint.text

        print("Respuesta Endpoint:", response_text)
        return jsonify({"Endpoint Response": response_endpoint.text}), 200
    

    except Exception as err:
        print("Error al obtener el endpoint:", err)

        return jsonify({"Error":"Problema en el servidor, contactar a Administrador"}), 400