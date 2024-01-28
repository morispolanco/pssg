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
    response_json = response.json()
    # Remove headers
    for header in response_json["headers"]:
        del header["name"]
    return response_json["body"]

# Streamlit app
def main():
    st.title("API Call Example")

    # Input fields
    name = st.text_input("Name")
    location = st.text_input("Location")
    email = st.text_input("Email")
    product_or_service = st.text_input("Product or Service")
    price = st.text_input("Price")

    # Button to submit inputs
    if st.button("Submit"):
        inputs = {
            "name": name,
            "location": location,
            "email": email,
            "product_or_service": product_or_service,
            "price": price
        }
        result = make_api_request(inputs)
        st.write(result)

if __name__ == "__main__":
    main()
