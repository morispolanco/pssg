import streamlit as st
import requests
import json

# Función para realizar la solicitud a la API
def run_api(inputs):
    url = "https://api.respell.ai/v1/run"
    headers = {
        "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "spellId": "SwM1TRZNvRQjaA-bJ969H",
        "inputs": inputs
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Crear la aplicación Streamlit
def main():
    st.title("App de Streamlit con API Respell")

    # Definir los campos de entrada
    email = st.text_input("Email")
    name = st.text_input("Name")
    location = st.text_input("Location")
    price = st.text_input("Price")
    product_or_service = st.text_input("Product or Service")
    user_input = st.text_input("Input")

    # Ejecutar la solicitud a la API cuando se hace clic en el botón
    if st.button("Submit"):
        inputs = {
            "email": email,
            "name": name,
            "location": location,
            "price": price,
            "product_or_service": product_or_service,
            "input": user_input
        }
        response = run_api(inputs)
        
        # Mostrar los resultados
        st.subheader("Resultados:")
        st.json(response)

if __name__ == "__main__":
    main()
