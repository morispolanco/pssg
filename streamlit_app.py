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

# Create the Streamlit application
def main():
    st.title("Personalized Sales Strategy Generator")
    st.write("Welcome to the personalized sales strategy generator, a revolutionary tool designed to transform your sales approach. This application crafts tailored sales strategies based on LinkedIn user profiles and specific product details.")

    # Define the input fields in a column layout
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
        email = st.text_input("Email")
        location = st.text_input("Location")
    with col2:
        product_or_service = st.text_input("Product or Service")
        price = st.text_input("Price")
        language = st.text_input("Language")

    # Execute the request to the API when the button is clicked
    if st.button("Generate Strategy"):
        inputs = {
            "name": name,
            "email": email,
            "location": location,
            "product_or_service": product_or_service,
            "price": price,
            "language": input
        }
        response = run_api(inputs)
        
        # Mostrar los resultados
        st.subheader("Resultados:")
        st.markdown(response)

if __name__ == "__main__":
    main()
