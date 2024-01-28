import requests
import json
import streamlit as st

# API key and endpoint
API_KEY = "260cee54-6d54-48ba-92e8-bf641b5f4805"
ENDPOINT = "https://api.respell.ai/v1/run"

# Spell ID and version ID
SPELL_ID = "n834YRtN-Sw_lg1U4nZJ7"
SPELL_VERSION_ID = "ZM_PQe-MjMZxERXkBmhvf"

# Function to make API request
def make_api_request(inputs):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "spellId": SPELL_ID,
        "spellVersionId": SPELL_VERSION_ID,
        "inputs": inputs
    })
    response = requests.post(ENDPOINT, headers=headers, data=data)
    return response.json()

# Streamlit app
def main():
    st.title("My App")

    # Input fields
    product_or_service = st.text_input("Product or Service")
    price = st.text_input("Price")
    location = st.text_input("Location")
    name = st.text_input("Name")
    email = st.text_input("Email")

    # Button to submit inputs
    if st.button("Submit"):
        inputs = {
            "product_or_service": product_or_service,
            "price": price,
            "location": location,
            "name": name,
            "email": email
        }
        result = make_api_request(inputs)
        st.write(result)

if __name__ == "__main__":
    main()

