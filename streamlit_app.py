import tkinter as tk
import requests
import json
import streamlit as st

def llamar_api():
    # Hacer la solicitud a la API
    response = requests.post(
      "https://api.respell.ai/v1/run",
      headers={
        # Esta es tu clave API
        "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      data=json.dumps({
        "spellId": "n834YRtN-Sw_lg1U4nZJ7",
        # Este campo se puede omitir para ejecutar la versión publicada más reciente
        "spellVersionId": "TI7gzCPzWyPxRkwWB7FFj",
        # Rellenar los valores para cada uno de tus 5 bloques de entrada dinámica
        "inputs": {
          "product_or_service": product_or_service.get(),
          "price": price.get(),
          "location": location.get(),
          "name": name.get(),
          "email": email.get(),
        }
      }),
    )
    
    # Imprimir la respuesta de la API
    print(response.json())

# Crear la ventana de la interfaz de usuario
root = tk.Tk()
root.title("Llamada a la API de Stream")

# Crear y posicionar los elementos de la interfaz de usuario
tk.Label(root, text="Producto o Servicio:").pack()
product_or_service = tk.Entry(root)
product_or_service.pack()

tk.Label(root, text="Precio:").pack()
price = tk.Entry(root)
price.pack()

tk.Label(root, text="Ubicación:").pack()
location = tk.Entry(root)
location.pack()

tk.Label(root, text="Nombre:").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Email:").pack()
email = tk.Entry(root)
email.pack()

boton_llamar_api = tk.Button(root, text="Llamar a la API", command=llamar_api)
boton_llamar_api.pack()

# Ejecutar la ventana de la interfaz de usuario
root.mainloop()
