import streamlit as st
import requests
import json

st.title("Call API")

email = st.text_input("Email", "Example text")
name = st.text_input("Name", "Example text")
location = st.text_input("Location", "Example text")
price = st.text_input("Price", "Example text")
product_or_service = st.text_input("Product or Service", "Example text")
language = st.text_input("Language", "Example text")

if st.button("Call API"):
    # Check for empty inputs
    if not email or not name or not location or not price or not product_or_service or not language:
        st.error("Please fill in all fields.")
    else:
        try:
            response = requests.post(
                "https://api.respell.ai/v1/run",
                headers={
                    "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "spellId": "SwM1TRZNvRQjaA-bJ969H",
                    "spellVersionId": "qHiqa1EwXNP1LNoj9Ow_l",
                    "inputs": {
                        "email": email,
                        "name": name,
                        "location": location,
                        "price": price,
                        "product_or_service": product_or_service,
                        "language": language,  # Corrected field name
                    }
                }),
            )
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error("API request failed.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
